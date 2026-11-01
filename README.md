# CineHubPro File-to-Link Bot (modified existing project)

This keeps the original Telegram file-link streaming backend and adds channel auto-link generation plus a CineHubPro responsive media page and configurable ad slots.

## Channel auto-link
- Add the bot as an administrator to the channel (must be able to read posts).
- Set `LOG_CHANNEL` to a private storage/log channel where the bot can copy media.
- Set `URL` to the public base URL with trailing slash, e.g. `https://your-koyeb-app.koyeb.app/`.
- Upload supported media in the source channel. The bot replies with Watch and Download links.
- Existing private-chat file-to-link flow remains available.

## Ads
Set `AD_HTML` in the deployment environment to your ad network's approved HTML/JS snippet. It appears above and below the media content. Only use snippets from a trusted ad provider. Some providers require domain verification and may prohibit ads on certain content.

## Main environment variables
`API_ID`, `API_HASH`, `BOT_TOKEN`, `DATABASE_URI`, `DATABASE_NAME`, `LOG_CHANNEL`, `URL`, `PORT`.
Optional: `AD_HTML`, `SITE_NAME`, `SHORTLINK`, `SHORTLINK_URL`, `SHORTLINK_API`.

## Important
- This is a modified version of the uploaded FileToLink project, not a newly rebuilt backend.
- The web page streams the original media with the existing byte-range implementation. It does not transcode or create additional qualities.
- Use only media you own or are authorized to distribute.
- Keep bot/database credentials private; never commit them to GitHub.
