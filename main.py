import imghdr
from asyncio import gather
from traceback import format_exc
import aiohttp

import re
import uuid
import socket
import platform
import os
import random
import time
import math
import json
import string
import traceback
import psutil
import asyncio
import wget
import motor.motor_asyncio
import pymongo
import aiofiles
import datetime
from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *
from config import *
from asyncio import *
import heroku3
import requests

from apis.api import make_carbon

from io import BytesIO
from traceback import format_exc
from apis.aio import *

#---------------------------Gen Logo Epic-------------------------------------#

app = Client(
    "Epic Logo",
    bot_token= BOT_TOKEN,
    api_id= API_ID,
    api_hash= API_HASH,
)

@app.on_message(filters.command("carbon"))
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴄᴀʀʙᴏɴ 😡"
        )
    if not message.reply_to_message.text:
        return await message.reply_text(
            "ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴄᴀʀʙᴏɴ 😡"
        )
    m = await message.reply_text("⎐ᴘʀᴏᴄᴇꜱꜱɪɴɢ.....")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("ɢᴇɴᴏʀᴀᴛɪɴɢ....")
    await m.edit("▱▱▱▱▱▱▱▱▱")
    await m.edit("▰▱▱▱▱▱▱▱▱")
    await m.edit("▰▰▱▱▱▱▱▱▱")
    await m.edit("▰▰▰▱▱▱▱▱▱")
    await m.edit("▰▰▰▰▱▱▱▱▱")
    await m.edit("▰▰▰▰▰▱▱▱▱")
    await m.edit("▰▰▰▰▰▰▱▱▱")
    await m.edit("▰▰▰▰▰▰▰▱▱")
    await m.edit("▰▰▰▰▰▰▰▰▱")
    await m.edit("▰▰▰▰▰▰▰▰▰")
    await m.edit("ꜱᴇɴᴅɪɴɢ.....")
    await app.send_document(message.chat.id, carbon)
    await m.delete()
    carbon.close()
