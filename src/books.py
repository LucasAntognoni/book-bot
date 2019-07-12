import requests


class Books(object):

    BASE_URL = "https://www.googleapis.com/books/v1/volumes?q="
    FILTERS = [
        "intitle",
        "inauthor",
        "inpublisher",
        "subject",
        "isbn",
        "lccn",
        "oclc"
        ]

    def __init__(self):
        pass

    def search(self, filter, query):

        """
            Search book on Google Books API

            Parameters
            ----------
                filter
                    Search field 

                query
                    Value to be searched

            Returns
            -------
                JSON
                    Search results in JSON format if successful, None o/w
        """

        if filter in self.FILTERS:

            try:
        
                response = requests.get(self.BASE_URL + query)

                if response.status_code == 200:
                    return response.json()
        
            except requests.exceptions.RequestException as e:        
                # print(e)
                return None

        # print('Unsuported search field!')
        return None
