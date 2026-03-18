import requests
from bs4 import BeautifulSoup
import sqlite3


url = 'https://www.idealsoftwares.com.br/indices/ipca_ibge.html'

response = requests.get(url)
html_content = response.content

Beauti = BeautifulSoup(html_content, 'html.parser')

soup = Beauti.find_all(
    name='table',
    attrs={'class': 'table table-bordered table-striped text-center'}
)

texto = soup[0]
#print(soup.prettify()[:3000])

ipca_data = []
for row in texto.find_all('tr')[1:]:
    cols = row.find_all('td')
    if cols:
        data = cols[0].text.strip()
        valor = cols[1].text.strip().replace(',', '.').replace(' ', '').replace('/n', '')
        if valor:
            ipca_data.append((data, valor))

conn = sqlite3.connect('ipca_data.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS ipca (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          valor REAL,
          data TEXT
    )''')

cursor.execute('CREATE UNIQUE INDEX IF NOT EXISTS idx_ipca_data ON ipca(data, valor)')

cursor.executemany(
    'INSERT OR IGNORE INTO ipca (data, valor) VALUES (?, ?)',
    [(data, valor) for valor, data in ipca_data]
)

conn.commit()

dados_brutos_do_banco = cursor.execute('SELECT * FROM ipca').fetchall()

conn.close()

print("Dados brutos do banco:")
for row in dados_brutos_do_banco:
    print(row)

print("\nDados organizados\n"+("=" * 30))
dados_dict = {row[1]: row[2] for row in dados_brutos_do_banco}

for item_data, iten_valor in dados_dict.items():
    print(f"Data: {item_data}, Valor: {iten_valor}")

#Alternativamente, usando uma compreensão de lista para formatar a saída:
# print("\nDados organizados\n" + ("@" * 30))
# print("\n".join(f"Data: {item_data}, Valor: {item_valor}" for item_data, item_valor in dados_dict.items()))

print("\nDeu bom! Confia")