import asyncio
import time
import requests
from telegram import Bot

TOKEN = "7848693387:AAFCzfHbp6KFPeWMhT7shP0o08l4Snak_SM"
CHAT_ID = "6743824205"

bot = Bot(token=TOKEN)

# Здесь будет твоя логика проверки сайта МВД Словакии
def check_for_terms():
    # Пример: отправляем GET-запрос (замени на нужную логику)
    response = requests.get("https://portal.minv.sk/wps/portal/domov/ecu/ecu_elektronicke_sluzby/ecu-vysys")
    return "Žiadosť" in response.text  # пример простой проверки

async def monitor():
    while True:
        try:
            if check_for_terms():
                await bot.send_message(chat_id=CHAT_ID, text="🔔 Objavili sa nové termíny! Skontrolujte portál.")
        except Exception as e:
            print("Ошибка при проверке:", e)
        await asyncio.sleep(60)  # ждать 60 секунд

if __name__ == "__main__":
    asyncio.run(monitor())
