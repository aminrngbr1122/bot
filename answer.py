from bot import send_message, send_photo, send_audio, send_video, TOKEN
from subprocess import getoutput

TOKEN = '6049447676:AAHV9ptQikS1ATSAfes2xJmB_aWme3H1bPg'

def yourbotcode(chat_id, text):
    # 
    if text == '/start':
        send_message(chat_id, "Code >")
    else:
        send_message(chat_id, 'Please Wait ...')
        get = getoutput(f'{text}')
        send_message(chat_id, get)
    # 