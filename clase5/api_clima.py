import sys
import requests

r = requests.get(f"https://wttr.in/{sys.argv[1]}")

print(r.text)