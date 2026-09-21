import os
from flask import Flask
import threading
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola! Bot de obras activo")

async def estado(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📍 Obra Olivos: en curso")

async def avance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = " ".join(context.args)
    await update.message.reply_text(f"✅ Guardado: {texto}")

async def foto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📸 Foto recibida!")

# --- Truco para Render Gratis ---
app_web = Flask(__name__)
@app_web.route('/')
def home():
    return "Bot Obras vivo!"
def run_web():
    app_web.run(host='0.0.0.0', port=10000)
threading.Thread(target=run_web, daemon=True).start()
# --- Fin truco ---

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("estado", estado))
app.add_handler(CommandHandler("avance", avance))
app.add_handler(MessageHandler(filters.PHOTO, foto))
app.run_polling()
