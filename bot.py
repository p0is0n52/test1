import logging
import os
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Токен из переменных окружения
BOT_TOKEN = os.getenv('8364983433:AAGM4A4_lmswx6M0Uz_0zw6cW3P5X4hesng')

def create_main_keyboard():
    keyboard = [
        [KeyboardButton("📸 Картинка 1"), KeyboardButton("📸 Картинка 2")],
        [KeyboardButton("📝 Текст 1"), KeyboardButton("📝 Текст 2")],
        [KeyboardButton("ℹ️ Информация"), KeyboardButton("🎉 Сюрприз")]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = create_main_keyboard()
    await update.message.reply_text(
        "Привет! Выбери одну из кнопок:",
        reply_markup=keyboard
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    
    if text == "📸 Картинка 1":
        await update.message.reply_photo(
            photo="https://via.placeholder.com/400x200/FF0000/FFFFFF?text=Картинка+1",
            caption="Вот первая картинка! 🖼️"
        )
    
    elif text == "📸 Картинка 2":
        await update.message.reply_photo(
            photo="https://via.placeholder.com/400x200/0000FF/FFFFFF?text=Картинка+2",
            caption="А вот вторая картинка! 📸"
        )
    
    elif text == "📝 Текст 1":
        await update.message.reply_text("Это первый текст! ✨")
    
    elif text == "📝 Текст 2":
        await update.message.reply_text("Это второй текст! 📚")
    
    elif text == "ℹ️ Информация":
        await update.message.reply_text("ℹ️ Информация о боте")
    
    elif text == "🎉 Сюрприз":
        await update.message.reply_text("🎉 Сюрприз! 🎉")
    
    else:
        await update.message.reply_text(
            "Используйте кнопки ниже 👇",
            reply_markup=create_main_keyboard()
        )

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.error(f"Ошибка: {context.error}")

def main():
    if BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
        print("⚠️ Замените BOT_TOKEN на реальный токен!")
        return
    
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_error_handler(error_handler)
    
    print("Бот запущен...")
    application.run_polling()

if __name__ == "__main__":
    main()
