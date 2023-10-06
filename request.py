import requests
res = requests.post('http://localhost:8000/items/',
    headers = {
        #'User-agent'  : 'Internet Explorer/2.0',
        'Content-type': 'application/json'
    },
    json = {"text": "Fast API",
            "name": "jaber"},
)
#print(res.headers['content-type'])
print(res.text)