from bot import send_message, send_photo, send_audio, send_video
import re


def is_link(text):
    # Regular expression pattern to match a URL
    url_pattern = re.compile(
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

    # Use the `re.search` method to check if the text matches the URL pattern
    return bool(re.search(url_pattern, text))


def yourbotcode(chat_id, text):
    #
    if is_link(text):
        send_video(chat_id, text)
    else:
        pass
    #
