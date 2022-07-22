import sys
import requests

r = requests.get(f"http://localhost:7001/student/{sys.argv[1]}")

student = r.json()
print((student))
print(f"id:  {student['id']}")
print(f"nombre:  {student['nombre']}")
print(f"cursos:  {student['cursos']}")