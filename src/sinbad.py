from books import Books
from bot import Bot

books = Books()
bot = Bot()


def main():

    while(True):

        updates = bot.get_updates()
        
        if updates:

            bot.last_update_id = updates[-1]['update_id'] + 1

            for update in updates:

                if 'edited_message' in update:
                    message_field = 'edited_message'
                else:
                    message_field = 'message'

                message = bot.get_message(update, message_field)

                command, text = bot.parse_message(message)
                result = books.search(command, text)

                if result:
                    response = bot.positive_response(bot.get_chat_id(update, message_field), result)
                    bot.send_message(response)
                else:
                    response = bot.negative_response(bot.get_chat_id(update, message_field))
                    bot.send_message(response)


if __name__ == '__main__':
    main()
