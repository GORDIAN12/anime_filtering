import http.client

conn = http.client.HTTPSConnection("imdb-movies-web-series-etc-search.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "7e5e99738amsh5df59f7fab899acp1232cejsnadcccb8d8c31",
    'x-rapidapi-host': "imdb-movies-web-series-etc-search.p.rapidapi.com"
}

conn.request("GET", "/yugioh!gx.json", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))