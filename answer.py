from bot import send_message, send_photo

def yourbotcode(chat_id, text):
    # 
    if text == '/start':
        send_message(chat_id, 'Hello World (:')
    else:
        send_message(chat_id, 'I do not understand what you say ?')
    # 