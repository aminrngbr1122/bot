# این فایل پل ارتباطی ما با تلگرام هست

# توکن جایگزین کن توی TOKEN
# وارد فایل answer.py بشو و کداتو بنویس
#بعد فایل bot.py که همین فایل هست اجرا کن

import json
import sys
import requests
import answer

TOKEN = input('t :')

if True:

    BASE_URL = "https://api.telegram.org/bot{0}/".format(TOKEN)

    def get_updates(offset=None):
        url = BASE_URL + "getUpdates"
        if offset:
            url += "?offset={}".format(offset)
        response = requests.get(url)
        return json.loads(response.content.decode("utf8"))

    def get_last_update_id(updates):
        update_ids = []
        for update in updates["result"]:
            update_ids.append(int(update["update_id"]))
        return max(update_ids)

    # Bot Function
    # ============================================

    def send_message_keyboard(chat_id, text, keyboard = []):
        url = BASE_URL + "sendMessage"
        data = {"chat_id": chat_id, "text": text, 'reply_markup':{'keyboard':{keyboard}, 'resize_keyboard':'true'}}
        response = requests.post(url, data=data)
        return json.loads(response.content.decode("utf8"))
        
    def send_message(chat_id, text):
        url = BASE_URL + "sendMessage"
        data = {"chat_id": chat_id, "text": text}
        response = requests.post(url, data=data)
        return json.loads(response.content.decode("utf8"))

    def send_photo(chat_id, url):
        url = BASE_URL + "sendphoto"
        data = {"chat_id": chat_id, "photo": url}
        response = requests.post(url, data=data)
        return json.loads(response.content.decode("utf8"))

    def send_video(chat_id, url):
        url = BASE_URL + "sendvideo"
        data = {"chat_id": chat_id, "video": url}
        response = requests.post(url, data=data)
        return json.loads(response.content.decode("utf8"))

    def send_audio(chat_id, url):
        url = BASE_URL + "sendaudio"
        data = {"chat_id": chat_id, "audio": url}
        response = requests.post(url, data=data)
        return json.loads(response.content.decode("utf8"))

    # =============================================
    # End Bot Function

    def handle_updates(updates):
        for update in updates["result"]:
            text = update["message"]["text"]
            chat_id = update["message"]["chat"]["id"]
            answer.yourbotcode(chat_id, text)

    def main():
        last_update_id = None
        while True:
            updates = get_updates(last_update_id)
            if len(updates["result"]) > 0:
                last_update_id = get_last_update_id(updates) + 1
                handle_updates(updates)

    if __name__ == '__main__':
        main()

else:

    sys.exit()
