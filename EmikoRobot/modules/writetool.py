import requests
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from EmikoRobot import BOT_NAME, BOT_USERNAME
from EmikoRobot import pbot as emiko


@emiko.on_message(filters.command("write"))
async def handwrite(_, message: Message):
    if not message.reply_to_message:
        text = message.text.split(None, 1)[1]
        m = await emiko.send_message(
            message.chat.id, "`Please wait...,\n\nWriting your text...`"
        )
        API = f"https://api.sdbots.tk/write?text={text}"
        req = requests.get(API).url
        caption = f"""
Successfully Written Text 💘
✨ **Written By :** [{BOT_NAME}](https://t.me/{bu})
🥀 **Requested by :** {message.from_user.mention}
❄ **Link :** `{req}`
"""
        await m.delete()
        await emiko.send_photo(
            message.chat.id,
            photo=req,
            caption=caption,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Telegraph", url=f"{req}")]]
            ),
        )
    else:
        lol = message.reply_to_message.text
        m = await emiko.send_message(
            message.chat.id, "`Please wait...,\n\nWriting your text...`"
        )
        API = f"https://api.sdbots.tk/write?text={lol}"
        req = requests.get(API).url
        caption = f"""
Successfully Written Text 💘
✨ **Written By :** [{BOT_NAME}](https://t.me/{bu})
🥀 **Requested by :** {message.from_user.mention}
❄ **Link :** `{req}`
"""
        await m.delete()
        await emiko.send_photo(
            message.chat.id,
            photo=req,
            caption=caption,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("• ᴛᴇʟᴇɢʀᴀᴩʜ •", url=f"{req}")]]
            ),
        )


__mod_name__ = "writetool"

__help__ = """
 Writes the given text on white page with a pen 🖊
❍ /write <text> *:* Writes the give"""
