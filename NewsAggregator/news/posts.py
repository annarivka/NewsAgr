import requests
from django.conf import settings


class NewsData:

    def __init__(self, country_list=[], category_list=[]):
        self.data = None
        if len(country_list) == 0:
            self.country = 'il'
        else:
            self.country = ','.join(country_list)

        if len(category_list) == 0:
            self.category = 'top'
        else:
            self.category = ','.join(category_list)

        self.url = f'https://newsdata.io/api/1/news?apikey={settings.API_KEY}' \
                   f'&country={self.country}&category={self.category}'
        self.message = ''
        self.code = ''

    def get_data(self):
        resp = requests.get(self.url)
        res = resp.json()

        if res['status'] == 'success':
            self.data = res['results']
        elif res['status'] == 'error':
            self.message = res['results']['message']
            self.code = res['results']['code']


