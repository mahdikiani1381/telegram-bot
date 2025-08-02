from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from config import TELEGRAM_TOKEN
from recommender import get_investment_advice
from scheduler import start_scheduler
from crypto_price import get_dollar_price, get_bitcoin_price

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 سلام! به بات سرمایه‌گذاری مهدی خوش آمدی. برای دریافت پیشنهاد، /suggest رو بزن.")

async def suggest(update: Update, context: ContextTypes.DEFAULT_TYPE):
    advice = get_investment_advice()
    await update.message.reply_text(advice)

async def prices(update: Update, context: ContextTypes.DEFAULT_TYPE):
    dollar = get_dollar_price()
    bitcoin = get_bitcoin_price()
    msg = f"💵 قیمت فعلی دلار: {dollar} تومان\n₿ قیمت بیت‌کوین: {bitcoin} دلار"
    await update.message.reply_text(msg)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("suggest", suggest))
    app.add_handler(CommandHandler("prices", prices))

    start_scheduler()

    app.run_polling()
