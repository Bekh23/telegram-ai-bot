from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "SIZNING_BOT_TOKEN"

AI_STYLES = """
🎨 *AI Style’lar ro‘yxati:*

1. Ghibli — sehrli animatsion uslub
2. Disney — yumshoq va yorqin personajlar
3. Pixar — 3D jonlantirilgan film ko‘rinishida
4. Cyberpunk — neon, qorong‘i shahar va texno effektlar
5. Realism — haqiqiy fotografiyaga yaqin
6. Van Gogh — mashhur rassom uslubida fırçali tekstura
7. Anime — yaponcha animatsiya uslubi
8. Steampunk — mexanik, eski davr texnologiyalari bilan uyg‘un
9. Watercolor — akvarel bo‘yog‘i uslubida yumshoq ranglar
10. Ukiyo-e — klassik yapon rasm uslubi
11. Sketch — qo‘lda chizilgan qoralama ko‘rinish
12. Futuristic — kelajak tasviridagi zamonaviy vizual
13. Dreamcore — orzudek surreal effektlar
14. Lego Style — Lego kublaridan yaratilgan ko‘rinish
15. Comic Book — komiks ko‘rinishida, qalin konturlar bilan
16. Oil Painting — moybo‘yoqli rassomlik uslubi
17. 3D Cartoon — hajmli va yumshoq multfilm personajlari
18. Synthwave — 80-yillar musiqasi va vizual effektlari asosida
19. Pop Art — rangli, kontrastli san’at uslubi
20. Isometric 3D — yuqoridan 3D burchakli chizmalar

🔥 Yana AI g‘oyalar uchun bizni kuzatib boring!
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args and context.args[0] == "style":
        await update.message.reply_text(AI_STYLES, parse_mode="Markdown")
    else:
        await update.message.reply_text("👋 Salom! Botga hush kelibsiz!")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()