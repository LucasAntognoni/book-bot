import os
import re

class Bot(object):

    BOT_URL = 'https://api.telegram.org/bot' + os.environ['BOT_TOKEN'] + '/'

    def __init__(self):
        self.parser = re.compile('^\/(?:(\S+)|)\s?([\s\S]*)$')

    def get_chat_id(self, data):
        return data['message']['chat']['id']

    def get_message(self, data):
        return data['message']['text']

    def get_username(self, data):
        return  data['message']['chat']['username']

    def send_message(self, data):
        message_url = self.BOT_URL + 'sendMessage'
        requests.post(message_url, json=data)

    def parse_message(self, data):
        parsed_message = self.parser.match(data)
        return parsed_message.group(1), parsed_message.group(2)
        
    def prepare_response(self, chat, message):
        pass
