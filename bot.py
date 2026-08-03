from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

TOKEN = "8678805338:AAHPumjkRMOvkd81aPJ_H7kjiVJWi18V3Ac"
NEWS_API_KEY = "f6d056f516504ce1b83f405342ac1b50"
CHANNEL = "@PlanenNews"
ADMIN_ID = 8513038295


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 PlanenNews Bot работает!"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - запуск\n"
        "/help - помощь\n"
        "/post ТЕКСТ - опубликовать новость"
    )


async def post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("❌ Нет доступа.")
        return

    text = " ".join(context.args)

    if not text:
        await update.message.reply_text(
            "Используй:\n/post Текст новости"
        )
        return

    await context.bot.send_message(
        chat_id=CHANNEL,
        text=text
    )

    await update.message.reply_text("✅ Новость опубликована!")


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("post", post))

    print("Bot started")

    app.run_polling()


if __name__ == "__main__":
    main()