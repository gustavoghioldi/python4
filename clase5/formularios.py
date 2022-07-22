import requests
body = {
    "name": "Gus",
    "email": "gus@gus.com",
    "message":"hola mundo"
}

#Formularios el dict de manda como data y en rest el dict lo mandamos como json
r = requests.post("http://localhost:8880/form", data=body)

print(r.status_code)