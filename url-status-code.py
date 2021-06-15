##################################
## Author: Thiago S Almeida     ##
## E-mail: thiagodons@gmail.com ##
##################################


import pandas as pd
from pandas import ExcelWriter
import requests


urls = pd.read_excel("lista-urls.xlsx", sheet_name="urls")
url_lista = []
status_lista = []

for indice in range(0, len(urls)):
    url = urls['urls'][indice]
    r = requests.get(url)
    status = r.status_code
    print("{0}  | status code = {1} ".format(url, status))

    #adicionando valores a  lista urls e status
    url_lista.append(url)
    status_lista.append(status)

#inserindo df
df = pd.DataFrame({'urls' : url_lista, 'status-code' : status_lista })

# Escrita no novo arquivo
with ExcelWriter("urls-status-gerado.xlsx") as w:
    df.to_excel(w, 'URLs', index=False)




