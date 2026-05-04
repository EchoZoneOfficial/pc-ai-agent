import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

def is_admin(user_id):
    return user_id == ADMIN_ID

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if user_id != ADMIN_ID:
        await update.message.reply_text("Нет доступа")
        return

    text = update.message.text.lower()

    # просто тестовые команды
    if text == "ping":
        await update.message.reply_text("pong")
        return

    if text == "hello":
        await update.message.reply_text("бот работает")
        return

    await update.message.reply_text(f"получено: {text}")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handle))

app.run_polling()
