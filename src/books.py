import requests


class Books(object):
    BASE_URL = 'https://www.googleapis.com/books/v1/volumes?q="{}"&printType={}&maxResults={}'

    MAX_RESULTS = 1
    PRINT_TYPE = 'books'

    # SEARCH_FIELDS = {
    #     "title": "intitle",
    #     "author": "inauthor",
    #     "publisher": "inpublisher",
    #     "subject": "subject",
    #     "isbn": "isbn",
    # }

    def __init__(self):
        pass

    def process_search(self, data):
        book = {
            'title': data['items'][0]['volumeInfo']['title'],
            'authors': data['items'][0]['volumeInfo']['authors'],
            'publisher': data['items'][0]['volumeInfo']['publisher'],
            'publishedDate': data['items'][0]['volumeInfo']['publishedDate'],
            'categories': data['items'][0]['volumeInfo']['categories'],
            'averageRating': data['items'][0]['volumeInfo']['averageRating'],
            'language': data['items'][0]['volumeInfo']['language']
        }

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
            url = self.BASE_URL.format(query.replace(' ', '+'), self.PRINT_TYPE, self.MAX_RESULTS)
        else:
            return None

        try:
            response = requests.get(url)

            if response.status_code == 200:
                return self.process_search(response.json())

        except requests.exceptions.RequestException as e:
            print(e)
            return None



