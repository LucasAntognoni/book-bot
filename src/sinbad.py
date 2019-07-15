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
    
    # response = books.process_search(command, result)
    
    return 'ok'

if __name__ == '__main__':
    app.run()
