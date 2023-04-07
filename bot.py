import logging,os,asyncio
from pywinauto import Desktop,Application
from telethon import TelegramClient,events
from telethon.sessions import StringSession
from dotenv import load_dotenv

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
load_dotenv(override=True)

API_ID = os.getenv('TG_API_ID')
API_HASH = os.getenv('TG_API_HASH')
BOT_TOKEN = os.getenv('BOT_TOKEN')

def start_hma():
    try:
        vpn_app = Application(backend="uia").start('C:\Program Files\Privax\HMA VPN\Vpn.exe')
        return True
    except:
        return False
def get_hma_window():
    dialog = Desktop(backend="uia").HMA
    return dialog.Pane
def connect(hma):
    try:
        connect_button = hma.ConnectButton
        if not connect_button.get_toggle_state():
            connect_button.click()
            return True
    except:
        return False
def change_ip(hma):
    try:
        changeIP = hma.Button5
        changeIP.click()
        return True
    except:
        return False

bot = TelegramClient(StringSession(), API_ID, API_HASH).start(bot_token=BOT_TOKEN)
@bot.on(events.NewMessage(pattern="/start_hma"))
async def handler(event):
    if start_hma():
        await event.reply("Done !")
    else:
        await event.reply("Error !")
@bot.on(events.NewMessage(pattern="/connect"))
async def handler(event):
    hma = get_hma_window()
    if connect(hma):
        await event.reply("Done !")
    else:
        await event.reply("Error !")
@bot.on(events.NewMessage(pattern="/switch_ip"))
async def handler(event):
    hma = get_hma_window()
    if change_ip(hma):
        await event.reply("Done !")
    else:
        await event.reply("Error !")
with bot:
    bot.run_until_disconnected()