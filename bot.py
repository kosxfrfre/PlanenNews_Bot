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