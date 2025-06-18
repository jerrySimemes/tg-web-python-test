import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, InputMediaPhoto
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters, CommandHandler
from pprint import pprint

BOT_TOKEN = os.getenv("BOT_TOKEN")

# 接收使用者訊息後回覆
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pprint(update.message.to_dict()) 
    await update.message.reply_text(f'Hi {update.effective_user.first_name}, you can use "/" to see cammands')

# /start cammand func
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🚀 Start!", web_app=WebAppInfo(url="https://pre-register.web.app/"))],
        [InlineKeyboardButton("🎮 Mini Game", web_app=WebAppInfo(url="https://example.com/"))],
        [InlineKeyboardButton("📞 Simemes X", url="https://x.com/simemesdotxyz/")]
    ])
    
    # 傳送圖片 + 按鈕
    await update.message.reply_photo(
        photo="https://i.meee.com.tw/8y2okGj.png",
        caption=f"Hello {update.effective_user.first_name} 👋\nPlease click the button below to pre-register or contact us.：",
        reply_markup=keyboard
    )
    
# 啟動 bot
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(CommandHandler("start", start))
    print("🤖 I'm listening...")
    app.run_polling()