import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.environ.get("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola! Bot de obras activo ✅\n/estado\n/avance texto\nMandá foto")

async def estado(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📍 Obra Olivos: En progreso ✅")

async def avance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = " ".join(context.args)
    if not texto:
        await update.message.reply_text("Usá: /avance terminamos losa")
        return
    await update.message.reply_text(f"✅ Guardado: {texto}")

async def foto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📸 Foto recibida ✅")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("estado", estado))
app.add_handler(CommandHandler("avance", avance))
app.add_handler(MessageHandler(filters.PHOTO, foto))
app.run_polling()
