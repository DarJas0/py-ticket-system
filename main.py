import os
import logging
import sys
from typing import Final
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

API_TOKEN: Final = os.getenv('TELEGRAM_TOKEN')


async def initiate_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles the /start command."""
    await update.message.reply_text('Greetings! I am your pingpong bot. Say "ping" if you want a "pong".')


def generate_response(user_input: str) -> str:
    """Processes user text and generates a response."""
    normalized_input: str = user_input.lower()

    if 'ping' in normalized_input:
        return 'pong!'

    return 'Wanna play ping pong or not?'


async def process_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Processes incoming text messages."""
    text: str = update.message.text

    logger.info(f'User ({update.message.chat.id}) sent: "{text}"')

    # Get response and reply to user
    response: str = generate_response(text)

    logger.info(f'Bot response: {response}')
    await update.message.reply_text(response)


async def log_error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Logs exceptions."""
    logger.error(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    logger.info('Starting bot application...')

    if not API_TOKEN:
        logger.error("TELEGRAM_TOKEN is missing. Shutting down.")
        sys.exit(1)

    app = Application.builder().token(API_TOKEN).build()

    # Register handlers
    app.add_handler(CommandHandler('start', initiate_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process_message))
    app.add_error_handler(log_error)

    logger.info('Polling started.')
    app.run_polling(poll_interval=2)