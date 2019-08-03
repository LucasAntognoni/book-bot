import os
import re
import requests


class Bot(object):

    BOT_URL = 'https://api.telegram.org/bot' + os.environ['BOT_TOKEN'] + '/'

    def __init__(self):
        self.parser = re.compile('^\/(?:(\S+)|)\s?([\s\S]*)$')
        self.last_update_id = 0

    def get_chat_id(self, data):
        return data['message']['chat']['id']

    def get_message(self, data):
        return data['message']['text']

    def get_username(self, data):
        return data['message']['chat']['username']

    def parse_message(self, data):
        parsed_message = self.parser.match(data)
        return parsed_message.group(1), parsed_message.group(2)

    def get_updates(self):
        
        updates_url = self.BOT_URL + 'getUpdates'
        payload = {'offset': self.last_update_id}

        try:
            response = requests.get(updates_url, params=payload)

            if response.status_code == 200:
                return response.json()['result']

        except requests.exceptions.RequestException as e:
            print(e)
            return None

    def positive_response(self, chat, answer):

        f = open("../resources/response.html", "r")
        html = f.read()
        f.close()

        html = html % (answer['title'], answer['authors'], answer['description'], answer['thumbnail'])

        response = {
            "chat_id": chat,
            "text": html,
            "parse_mode": "HTML"
        }

        return response

    def negative_response(self, chat):

        response = {
            "chat_id": chat,
            "text": 'Sorry, i could not find anything!',
        }

        return response

    def send_message(self, payload):
        message_url = self.BOT_URL + 'sendMessage'
        requests.post(message_url, json=payload)
