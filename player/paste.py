import os
import re
import asyncio
import requests
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def paste(content: str):
    url = "https://paste.safone.tech/api"
    data = {
        "content": content,
        "heading": "BrayDen",
        "raw": True,
        "code": True,
        "footer": True,
    }
    try:
        resp = requests.post(url, json=data)
        link = "https://paste.safone.tech/" + resp.text
        rawlink = "https://paste.safone.tech/raw/" + resp.text
        return link, rawlink
    except Exception as e:
        print(e)
        return None


async def spaste(content: str):
    siteurl = "https://spaceb.in/api/v1/documents/"
    try:
        resp = requests.post(siteurl, data={"content": content, "extension": "py"})
        response = resp.json()
        link = f"https://spaceb.in/{response['payload']['id']}"
        rawlink = f"{siteurl}{response['payload']['id']}/raw"
        return link, rawlink
    except Exception as e:
        print(e)
        return None


@Client.on_message(filters.command("paste") & ~filters.edited)
async def paste_func(_, message):
    if not message.reply_to_message:
        return await message.reply("Reply To A Message With /paste")
    r = message.reply_to_message

    if not r.text and not r.document:
        return await message.reply("Only text and documents are supported.")

    m = await message.reply("Pasting...")

    if r.text:
        content = r.text
    elif r.document:
        p_file = await r.download()
        content = open(p_file, "r").read()
        os.remove(p_file)

    link, rawlink = await paste(content)
    s_link, s_rawlink = await spaste(content)
    kb = InlineKeyboardMarkup([[InlineKeyboardButton("PasteBin", url=link), InlineKeyboardButton("SpaceBin", url=s_link)]])
    await message.reply_text(
        f"**Pasted!**\nPasteBin: [Here]({rawlink})\nSpaceBin: [Here]({s_rawlink})",
        quote=True,
        reply_markup=kb,
    )
    await m.delete()

# Adopted Code !

# എന്താടാ മോനെ അടിച്ചു അടിച്ചു മാറ്റാൻ വന്നതാണോ? നാണം വേണം കേട്ടോ കുറച്ച് 😜😹.
# എന്തായാലും എടുത്തു bug ആരികും മുഴുവൻ നോക്കി ഒക്കെ add ആക്ക് കേട്ടോ 🤭
