import logging
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Your bot token obtained from BotFather
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

# Define the /now command handler
def now(update: Update, context: CallbackContext) -> None:
    current_time = update.message.date.strftime("%Y-%m-%d %H:%M:%S")
    update.message.reply_text(f"The current date and time is: {current_time}")

def main() -> None:
    # Create the Updater and pass it your bot's token
    updater = Updater(6321549495:AAE-shnQcCl5_MwBqfj9_2LvQIu3z_kbqaM)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register the /now command handler
    dp.add_handler(CommandHandler("now", now))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop it
    updater.idle()

if __name__ == '__main__':
    main()

