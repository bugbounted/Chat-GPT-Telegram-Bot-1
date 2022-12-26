import openai
import logging
import telegram
from dotenv import load_dotenv
import os


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

load_dotenv()

# Set up OpenAI API client
openai.api_key = os.getenv("OPENAI_APIKEY")

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Function to generate a response using GPT-3
def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

def chat(update, context):
    """Generate a response to the user's message using GPT-3."""
    user_message = update.message.text
    response_prompt = f"User: {user_message}\nBot: "
    response = generate_response(response_prompt)
    update.message.reply_text(response)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(os.getenv("TELEGRAM_BOT_APIKEY"), use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on noncommand i.e message - generate a response using GPT-3
    dp.add_handler(MessageHandler(Filters.text, chat))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
