import httpx
from pprint import pprint

print("Program pro prevod CZK do libovolne meny dle aktualniho kurzu")

input_val = float(input('Zadej castku: '))
target_curr = 'EUR'

# stahnout vsechny atualni kurzy
r = httpx.get('https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt')

# rozdelit na pole - list
lines_list = r.text.split('\n')

# vybrat radek s cilovou menou
target_line = ''
for line in lines_list:
    if target_curr in line:
        target_line = line

# extrahovat kurz
exchange_rate = float(target_line.split('|')[-1].replace(',', '.'))

output_val = input_val / exchange_rate

print(f"Aktualni hodnota: {output_val:.2f} {target_curr}")

