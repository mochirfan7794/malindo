from telegram import *
from telegram.ext import *
from package_1 import *
import os
import sys
from threading import Thread
from exam_pkg import *

def main():
    updater = Updater(token='1708137883:AAEisJWKr-xRygtm3GC9zq9oDDTq_P3215E', use_context=True)
    dp = updater.dispatcher

    def stop_and_restart():
        updater.stop()
        os.execl(sys.executable, sys.executable, *sys.argv)
    
    def restart(update:Update, context:CallbackContext):
        update.message.reply_text('Bot is restartting...')
        # context.bot.send_message(, 'asjkcbashjcbjhsabcjhsac')
        Thread(target=stop_and_restart).start()

    dp.add_handler(CommandHandler('r', restart, filters=Filters.user(username='@malindo_fanmoch')))

    dp.add_handler(
        ConversationHandler(
            entry_points=[CommandHandler('start', start)],
            states={
                SELECTION:[CallbackQueryHandler(select, pattern=str(SELECT)),
                           
                           CallbackQueryHandler(bahasa, pattern=str(BAHASA)),
                           CallbackQueryHandler(select, pattern=str(KEMBALI_S1)),
                           
                           CallbackQueryHandler(asing, pattern=str(ASING)),
                           CallbackQueryHandler(bahasa, pattern=str(KEMBALI_B)),
                           
                           CallbackQueryHandler(jepang, pattern=str(JEPANG)),
                           CallbackQueryHandler(asing, pattern=str(KEMBALI_BA)),
                           
                           CallbackQueryHandler(lokal, pattern=str(LOKAL)),
                           CallbackQueryHandler(bahasa, pattern=str(KEMBALI_BL)),
                           
                           CallbackQueryHandler(inggris_pkg, pattern=str(INGGRIS))],
                INGGRIS_PKG:[MessageHandler(Filters.command | Filters.regex('Mencari'), find_002),
                             MessageHandler(Filters.command | Filters.regex('Berhenti'), disconnect_002),
                             MessageHandler(Filters.command | Filters.regex('Kembali Halaman Awal'), start),
                             MessageHandler(Filters.text, kirim_pesan_text_002),
                             MessageHandler(Filters.sticker, kirim_pesan_sticker_002),
                             MessageHandler(Filters.voice, kirim_pesan_voice_002)]},
            fallbacks=[CommandHandler('stop', stop)]))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()