from fastapi import FastAPI
from decouple import config
from app.helper import make_get_request


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health")
def health_route():
    return {"status": "Healthy"}


@app.get("/get_news/{query}")
def get_news(query):
    q = query
    url = config('URL')
    data = make_get_request(url=url, params={ 'q': q })
    articles = data['articles']
    return {'articles': articles}
