import sys
import requests

body = {"name": sys.argv[1], "courses":sys.argv[2]}

r = requests.put(f"http://localhost:7001/student/{sys.argv[3]}", json=body)

print(r.status_code)