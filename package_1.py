from telegram import *
from telegram.ext import *
from functools import wraps
from exam_pkg import *

SELECTION = map(chr, range(1))
SELECT = map(chr, range(1,2))
BAHASA, MAHASISWA, PUBLIK = map(chr, range(2,5))
ASING, LOKAL, KEMBALI_S1 = map(chr, range(5,8))
INGGRIS, ARAB, JEPANG, KOREA, JERMAN, RUSIA, BELANDA, CHINA, THAILAND, MYANMAR, MALAYSIA, INDIA, KEMBALI_B = map(chr, range(8, 21))
KANJI, HIRAGANA, KATAKANA, KEMBALI_BA = map(chr, range(21, 25))
JAWA, SUNDA, MADURA, BETAWI, BUGIS, MINANGKABAU, BANJAR, ACEH, BALI, PALEMBANG, KEMBALI_BL = map(chr, range(25, 36))

KEYBOARD_1 = ReplyKeyboardMarkup([['Mencari'], ['Kembali Halaman Awal']], resize_keyboard=True, one_time_keyboard=True)
KEYBOARD_2 = ReplyKeyboardMarkup([['Berhenti']], resize_keyboard=True, one_time_keyboard=True)

OFFSET = 127462 - ord('A')
def flag(code):
    code = code.upper()
    return chr(ord(code[0]) + OFFSET) + chr(ord(code[1]) + OFFSET)

def send_action(action):
    def decorator(func):
        @wraps(func)
        def command_func(update, context, *args, **kwargs):
            context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=action)
            return func(update, context,  *args, **kwargs)
        return command_func
    return decorator

@send_action(ChatAction.TYPING)
def start(update:Update, context:CallbackContext):
    MyChannel = context.bot.get_chat_member(
        '@cyber_malindo_project', update.effective_user.id)
    if MyChannel.status == 'left' or MyChannel.status == 'kicked':
        update.message.reply_text(
            'Status : {}'.format(MyChannel.status),
            reply_markup=ReplyKeyboardRemove())
        update.message.reply_text(
            'Untuk melanjutkan ke dalam bot anda terlebih dahulu masuk',
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton('Klik disini', url='https://t.me/cyber_malindo_project')]]))
        return start
    else:
        update.message.reply_text(
            'Status : {}'.format(MyChannel.status),
            reply_markup=ReplyKeyboardRemove())
        update.message.reply_text(
            'Selamat datang',
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton('Masuk', callback_data=str(SELECT))]]))
    return SELECTION

def select(update:Update, context:CallbackContext):
    update.callback_query.answer()
    update.callback_query.edit_message_text(
        'Kembali gih',
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton('Relasi Komunikasi Bahasa', callback_data=str(BAHASA))],
             [InlineKeyboardButton('Relasi Perguruan Tinggi', callback_data=str(MAHASISWA))],
             [InlineKeyboardButton('Relasi Universal', callback_data=str(PUBLIK))]]))
    return SELECTION

def bahasa(update:Update, context:CallbackContext):
    update.callback_query.answer()
    update.callback_query.edit_message_text(
        'Pilih',
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton('Bahasa Asing', callback_data=str(ASING)),
              InlineKeyboardButton('Bahasa Lokal', callback_data=str(LOKAL))],
             [InlineKeyboardButton('Kembali', callback_data=str(KEMBALI_S1))]]))
    return SELECTION

def asing(update:Update, context:CallbackContext):
    update.callback_query.answer()
    update.callback_query.edit_message_text(
        'Pooooo jjbxjbxjsvcjsachvhsc schvsajhcvsjavcjsac scvhahjsvcjasvcja sjavcjsvcj',
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton('Inggris {}'.format(flag('GB')), callback_data=str(INGGRIS)),
              InlineKeyboardButton('Arab {}'.format(flag('SA')), callback_data=str(ARAB)),
              InlineKeyboardButton('Jepang {}'.format(flag('JP')), callback_data=str(JEPANG))],
             [InlineKeyboardButton('Korea {}'.format(flag('KR')), callback_data=str(KOREA)),
              InlineKeyboardButton('Jerman {}'.format(flag('DE')), callback_data=str(JERMAN)),
              InlineKeyboardButton('Rusia {}'.format(flag('RU')), callback_data=str(RUSIA))],
             [InlineKeyboardButton('Belanda {}'.format(flag('NL')), callback_data=str(BELANDA)),
              InlineKeyboardButton('China {}'.format(flag('CN')), callback_data=str(CHINA)),
              InlineKeyboardButton('Thailand {}'.format(flag('TH')), callback_data=str(THAILAND))],
             [InlineKeyboardButton('Myanmar {}'.format(flag('MM')), callback_data=str(MYANMAR)),
              InlineKeyboardButton('Malaysia {}'.format(flag('MY')), callback_data=str(MALAYSIA)),
              InlineKeyboardButton('India {}'.format(flag('IN')), callback_data=str(INDIA))],
             [InlineKeyboardButton('Kembali', callback_data=str(KEMBALI_B))]]))
    return SELECTION

def jepang(update:Update, context:CallbackContext):
    update.callback_query.answer()
    update.callback_query.edit_message_text(
        'pilih salah satu',
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton('Kanji', callback_data=str(KANJI)),
              InlineKeyboardButton('Hiragana', callback_data=str(HIRAGANA)),
              InlineKeyboardButton('Katagana', callback_data=str(KATAKANA))],
             [InlineKeyboardButton('Kembali', callback_data=str(KEMBALI_BA))]]))
    return SELECTION

def lokal(update:Update, context:CallbackContext):
    update.callback_query.answer()
    update.callback_query.edit_message_text(
        'pilih bahahahahahaha',
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton('Jawa', callback_data=str(JAWA)),
              InlineKeyboardButton('Sunda', callback_data=str(SUNDA))],
             [InlineKeyboardButton('Madura', callback_data=str(MADURA)),
              InlineKeyboardButton('Betawi', callback_data=str(BETAWI))],
             [InlineKeyboardButton('Bugis', callback_data=str(BUGIS)),
              InlineKeyboardButton('Minangkabau', callback_data=str(MINANGKABAU))],
             [InlineKeyboardButton('Banjar', callback_data=str(BANJAR)),
              InlineKeyboardButton('Aceh', callback_data=str(ACEH))],
             [InlineKeyboardButton('Bali', callback_data=str(BALI)),
              InlineKeyboardButton('Palembang', callback_data=str(PALEMBANG))],
             [InlineKeyboardButton('Kembali', callback_data=str(KEMBALI_BL))]]))
    return SELECTION

# BAHASA INGGRIS
def inggris_pkg(update:Update, context:CallbackContext):
    update.callback_query.answer()
    update.callback_query.bot.send_photo(
        update.effective_chat.id,
        photo='https://drive.google.com/file/d/1Up6HHFXeiqcz_tI5qTsp7u_FzIY3wcSc/view?usp=sharing',
        caption='INGGGGGGGGGGRIIIIISSSSS',
        reply_markup=KEYBOARD_1)
    return INGGRIS_PKG

def stop(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text='untuk memulai ulang /start')
    return ConversationHandler.END