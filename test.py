import requests

URL = "http://127.0.0.1:5000" 

def get(route, req=None):
    url_route = URL + route
    r = requests.get(url=url_route, params=req)
    return r.json()

def post(route, data):
    url_route = URL + route
    r = requests.post(url=url_route, params=data)

if __name__ == '__main__':
    post('/names/google', {'url': 'www.google.com'})