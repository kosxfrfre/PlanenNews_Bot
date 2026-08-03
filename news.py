import feedparser
import asyncio
from telegram import Bot

BOT_TOKEN = "8678805338:AAHPumjkRMOvkd81aPJ_H7kjiVJWi18V3Ac"
CHANNEL_ID = "@PlanenNews"

RSS_FEEDS = [
    "https://lenta.ru/rss",
    "https://ria.ru/export/rss2/index.xml",
    "https://rss.cnn.com/rss/edition.rss"
]

sent_links = set()

bot = Bot(token=BOT_TOKEN)