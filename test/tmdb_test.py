import http.client

conn = http.client.HTTPSConnection("api.themoviedb.org")

payload = "{}"

# use your key 
conn.request("GET", "/3/search/person?include_adult=false&page=1&query=Ian%20McKellen&language=en-US&api_key=YOURKEYHERE", payload)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
