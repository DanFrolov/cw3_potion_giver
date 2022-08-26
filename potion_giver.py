from telethon import TelegramClient, events, connection
import time
import datetime
from datetime import datetime, timedelta
import re
import asyncio
import math
import emoji
import sys

api_id = 1284946
api_hash = 'f1cadcc89dafe7114c78d379c4531c75'
session_name = "cw3_giver"
client = TelegramClient(session_name, api_id, api_hash)

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
  
chat = -1001380922754
#chat = -465743828

game_bot = 265204902

async def start_time():
    print(f"Started at {time.strftime('%X')}")

#send info with guild_members to the guild_chat
@client.on(events.NewMessage(chats=[chat]))
async def command_ping(event):
    if "/ping" in event.raw_text:
        print("Start")
        await client.send_message(game_bot, "/g_list")

#Here we catch messages from the specific chat and send it to the Chat Wars bot
@client.on(events.NewMessage(chats=[chat]))
async def command_chat(event):
    if "/rage" in event.raw_text:
        await client.send_message(game_bot, "/g_withdraw p01 01 p02 01 p03 1")
    elif "/peace" in event.raw_text:
        await client.send_message(game_bot, "/g_withdraw p04 1 p05 1 p06 1")
    elif "/morph" in event.raw_text:
        await client.send_message(game_bot, "/g_withdraw p19 1 p20 1 p21 1")
    elif "/mana" in event.raw_text:
        await client.send_message(game_bot, "/g_withdraw p13 1 p14 1 p15 1")

#Here we forward the response from the Chat Wars bot
@client.on(events.NewMessage(from_users = [game_bot]))
async def bot_reply(event):
    await asyncio.sleep(1)
    if 'Withdrawing' in event.raw_text:
        await client.forward_messages(chat, event.message)
    elif '#20' in event.raw_text:
        await client.forward_messages(chat, event.message)
    elif 'Ты сейчас занят' in event.raw_text:
        await client.send_message(chat, "Разливаю зелья по пробиркам. Попробуй снова через 5 минут.")
    elif 'Not enough items' in event.raw_text:
        await client.send_message(chat, "Весь алкоголь был выпит, приходи позже.")

client.start()
client.run_until_disconnected()
