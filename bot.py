from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import os

TOKEN = os.getenv("TOKEN")  # Токен читается из переменных окружения

async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.video:
        user_id = update.message.from_user.id
        file = await context.bot.get_file(update.message.video.file_id)

        # Создание папки videos, если её нет
        os.makedirs("videos", exist_ok=True)
        path = f"videos/video_{user_id}_{update.message.video.file_unique_id}.mp4"
        await file.download_to_drive(path)

        await update.message.reply_text("✅ Видео получено и сохранено!")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.VIDEO, handle_video))

print("Бот запущен...")
app.run_polling()
