from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8678805338:AAFxrQBnfcGdPUmzWmgJxjqvP2a5K9NmcPA"

8678805338:AAFxrQBnfcGdPUmzWmgJxjqvP2a5K9NmcPA

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 PlanenNews Bot работает!")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
