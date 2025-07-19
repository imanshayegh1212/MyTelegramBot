from flask import Flask
from threading import Thread
import asyncio
import main_bot  # این همون فایل ربات توئه، فرض کنیم اسمش main_bot.py هست

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive!"

def run_flask():
    app.run(host="0.0.0.0", port=8080)

def run_bot():
    asyncio.run(main_bot.main())

if __name__ == '__main__':
    Thread(target=run_flask).start()
    Thread(target=run_bot).start()
