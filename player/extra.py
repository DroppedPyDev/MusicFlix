import os
import asyncio
import time
import shlex
import requests
from datetime import datetime
from pyrogram.errors import UserNotParticipant
from plugins.extract_user import extract_user, last_online
from telegraph import upload_file
from typing import Callable, Coroutine, Dict, List, Tuple, Union
from json import JSONDecodeError
from pyrogram import Client, filters


@Client.on_message(filters.command(["telegraph", "tgm"]))
async def telegraph(client, message):
    replied = message.reply_to_message
    if not replied:
        await message.reply("Reply to a supported media file")
        return
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 5242880)
        or (
            replied.video
            and replied.video.file_name.endswith(".mp4")
            and replied.video.file_size <= 5242880
        )
        or (
            replied.document
            and replied.document.file_name.endswith(
                (".jpg", ".jpeg", ".png", ".gif", ".mp4"),
            )
            and replied.document.file_size <= 5242880
        )
    ):
        await message.reply("Not supported!")
        return
    download_location = await client.download_media(
        message=message.reply_to_message,
        file_name="root/downloads/",
    )
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.reply(message, text=document)
    else:
        await message.reply(f"**[Here's Your Telegraph Link](https://telegra.ph{response[0]})**", disable_web_page_preview=False)
    finally:
        os.remove(download_location)

# ====== TELEGRAPH ======


@Client.on_message(filters.command(["whois", "info"]))
async def who_is(client, message):
    """ extract user information """
    status_message = await message.reply_text("`Getting Information....`")
    from_user = None
    from_user_id, _ = extract_user(message)
    try:
        from_user = await client.get_users(from_user_id)
    except Exception as error:
        await status_message.edit(str(error))
        return
    if from_user is None:
        await status_message.edit("no valid user_id / message specified")
        return
    
    first_name = from_user.first_name or ""
    last_name = from_user.last_name or ""
    username = from_user.username or ""
    
    message_out_str = (
        "<b>Name:</b> "
        f"<a href='tg://user?id={from_user.id}'>{first_name}</a>\n"
        f"<b>Suffix:</b> {last_name}\n"
        f"<b>Username:</b> @{username}\n"
        f"<b>User ID:</b> <code>{from_user.id}</code>\n"
        f"<b>User Link:</b> {from_user.mention}\n" if from_user.username else ""
        f"<b>Is Deleted:</b> True\n" if from_user.is_deleted else ""
        f"<b>Is Verified:</b> True" if from_user.is_verified else ""
        f"<b>Is Scam:</b> True" if from_user.is_scam else ""
        # f"<b>Is Fake:</b> True" if from_user.is_fake else ""
        f"<b>Last Seen:</b> <code>{last_online(from_user)}</code>\n\n"
    )

    if message.chat.type in ["supergroup", "channel"]:
        try:
            chat_member_p = await message.chat.get_member(from_user.id)
            joined_date = datetime.fromtimestamp(
                chat_member_p.joined_date or time.time()
            ).strftime("%Y.%m.%d %H:%M:%S")
            message_out_str += (
                "<b>Joined on:</b> <code>"
                f"{joined_date}"
                "</code>\n"
            )
        except UserNotParticipant:
            pass
    chat_photo = from_user.photo
    if chat_photo:
        local_user_photo = await client.download_media(
            message=chat_photo.big_file_id
        )
        await message.reply_photo(
            photo=local_user_photo,
            quote=True,
            caption=message_out_str,
            disable_notification=True
        )
        os.remove(local_user_photo)
    else:
        await message.reply_text(
            text=message_out_str,
            quote=True,
            disable_notification=True
        )
    await status_message.delete()

# Need an Updation please wait some time 

# എന്താടാ മോനെ അടിച്ചു അടിച്ചു മാറ്റാൻ വന്നതാണോ? നാണം വേണം കേട്ടോ കുറച്ച് 😜😹.
# എന്തായാലും എടുത്തു bug ആരികും മുഴുവൻ നോക്കി ഒക്കെ add ആക്ക് കേട്ടോ 🤭
