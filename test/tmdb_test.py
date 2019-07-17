import http.client

conn = http.client.HTTPSConnection("api.themoviedb.org")

payload = "{}"

conn.request("GET", "/3/search/person?include_adult=false&page=1&query=Ian%20McKellen&language=en-US&api_key=4e451d47079417d82742022a3cf54988", payload)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))