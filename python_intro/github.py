import httpx
import json

with open('token.txt') as soubor:
    token = soubor.read().strip()

headers = {
    'Authorization': f'token {token}'
}

# stažení stránky
stranka = httpx.put('https://api.github.com/user/starred/django/django', headers=headers)

# ověření, že dotaz proběhl v pořádku
stranka.raise_for_status()

# vypsání obsahu
print(stranka.text)
# data = json.loads(stranka.text)
# print(json.dumps(data, ensure_ascii=True, indent=2))