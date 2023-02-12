# هشدار کتابخانه های زیر به هیچ وجه پاک یا دستکاری نشه !
# کداتو داخل فانکشن yourbotcode بنویس !
# برای اینکه گیج نشی یه کد خودم نوشتم که اگه کاربر استارت کرد رباتو براش پیام سلام بفرسته !

# این فایل پاسخ های ربات هست

from bot import send_message, send_photo, send_audio, send_video

def yourbotcode(chat_id, text):
    #
    if ( text == '/start' ) :
        send_message(chat_id, 'Welcome to pybot (:')
    else:
    	send_message(chat_id, '/start')
    #
