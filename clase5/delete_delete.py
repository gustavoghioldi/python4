import sys
import requests

r = requests.delete(f"http://localhost:7001/student/{sys.argv[1]}")

print(r.status_code)