from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Replace 'YOUR_TOKEN' with the actual token provided by BotFather
TOKEN = 'YOUR_TOKEN'

# Replace 'ADMIN_IDS' with a list of your admin user IDs
ADMIN_IDS = [123456789, 987654321]

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! This is your bot.')

def request(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    user_message = update.message.text

    # Send the request to admins
    for admin_id in ADMIN_IDS:
        context.bot.send_message(admin_id, f"New request from user {user_id}:\n{user_message}")

    update.message.reply_text('Your request has been sent to the admins.')

def main() -> None:
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("request", request))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
