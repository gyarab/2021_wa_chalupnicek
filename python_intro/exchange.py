import httpx
from pprint import pprint

# nacist vstupy
input_value = float(input('Zadejte castku CZK pro prevod: '))
target_currency = input('Zadejte cilovou menu: ').upper()

# stahnout vsechny kurzy
r = httpx.get('https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt')
rates_str = r.text

# rozsekat vstup na pole radku
rates_list = rates_str.split('\n')

target_rate_str = None
for rate_item in rates_list:
    if target_currency in rate_item:
        # radek, ktery obsahuje target_currency si dame bokem
        target_rate_str = rate_item

if not target_rate_str:
    print('Zadana mena nenalezena')
    exit()

rate = float(target_rate_str.split('|')[-1].replace(',', '.'))

# provest vypocet
output_value = input_value / rate

# vypsat vystup
print(f"Prevedena castka: {output_value:.2f} {target_currency}")
