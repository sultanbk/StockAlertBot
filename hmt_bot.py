import requests
from bs4 import BeautifulSoup
import time
import telegram
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

PRODUCT_URL = "https://hmtwatches.in/product_details?id=..."

def check_stock():
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(PRODUCT_URL, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    cart_button = soup.find("button", class_="btn btn-block btn-cart")

    if cart_button:
        bot = telegram.Bot(token=BOT_TOKEN)
        bot.send_message(chat_id=CHAT_ID, text=f"🚨 HMT Watch is IN STOCK!\n👉 {PRODUCT_URL}")
        print("✅ In stock!")
        return True

    print("❌ Still out of stock.")
    return False

# Run every hour
while True:
    try:
        if check_stock():
            break
    except Exception as e:
        print("Error:", e)
    time.sleep(3600)