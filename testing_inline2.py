from telegram import *
from telegram.ext import *
from ConfigId import token
from functools import wraps

PERALIHAN = map(chr, range(1))
PILIHAN_1, PILIHAN_2 = map(chr, range(1,3))
MY_KEYBOARD_1 = map(chr, range(1))

KEYBOARD_1 = ReplyKeyboardMarkup([['BACOT']], resize_keyboard=True, one_time_keyboard=True)

def Subscribe(func):
    @wraps(func)
    def langganan_channel(update:Update, context:CallbackContext):
        JoinChannel = context.bot.get_chat_member(
            '@cyber_malindo_project', update.effective_user.id)
        if JoinChannel.status == 'left' or JoinChannel.status == 'kicked':
            update.message.reply_text('Masuk dulu coeg')
        else:
            pass
        return func(update, context)
    return langganan_channel

@Subscribe
def start(update:Update, context:CallbackContext):
    update.message.reply_text(
        'selamat datang *[{}](http://t.me/{})*\.'.format(update.effective_user.id, update.effective_user.language_code),
        ParseMode.MARKDOWN_V2,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(
                'JOIN', 
                url='https://t.me/cyber_malindo_project')],
             [InlineKeyboardButton(
                 'LANJUT',
                 callback_data=str(PILIHAN_1))]]))
    return PERALIHAN

def pilihan_1(update:Update, context:CallbackContext):
    JoinChannel = context.bot.get_chat_member(
        '@cyber_malindo_project', update.effective_user.id)
    print(JoinChannel.status)
    if JoinChannel.status == 'left' or JoinChannel.status == 'kicked':
        update.callback_query.answer()
        update.callback_query.edit_message_text(
            'Join Asu')
    else:
        update.callback_query.answer()
        update.callback_query.edit_message_text(
            'PILIHAN 1',
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(
                    'PILIHAN 2', 
                    callback_data=str(PILIHAN_2))]]))
    return PERALIHAN

def pilihan_2(update:Update, context:CallbackContext):
    update.callback_query.answer()
    update.callback_query.bot.send_message(
        update.effective_user.id,
        'bacot',
        reply_markup=KEYBOARD_1)
    return MY_KEYBOARD_1

def stop(update:Update, context:CallbackContext):
    update.message.reply_text(
        'Bot _telah_ *berhenti* [Channel Telegram](http://t.me/cyber_malindo_project)\.',
        ParseMode.MARKDOWN_V2,
        reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

def main():
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('start', start)],
        states={
            PERALIHAN:[
                CallbackQueryHandler(pilihan_1, pattern=str(PILIHAN_1)),
                CallbackQueryHandler(pilihan_2, pattern=str(PILIHAN_2))],
            MY_KEYBOARD_1:[
                MessageHandler(Filters.command | Filters.regex('BACOT'), start)]
                },
        fallbacks=[
            CommandHandler('stop', stop)]))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()