import os
import logging
import sys
from typing import Final, Dict, Any
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

# --- IN-MEMORY DATABASE ---
ticket_db: Dict[int, Dict[str, Any]] = {}
ticket_counter: int = 1

async def initiate_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles the /start command."""
    await update.message.reply_text('Greetings! I am your pingpong bot. Say "ping" if you want a "pong".')

async def create_ticket(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles the /ticket command."""
    global ticket_counter

    if not context.args:
        await update.message.reply_text(
            "Please describe your issue! \nExample: /ticket My printer is burning"
        )
        return

    problem_description: str = " ".join(context.args)
    user_id: int = update.message.from_user.id

    ticket_id: int = ticket_counter
    ticket_db[ticket_id] = {
        "user_id" : user_id,
        "problem_description" : problem_description,
        "status" : "open"
    }
    ticket_counter += 1

    logger.info(f"New ticket #{ticket_id} created by user {user_id}")
    await update.message.reply_text(f"✅ Ticket #{ticket_id} has been created!\n\nDescription: {problem_description}")

async def show_tickets(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles the /tickets command."""
    if not ticket_db:
        await update.message.reply_text(
            "No tickets open currently!"
        )
        return

    response: str = "These are the tickets:\n\n"
    for ticket_id, data in ticket_db.items():
        response += f"{ticket_id}: {data['problem_description']}\n"

    await update.message.reply_text(response)

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
    app.add_handler(CommandHandler('ticket', create_ticket))
    app.add_handler(CommandHandler('tickets', show_tickets))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process_message))
    app.add_error_handler(log_error)

    logger.info('Polling started.')
    app.run_polling(poll_interval=2)