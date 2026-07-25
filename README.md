# Reddit Saved Items Export

A minimal script for exporting your own saved Reddit posts and comments via [PRAW](https://praw.readthedocs.io/).

Live page: `https://YOUR_USERNAME.github.io/reddit-saved-export/` (once GitHub Pages is enabled)

## Security

No credentials are stored in this repository. `client_id`, `client_secret`, and `refresh_token`
are read from environment variables at runtime. `.env` is git-ignored.

**Never commit real tokens or secrets.** If one is ever exposed, revoke/rotate it immediately
at https://www.reddit.com/prefs/apps.

## Setup

1. Create a "script" type app at https://www.reddit.com/prefs/apps
   (redirect uri: `http://localhost:8080`)
2. Install dependencies:
   ```
   pip install praw
   ```
3. Get a refresh token (one-time):
   ```
   export REDDIT_CLIENT_ID="your_client_id"
   export REDDIT_CLIENT_SECRET="your_client_secret"
   python get_token.py
   ```
4. Set all three environment variables and run the export:
   ```
   export REDDIT_CLIENT_ID="your_client_id"
   export REDDIT_CLIENT_SECRET="your_client_secret"
   export REDDIT_REFRESH_TOKEN="token_from_step_3"
   python get_saved.py
   ```

## Files

- `get_token.py` -- one-time OAuth flow to obtain a refresh_token
- `get_saved.py` -- fetches and prints saved posts/comments
- `index.html` -- GitHub Pages landing page describing the project
- `.env.example` -- template for local environment variables (placeholders only)

## Enabling GitHub Pages

After pushing this repo to GitHub:
1. Go to **Settings → Pages**
2. Under "Source," select the `main` branch and `/ (root)` folder
3. Save -- your page will be live at `https://YOUR_USERNAME.github.io/reddit-saved-export/`
