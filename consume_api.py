import json
import requests

archivo = open("/consumeAPI/hibiscus.json", "w")
response = requests.post("https://api-manganeso.herokuapp.com/producto/0")
messageJson = response.json()
x = json.dumps(messageJson)
print(x)
archivo.write(x)
archivo.close()

response = requests.get("https://api-manganeso.herokuapp.com/producto/0")
messageJson = response.json()
print(messageJson)
