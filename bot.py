import os
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

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
        await update.message.reply_text('Выберите действие:', reply_markup=exchange_keyboard())
    elif text == 'Спред':
        await update.message.reply_text('Запущена программа 2!')
        # Здесь можно добавить ваш код для запуска программы 2
    elif text == 'Черный список':
        await update.message.reply_text('Запущена программа 3!')
        # Здесь можно добавить ваш код для запуска программы 3

def exchange_keyboard():
    keyboard = [
        [InlineKeyboardButton("BytMart Buy", callback_data='BytMart Buy'), InlineKeyboardButton("BytMart Sell", callback_data='BytMart Sell')],
        [InlineKeyboardButton("Mexc Buy", callback_data='Mexc Buy'), InlineKeyboardButton("Mexc Sell", callback_data='Mexc Sell')]
    ]
    return InlineKeyboardMarkup(keyboard)

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    selected_action = query.data

    # Обновление кнопок с галочкой
    keyboard = [
        [InlineKeyboardButton("BytMart Buy " + ("✅" if selected_action == "BytMart Buy" else ""), callback_data='BytMart Buy'),
         InlineKeyboardButton("BytMart Sell " + ("✅" if selected_action == "BytMart Sell" else ""), callback_data='BytMart Sell')],
        [InlineKeyboardButton("Mexc Buy " + ("✅" if selected_action == "Mexc Buy" else ""), callback_data='Mexc Buy'),
         InlineKeyboardButton("Mexc Sell " + ("✅" if selected_action == "Mexc Sell" else ""), callback_data='Mexc Sell')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(f'Вы выбрали: {selected_action}', reply_markup=reply_markup)

def main():
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    application.add_handler(CallbackQueryHandler(handle_callback, pattern='^(BytMart Buy|BytMart Sell|Mexc Buy|Mexc Sell)$'))

    application.run_polling()

if __name__ == '__main__':
    main()
