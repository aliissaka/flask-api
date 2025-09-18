import requests


BASE = "http://localhost:5000"


response = requests.get(f"{BASE}/helloworld")
print(response.json())


