import logging
import os
import sys
import time
from config import *
from telethon import TelegramClient
from telethon.sessions import MemorySession
from aiohttp import ClientSession
from pyrogram.types import Message
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid, ChannelInvalid
from pyrogram.types import Chat, User
from inspect import getfullargspec

from pyrogram import Client, errors
from aiohttp import ClientSession
from motor import motor_asyncio
from odmantic import AIOEngine
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

print("[EPIC]: Initializing AIOHTTP Session")
aiohttpsession = ClientSession() 

