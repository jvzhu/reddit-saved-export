"""
Fetch and print your saved Reddit posts and comments.

Requires REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, and REDDIT_REFRESH_TOKEN
to be set as environment variables. Get a refresh_token by running
get_token.py once.
"""

import os
import sys

import praw
from prawcore.exceptions import OAuthException, ResponseException


def main():
    required = ["REDDIT_CLIENT_ID", "REDDIT_CLIENT_SECRET", "REDDIT_REFRESH_TOKEN"]
    missing = [v for v in required if not os.environ.get(v)]
    if missing:
        print(f"Missing environment variables: {', '.join(missing)}")
        return 1

    reddit = praw.Reddit(
        client_id=os.environ["REDDIT_CLIENT_ID"],
        client_secret=os.environ["REDDIT_CLIENT_SECRET"],
        refresh_token=os.environ["REDDIT_REFRESH_TOKEN"],
        user_agent="reddit-saved-export/1.0",
    )

    try:
        me = reddit.user.me()
        print(f"Logged in as: {me.name}\n")

        count = 0
        for saved in me.saved(limit=None):
            count += 1
            if isinstance(saved, praw.models.Submission):
                print(f"[POST] {saved.title}")
                print(f"  link: {saved.shortlink}")
                if saved.selftext:
                    print(f"  preview: {saved.selftext[:100]}...")
            elif isinstance(saved, praw.models.Comment):
                print(f"[COMMENT] {saved.body[:80]}...")
                print(f"  on: {saved.submission.title}")
            print()

        if count == 0:
            print("No saved items found.")

    except OAuthException as e:
        print(f"Auth failed -- check your refresh_token: {e}")
        return 1
    except ResponseException as e:
        print(f"API error: {e}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
