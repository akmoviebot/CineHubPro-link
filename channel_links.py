import logging
from urllib.parse import quote_plus
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from info import URL, LOG_CHANNEL
from TechVJ.util.file_properties import get_name, get_hash

@Client.on_message(filters.channel & (filters.document | filters.video | filters.audio | filters.animation))
async def channel_media_link(client, message):
    """Mirror supported channel media to the configured log/source chat and reply with CineHubPro links."""
    try:
        saved = await client.copy_message(
            chat_id=LOG_CHANNEL,
            from_chat_id=message.chat.id,
            message_id=message.id,
        )
        filename = get_name(saved) or "media"
        encoded = quote_plus(filename)
        file_hash = get_hash(saved)
        base = URL.rstrip("/") + "/"
        stream = f"{base}watch/{saved.id}/{encoded}?hash={file_hash}"
        download = f"{base}{saved.id}/{encoded}?hash={file_hash}"
        await message.reply_text(
            f"🎬 <b>CineHubPro link generated</b>\n\n"
            f"📁 <code>{filename}</code>\n\n"
            f"▶️ <a href=\"{stream}\">Watch online</a>\n"
            f"⬇️ <a href=\"{download}\">Download</a>",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("▶️ Stream", url=stream),
                InlineKeyboardButton("⬇️ Download", url=download),
            ]]),
            disable_web_page_preview=True,
        )
    except Exception:
        logging.exception("Could not generate channel media link")
