"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter

# -- Constants -- #
ALIVE = "എന്നെ ചീത്ത വിളിക്കു... വേണമെങ്കിൽ നല്ല ഇടി ഇടിക്കു... പക്ഷെ ഉപദേശിക്കരുത്....." 
HELP = "ദൈവമേ എന്നെ മാത്രം രക്ഷിക്കണേ...."
REPO = "[നമ്മൾ നമ്മൾ പോലുമറിയാതെ അധോലോകം ആയി മാറിക്കഴിഞ്ഞിരിക്കുന്നു ഷാജിയേട്ടാ...](https://github.com/Samantha-a/Film-Club)"
CHANNEL = "<a href='https://t.me/moviespot00100'>𝐌𝐒 𝐔𝐏𝐃𝐀𝐓𝐄𝐒</a>"
GROUP = "<a href='https://t.me/moviespot001100'>𝐌𝐨𝐯𝐢𝐞 𝐒𝐩𝐨𝐭</a>"
OWNER = "<a href='https://t.me/zinan00100'>𝐙𝐢𝐧𝐚𝐧 𝐓𝐞𝐜𝐡 2.𝐎 {ALIVE}</a>"
# -- Constants End -- #


@Client.on_message(filters.command("alive", COMMAND_HAND_LER) & f_onw_fliter)
async def check_alive(_, message):
    await message.reply_text(ALIVE)


@Client.on_message(filters.command("help", COMMAND_HAND_LER) & f_onw_fliter)
async def help_me(_, message):
    await message.reply_text(HELP)


@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")


@Client.on_message(filters.command("repo", COMMAND_HAND_LER) & f_onw_fliter)
async def repo(_, message):
    await message.reply_text(REPO)


@Client.on_message(filters.command("channel", COMMAND_HAND_LER) & f_onw_fliter)
async def check_CHANNEL(_, message):
    await message.reply_text(CHANNEL)



@Client.on_message(filters.command("group", COMMAND_HAND_LER) & f_onw_fliter)
async def check_group(_, message):
    await message.reply_text(GROUP)

@Client.on_message(filters.command("owner", COMMAND_HAND_LER) & f_onw_fliter)
async def check_owner(_, message):
    await message.reply_text(OWNER)
