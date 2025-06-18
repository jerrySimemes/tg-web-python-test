import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from pprint import pprint

BOT_TOKEN = os.getenv("BOT_TOKEN")

# 接收使用者訊息後回覆
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    pprint(update.message.to_dict())
    # user_text = update.message.text
    # reply = f"你說的是： {user_text}"
    # await update.message.reply_text(reply)
    
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton("🚀 Start!", web_app=WebAppInfo(url="https://pre-register.web.app/"))
    ]])
    await update.message.reply_text("Press Button To Start Preregistation：", reply_markup=keyboard)

# 啟動 bot
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("🤖 I'm listening...")
    app.run_polling()