import requests

response = requests.get("https://criptoya.com/api/dolar")
print(response.status_code)
print(response.json())

response = requests.get("https://criptodasdasd.com")

#STATUS
# 2XX <-- OK
# 4XX <-- problemas del cliente
# 5XX <--  problemas del servidor.
# response = requests.get("https://google.com")
# print(response.text)

