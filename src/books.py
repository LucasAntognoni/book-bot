import requests


class Books(object):
    BASE_URL = \
        'https://www.googleapis.com/books/v1/volumes?' \
        'q="{}"&projection={}&printType={}&langRestrict={}&maxResults={}'

    MAX_RESULTS = 1
    PRINT_TYPE = 'books'
    PROJECTION = 'full'
    LANGUAGE = 'en'

    # SEARCH_FIELDS = {
    #     "title": "intitle",
    #     "author": "inauthor",
    #     "publisher": "inpublisher",
    #     "subject": "subject",
    #     "isbn": "isbn",
    # }

    BOOK_FIELDS = [
        'title',
        'authors',
        'categories',
        'description',
        'imageLinks'
    ]

    def __init__(self):
        pass

    @staticmethod
    def get_attribute(data, attribute, default_value):
        return data.get(attribute) or default_value

    def process_search(self, data):

        book = {}

        for field in self.BOOK_FIELDS:

            book[field] = self.get_attribute(data, field, '')

            if (field == 'authors') or (field == 'categories') and book[field] != '':
                if len(book[field]) > 1:
                    book[field] = ', '.join(book[field])
                else:
                    book[field] = book[field][0]

            if field == 'imageLinks' and book[field] != '':
                book[field] = self.get_attribute(book[field], 'thumbnail', '')

        return book

    def search(self, field, query):
        """
            Search book on Google Books API

            Parameters
            ----------
                field
                    Search field 

                query
                    Value to be searched

            Returns
            -------
                JSON
                    Search results in JSON format if successful, None o/w
        """

        if field == 'search':
            url = self.BASE_URL.format(query.replace(' ', '+'),
                                       self.PROJECTION,
                                       self.PRINT_TYPE,
                                       self.LANGUAGE,
                                       self.MAX_RESULTS)
        else:
            return None

        try:
            response = requests.get(url)

            if response.status_code == 200:

                response_json = response.json()

                if response_json['totalItems'] != 0:
                    return self.process_search(response_json['items'][0]['volumeInfo'])
                else:
                    return None

        except requests.exceptions.RequestException as e:
            print(e)
            return None



