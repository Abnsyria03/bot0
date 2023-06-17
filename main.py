import pyrogram , pyromod

from pyromod import listen
from keep import alive
from pyrogram import Client, filters, enums
p = dict(root='plugins')
import Client

db = Client("data.sqlite", 'fuck')
if not db.exists("admin_list"):
    db.set('admin_list', [5108562302,5108562302])
if not db.exists("sessions"):
    db.set('sessions', [])
if not db.exists("ban_list"):
    db.set("ban_list", [])
x = Client(name='lossclhos', api_id=19312827, api_hash='84da7f08e87849853b2fa6728e4192a2', bot_token='5496059752:AAHv276B3_GFVsodjgyyfwcCR6VUuEySpwY', workers=20, plugins=p, parse_mode=enums.ParseMode.DEFAULT)
alive()
x.run()
