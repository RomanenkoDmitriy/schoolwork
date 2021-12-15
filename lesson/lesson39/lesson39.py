import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

token = os.environ.get('TELEGRAM_BOT')
print(token)

updater = Updater(token)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello!')

def hellp(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='What?!')

def greeat(update, context):
    name = ' '.join(context.args)
    update.message.reply_text(f'Hello {name}!')

def some(update, context):
    sum_args = sum(map(int, context.args))
    update.message.reply_text(f'{sum_args}!')

def main():
    start_hendler = CommandHandler('start', start)
    hellp_handler = CommandHandler('hellp', hellp)
    some_hendler = CommandHandler('some', some)
    updater.dispatcher.add_hendler(start_hendler)
    updater.dispatcher.add_hendler(hellp_handler)
    updater.dispatcher.add_hendler(some_hendler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()