import json
import sys
import requests
import answer

TOKEN = "6049447676:AAHV9ptQikS1ATSAfes2xJmB_aWme3H1bPg"

BASE_URL = "https://api.telegram.org/bot{}/".format(TOKEN)

code = requests.get(BASE_URL)

if code == 200:
    pass
else:
    sys.exit()
    

def get_updates(offset=None):
    url = BASE_URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    response = requests.get(urboyl)
    return json.loads(response.content.decode("utf8"))

def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


# Bot Function
# ============================================

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