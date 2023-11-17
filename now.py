import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the /now command handler
def now(update: Update, context: CallbackContext) -> None:
    # Get the current date and time
    current_time = update.message.date.strftime("%Y-%m-%d %H:%M:%S")

    # Respond to the user with the current date and time
    update.message.reply_text(f"The current date and time is: {current_time}")

def main() -> None:
    # Set up the Telegram Bot with your token
    updater = Updater("")

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
