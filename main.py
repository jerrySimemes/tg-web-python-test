import os
import telepot
import time
from telepot.loop import MessageLoop
from pprint import pprint

# 測試是否有連上自己的 bot
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telepot.Bot(BOT_TOKEN)
# print(bot.getMe())

# 從 telegram 上接收訊息
def handle(msg):
    pprint(msg)
    chat_id = msg['chat']['id']
    # from_id = msg['from']['id']
    text = '你說的是： ' + msg['text']
    # photo = 'https://pic.pimg.tw/like9417/1504869777-564645577.jpg?v=1504869878'
    photo = 'https://i.meee.com.tw/7Y3VRQ7.jpg'
    
    # 用 bot 回訊息在 telegram 上
    bot.sendMessage(chat_id, text, parse_mode=None, disable_web_page_preview=None, disable_notification=None, reply_to_message_id=None, reply_markup=None)
    # 用 bot 回圖片在 telegram 上
    bot.sendPhoto(chat_id, photo, caption=None, parse_mode=None, disable_notification=None, reply_to_message_id=None, reply_markup=None)

MessageLoop(bot, handle).run_as_thread()
print("I'm listening...")

while 1:
    time.sleep(5)