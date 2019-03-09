from telegram.ext import Updater, CommandHandler
from telegram import Bot, Update
from telegram import ParseMode

def start (bot, update):
	update.message.reply_text(""" Hi {} i\'m @Giveme_id_bot 😉
Click /id to know your telegram user id.
Add me to a group and use /id to know the group's id. """ .format(update.message.from_user.first_name))
	
def about (bot, update):
	update.message.reply_text("A bot by @Jinszz")

def id (bot, update):
	update.message.reply_text("`{}` is your chat id 🙇 " .format(update.message.chat_id),
	parse_mode = ParseMode. MARKDOWN)
	
updater = Updater('778968419:AAFxHJBndpWf8WaJPHzLRqfOqqXq4n_s33Y')

updater.dispatcher.add_handler(CommandHandler('start' , start))
updater.dispatcher.add_handler(CommandHandler('id', id))
updater.dispatcher.add_handler(CommandHandler('about', about))

updater.start_polling()
updater.idle()
