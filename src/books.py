import requests


class Books(object):

    BASE_URL = "https://www.googleapis.com/books/v1/volumes?q="
    SEARCH_FIELDS = {
        "title": "intitle",
        "author": "inauthor",
        "publisher": "inpublisher",
        "subject": "subject",
        "isbn": "isbn",
    }

    def __init__(self):
        pass

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

        if self.SEARCH_FIELDS[field]:
            
            try:
                response = requests.get(self.BASE_URL + query)

                if response.status_code == 200:
                    return response.json()
        
            except requests.exceptions.RequestException as e:        
                return None

        return None

    def process_search(self, field, data):
        pass
