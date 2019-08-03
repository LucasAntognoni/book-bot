from books import Books
from bot import Bot

books = Books()
bot = Bot()


def main():

    while(True):

        print(bot.last_update_id)
        updates = bot.get_updates()
        
        if updates:

            bot.last_update_id = updates[-1]['update_id'] + 1

            for update in updates:

                message = bot.get_message(update)
                command, text = bot.parse_message(message)
                result = books.search(command, text)

                if result:
                    response = bot.positive_response(bot.get_chat_id(update), result)
                    bot.send_message(response)
                else:
                    response = bot.negative_response(bot.get_chat_id(update))
                    bot.send_message(response)


if __name__ == '__main__':
    main()
