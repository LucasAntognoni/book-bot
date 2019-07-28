from flask import Flask, request
from books import Books
from bot import Bot

app = Flask(__name__)
books = Books()
bot = Bot()


@app.route('/', methods=['POST'])
def main():

    data = request.get_json()
    message = bot.get_message(data)
    command, text = bot.parse_message(message)
    result = books.search(command, text)

    if result:
        response = bot.prepare_response(bot.get_chat_id(data), result)
        bot.send_message(response)
    else:
        response = bot.prepare_response(bot.get_chat_id(data), 'Could not find any book.')
        bot.send_message(response)

    return 'OK', 200


if __name__ == '__main__':
    app.run()
