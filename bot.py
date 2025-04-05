from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7904549978:AAE0qzaUAYjEU7zlgwsOyteHIOI5is-Deik"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args and context.args[0] == "style":
        await update.message.reply_text("📥 Siz so‘ragan AI Style ro‘yxati tayyor! Quyidagi faylni yuklab oling:")
        
        with open("ai_styles.pdf", "rb") as file:
            await update.message.reply_document(file, caption="📘 AI Style ro‘yxati (PDF)")
    else:
        await update.message.reply_text("👋 Salom! Botga hush kelibsiz!")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
