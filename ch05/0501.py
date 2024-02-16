import requests

# Status code returns 200 upon success (404 for failure)
# Headers gives diagnostic information for the query, and we save the google site to an html file
url = "http://www.google.com"
res = requests.get(url)
print(res.status_code)
print(res.headers)
with open("google.html", "w") as f:
    f.write(res.text)
print("Done")