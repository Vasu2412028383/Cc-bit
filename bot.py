# bot.py
from telegram import Update, BotCommand
from telegram.ext import Application, CommandHandler, ContextTypes
import random
from config import TOKEN

def generate_cc(bin_number):
    cc_number = bin_number + ''.join(str(random.randint(0, 9)) for _ in range(10))
    expiry_month = str(random.randint(1, 12)).zfill(2)
    expiry_year = str(random.randint(24, 30))
    cvv = str(random.randint(100, 999))
    return f"CC: {cc_number}\nEXP: {expiry_month}/{expiry_year}\nCVV: {cvv}"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to CC Generator Bot! Use /ccgen <BIN>")

async def ccgen(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /ccgen <BIN>")
        return
    
    bin_number = context.args[0]
    if len(bin_number) != 6 or not bin_number.isdigit():
        await update.message.reply_text("Invalid BIN. Provide a 6-digit number.")
        return
    
    cc_details = generate_cc(bin_number)
    await update.message.reply_text(cc_details)

async def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ccgen", ccgen))
    
    app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
