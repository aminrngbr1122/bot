# هشدار کتابخانه های زیر به هیچ وجه پاک یا دستکاری نشه !
# کداتو داخل فانکشن yourbotcode بنویس !
# برای اینکه گیج نشی یه کد خودم نوشتم که اگه کاربر استارت کرد رباتو براش پیام سلام بفرسته !

# این فایل پاسخ های ربات هست

from bot import send_message, send_photo, send_audio, send_video

import requests

from bs4 import BeautifulSoup

def yourbotcode(chat_id, text):
    #
    if ( text == '/start' ) :
    	url = 'http://sexporn.pics'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        img_tags = soup.find_all('img')
        urls = [img['src'] for img in img_tags]
        for i, url in enumerate(urls):
          try:
            send_photo(chat_id, url)
          except:
            pass
    else:
    	send_message(chat_id, '/start')
    #
