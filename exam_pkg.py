import random
from telegram import *
from telegram.ext import *
from collections import defaultdict
from functools import wraps
# from time import sleep
INGGRIS_PKG = map(chr, range(1))
users = defaultdict(dict)
list_user_1 = []

KEYBOARD_1 = ReplyKeyboardMarkup([['Mencari'], ['Kembali Halaman Awal']], resize_keyboard=True, one_time_keyboard=True)
KEYBOARD_2 = ReplyKeyboardMarkup([['Berhenti']], resize_keyboard=True, one_time_keyboard=True)

def scan(current):
    for key, value in users.items():
        if key != current and value.get('status') == 'free':
            return key
    return None

def connect(user, interlocutor):
    users[user]['status'] = 'busy'
    users[user]['interlocutor'] = interlocutor
    users[interlocutor]['status'] = 'busy'
    users[interlocutor]['interlocutor'] = user
    
def find_002(update: Update, context: CallbackContext) -> None:
    context.bot.delete_message(
        update.message.from_user.id, 
        message_id=update.message.message_id)
    user = update.message.from_user.id
    context.bot.send_message(
        user, 
        'Mencari...',
        reply_markup=KEYBOARD_2)
    interlocutor = users[user].get('interlocutor')
    if interlocutor:
        context.bot.send_message(
            interlocutor, 
            'Telah berhenti', 
            reply_markup=KEYBOARD_1)
        users[interlocutor]['interlocutor'] = None
        users[user]['interlocutor'] = None
    interlocutor = scan(user)
    if interlocutor:
        connect(user, interlocutor)
        context.bot.send_message(
            user, 
            'Sukses Konek {}'.format(interlocutor))
        context.bot.send_message(interlocutor, text='Sukses Konek {}'.format(user))
    else:
        users[user]['status'] = 'free'
    return INGGRIS_PKG

def disconnect_002(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user.id
    context.bot.send_message(
        user, 
        'Telah berhenti', 
        reply_markup=KEYBOARD_1)
    context.bot.delete_message(
        update.message.from_user.id, 
        message_id=update.message.message_id)
    users[user]['status'] = 'busy'
    interlocutor = users[user].get('interlocutor')
    if interlocutor:
        context.bot.send_message(
            interlocutor, 
            'Telah berhenti',  
            reply_markup=KEYBOARD_1)
        users[interlocutor]['interlocutor'] = None
        users[user]['interlocutor'] = None
    return INGGRIS_PKG




def send_action(action):
    def decorator(func):
        @wraps(func)
        def command_func(update:Update, context:CallbackContext, *args, **kwargs):
            user = update.effective_chat.id
            interlocutor = users[user].get('interlocutor')
            context.bot.send_chat_action(chat_id=interlocutor, action=action)
            return func(update, context,  *args, **kwargs)
        return command_func
    return decorator

# @send_action(ChatAction.TYPING)
def kirim_pesan_text_002(update: Update, context: CallbackContext) -> None:
    user = update.effective_chat.id
    interlocutor = users[user].get('interlocutor')
    if not interlocutor:
        update.message.reply_chat_action(action=ChatAction.TYPING)
        context.bot.send_message(
            user, 
            'Kamu harus mencari dulu /find')
    else:
        context.bot.send_chat_action(
            interlocutor,
            ChatAction.TYPING
        )
        context.bot.send_message(
            interlocutor, 
            update.message.text)
    return INGGRIS_PKG

@send_action(ChatAction.TYPING)
def kirim_pesan_sticker_002(update: Update, context: CallbackContext) -> None:
    user = update.effective_chat.id
    interlocutor = users[user].get('interlocutor')
    if not interlocutor:
        update.message.reply_chat_action(action=ChatAction.TYPING)
        context.bot.send_message(
            user, 
            'Kamu harus mencari dulu /find')
    else:
        context.bot.send_sticker(
            interlocutor, 
            update.message.sticker.file_id)
    return INGGRIS_PKG

@send_action(ChatAction.RECORD_AUDIO)
@send_action(ChatAction.UPLOAD_AUDIO)
def kirim_pesan_voice_002(update: Update, context: CallbackContext) -> None:
    user = update.effective_chat.id
    interlocutor = users[user].get('interlocutor')
    if not interlocutor:
        context.bot.send_message(
            user, 
            text='Kamu harus mencari dulu /find')
    else:
        context.bot.send_voice(
            interlocutor, 
            update.message.voice.file_id)
    return INGGRIS_PKG