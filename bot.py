import os
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Загружаем переменные окружения из файла .env
load_dotenv()

# Получаем токен из переменных окружения
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("Биржи"), KeyboardButton("Спред")],
        [KeyboardButton("Черный список")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)
    await update.message.reply_text('Пожалуйста, выберите программу:', reply_markup=reply_markup)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == 'Биржи':
        await update.message.reply_text('Запущена программа 1!')
        # Здесь можно добавить ваш код для запуска программы 1
    elif text == 'Спред':
        await update.message.reply_text('Запущена программа 2!')
        # Здесь можно добавить ваш код для запуска программы 2
    elif text == 'Черный список':
        await update.message.reply_text('Запущена программа 3!')
        # Здесь можно добавить ваш код для запуска программы 3

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    application.run_polling()

if __name__ == '__main__':
    main()
