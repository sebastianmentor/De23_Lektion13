import requests
import dotenv
import os
from rich import print_json

dotenv.load_dotenv('.env')

NEWSAPI_APIKEY = os.getenv("NEWSAPI_APIKEY")

# https://newsapi.org/
# https://newsapi.org/docs/get-started#search
# https://newsapi.org/docs/endpoints/top-headlines

# GET https://newsapi.org/v2/everything?q=Apple&from=2023-10-02&sortBy=popularity&apiKey=API_KEY
def get_newsapi1():
       url = ('https://newsapi.org/v2/everything?'
              'q=Apple&'
              'from=2023-10-02&'
              'sortBy=popularity&'
              f'apiKey={NEWSAPI_APIKEY}')

       response = requests.get(url)
       return response.json()

def get_newsapi2():
       url = ('https://newsapi.org/v2/top-headlines?'
              'country=us&'
              f'apiKey={NEWSAPI_APIKEY}')
       response = requests.get(url)
       return response.json()

def get_newsapi3():
       url = ('https://newsapi.org/v2/top-headlines?'
              'sources=bbc-news&'
              f'apiKey={NEWSAPI_APIKEY}')

       response = requests.get(url)
       return response.json()

print_json(data=get_newsapi3())