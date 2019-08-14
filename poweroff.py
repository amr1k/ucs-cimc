import requests
import secrets
from xml.etree import ElementTree as ET

url = "https://"+secrets.server+"/nuova"

payload = "<aaaLogin\n    inName=\'"+secrets.username+"\'\n    inPassword=\'"+secrets.password+"\'>\n</aaaLogin>"
headers = {
    'Content-Type': "text/plain",
    'Accept': "*/*",
    'Cache-Control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers, verify=False)

print(response.text.outCookie)