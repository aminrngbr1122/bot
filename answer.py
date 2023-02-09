# هشدار کتابخانه های زیر به هیچ وجه پاک یا دستکاری نشه !
# کداتو داخل فانکشن yourbotcode بنویس !
# برای اینکه گیج نشی یه کد خودم نوشتم که اگه کاربر استارت کرد رباتو براش پیام سلام بفرسته !

# این فایل پاسخ های ربات هست

from bot import send_message, send_photo, send_audio, send_video, send_message_keyboard

def yourbotcode(chat_id, text, username, name):
    #----------------------------------------------------
    if (text == '/start'):
        send_message(chat_id, f'@{username} \nId: <code>{chat_id}</code> \nFirst: <code>{name}</code>')
    else:
        send_message(chat_id, f'@{username} \nId: <code>{chat_id}</code> \nFirst: <code>{name}</code>')
    #----------------------------------------------------
