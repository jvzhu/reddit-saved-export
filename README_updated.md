# Reddit Saved Items Export

[![Secret scan](https://github.com/jvzhu/reddit-saved-export/actions/workflows/secret-scan.yml/badge.svg)](https://github.com/jvzhu/reddit-saved-export/actions/workflows/secret-scan.yml)
[![Lint](https://github.com/jvzhu/reddit-saved-export/actions/workflows/lint.yml/badge.svg)](https://github.com/jvzhu/reddit-saved-export/actions/workflows/lint.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A minimal script for exporting your own saved Reddit posts and comments via [PRAW](https://praw.readthedocs.io/).

Live page: `https://jvzhu.github.io/reddit-saved-export/`

## Demo

Example output (illustrative — run it yourself to see your actual saved items):

![Terminal demo](demo/terminal-demo.svg)

## Security

No credentials are stored in this repository. `client_id`, `client_secret`, and `refresh_token`
are read from environment variables at runtime. `.env` is git-ignored, and a `secret-scan`
GitHub Action runs on every push to catch anything accidentally committed.

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
- `demo/terminal-demo.svg` -- illustrative example of script output
- `.github/workflows/` -- CI: secret scanning + Python lint
- `LICENSE` -- MIT

## Enabling GitHub Pages

After pushing this repo to GitHub:
1. Go to **Settings → Pages**
2. Under "Source," select the `main` branch and `/ (root)` folder
3. Save -- your page is live at `https://jvzhu.github.io/reddit-saved-export/`

## License

MIT -- see [LICENSE](LICENSE).
