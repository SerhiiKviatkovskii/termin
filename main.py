from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7848693387:AAFCzfHbp6KFPeWMhT7shP0o08l4Snak_SM"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Vitajte! Tento bot vám bude posielať upozornenia na voľné termíny. Prístup máte po aktivácii predplatného.")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ℹ️ Máte aktívne predplatné. Sledujeme termíny pre vás.")

async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💳 Na získanie prístupu kliknite na tlačidlo nižšie a aktivujte si predplatné:

https://t.me/tribute?start=ВАША_ССЫЛКА_НА_ПОДПИСКУ")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("buy", buy))
    app.run_polling()

if __name__ == "__main__":
    main()
