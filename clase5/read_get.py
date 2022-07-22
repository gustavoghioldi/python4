import requests

r = requests.get("http://localhost:7001/student")

print(r.json())