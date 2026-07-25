"""
One-time script to obtain a Reddit OAuth refresh_token.

Usage:
    export REDDIT_CLIENT_ID="your_client_id"
    export REDDIT_CLIENT_SECRET="your_client_secret"
    python get_token.py

Opens a browser window for you to approve access, then prints a
refresh_token to store as REDDIT_REFRESH_TOKEN. This token is long-lived
and grants access to your account -- treat it like a password.
"""

import os
import random
import socket
import sys
import webbrowser

import praw


def receive_connection():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("localhost", 8080))
    server.listen(1)
    client = server.accept()[0]
    server.close()
    return client


def send_message(client, message):
    client.send(f"HTTP/1.1 200 OK\r\n\r\n{message}".encode("utf-8"))
    client.close()


def main():
    client_id = os.environ.get("REDDIT_CLIENT_ID")
    client_secret = os.environ.get("REDDIT_CLIENT_SECRET")

    if not client_id or not client_secret:
        print("Set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET before running.")
        return 1

    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri="http://localhost:8080",
        user_agent="reddit-saved-export/1.0",
    )

    state = str(random.randint(0, 65000))
    # "identity" confirms who you are; "history" and "save" are needed to read saved items.
    url = reddit.auth.url(["identity", "history", "save"], state, "permanent")
    print(f"Open this URL in your browser to authorize:\n{url}")
    webbrowser.open(url)

    client = receive_connection()
    data = client.recv(1024).decode("utf-8")
    param_tokens = data.split(" ", 2)[1].split("?", 1)[1].split("&")
    params = dict(token.split("=") for token in param_tokens)

    if state != params.get("state"):
        send_message(client, f"State mismatch. Expected {state}, got {params.get('state')}")
        return 1
    if "error" in params:
        send_message(client, params["error"])
        return 1

    refresh_token = reddit.auth.authorize(params["code"])
    send_message(client, "Success! You can close this tab and return to your terminal.")
    print(f"\nYour refresh_token:\n{refresh_token}")
    print("\nStore it as an environment variable -- do not commit it anywhere.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
