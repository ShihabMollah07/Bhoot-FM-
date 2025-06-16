import sys, glob, importlib, logging, logging.config, pytz, asyncio
from pathlib import Path

# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("cinemagoer").setLevel(logging.ERROR)

from pyrogram import Client, idle
from database.users_chats_db import db
from info import *
from utils import temp
from typing import Union, Optional, AsyncGenerator
from Script import script 
from datetime import date, datetime 
from aiohttp import web
from plugins import web_server
from plugins.clone import restart_bots

# --- এই অংশটি পরিবর্তন করতে হবে ---
# আপনার বট ক্লাসের সঠিক path দিন
from core.bot import Bot 
from core.util.keepalive import ping_server
from core.bot.clients import initialize_clients
# ---------------------------------

ppath = "plugins/*.py"
files = glob.glob(ppath)
Bot.start()
loop = asyncio.get_event_loop()


async def start():
    print('\n')
    print('Initializing Your Bot...')
    bot_info = await Bot.get_me()
    await initialize_clients()
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem.replace(".py", "")
            plugins_dir = Path(f"plugins/{plugin_name}.py")
            import_path = "plugins.{}".format(plugin_name)
            spec = importlib.util.spec_from_file_location(import_path, plugins_dir)
            load = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(load)
            sys.modules["plugins." + plugin_name] = load
            print("Plugin Imported => " + plugin_name)
            
    if ON_HEROKU:
        asyncio.create_task(ping_server())
        
    b_users, b_chats = await db.get_banned()
    temp.BANNED_USERS = b_users
    temp.BANNED_CHATS = b_chats
    
    me = await Bot.get_me()
    temp.BOT = Bot
    temp.ME = me.id
    temp.U_NAME = me.username
    temp.B_NAME = me.first_name
    
    logging.info(f"{me.first_name} with ID: {me.id} has started!")
    logging.info(script.LOGO)
    
    tz = pytz.timezone('Dhaka/Bangladesh')
    today = date.today()
    now = datetime.now(tz)
    time = now.strftime("%H:%M:%S %p")
    
    try:
        await Bot.send_message(chat_id=LOG_CHANNEL, text=script.RESTART_TXT.format(today, time))
    except Exception as e:
        print(f"Error sending message to LOG_CHANNEL: {e}")
        print("Make sure your bot is an admin in the Log Channel with full rights.")
        
    for ch in CHANNELS:
        try:
            k = await Bot.send_message(chat_id=ch, text="**Bot Restarted**")
            await k.delete()
        except Exception as e:
            print(f"Could not send message to channel {ch}. Error: {e}")
            print("Make sure your bot is an admin in all File Channels with full rights.")
            
    try:
        if AUTH_CHANNEL:
            k = await Bot.send_message(chat_id=AUTH_CHANNEL, text="**Bot Restarted**")
            await k.delete()
    except Exception as e:
        print(f"Error sending message to AUTH_CHANNEL: {e}")
        print("Make sure your bot is an admin in the Force Subscribe Channel with full rights.")
        
    if CLONE_MODE:
        print("Restarting all cloned bots...")
        await restart_bots()
        print("Restarted all cloned bots.")
        
    app = web.AppRunner(await web_server())
    await app.setup()
    bind_address = "0.0.0.0"
    await web.TCPSite(app, bind_address, PORT).start()
    
    print(f"\n{me.first_name} is now online!\n")
    await idle()


if __name__ == '__main__':
    try:
        loop.run_until_complete(start())
    except KeyboardInterrupt:
        logging.info('Service Stopped. Goodbye!')
