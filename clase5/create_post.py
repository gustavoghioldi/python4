import sys
import requests

body = {"name": sys.argv[1], "courses":sys.argv[2]}
r = requests.post("http://localhost:7001/student", json=body)

print(r.status_code)