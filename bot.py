import os
import logging
import requests
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

TOKEN = os.getenv("TOKEN")
CHANNEL = os.getenv("CHANNEL")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

LAST_NEWS = set()

NEWS_URL = (
    "https://newsapi.org/v2/top-headlines?"
    "language=en&pageSize=5&apiKey="
)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 PlanenNews Bot работает!")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - запуск\n"
        "/help - помощь\n"
        "/news - получить последние новости\n"
        "/post ТЕКСТ - опубликовать сообщение"
    )


async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = NEWS_URL + NEWS_API_KEY

    try:
        response = requests.get(url, timeout=15).json()

        if response.get("status") != "ok":
            await update.message.reply_text("❌ Не удалось получить новости.")
            return

        articles = response["articles"][:5]

        text = "📰 Последние новости:\n\n"

        for article in articles:
            text += f"• {article['title']}\n{article['url']}\n\n"

        await update.message.reply_text(text)

    except Exception as e:
        await update.message.reply_text(f"Ошибка: {e}")