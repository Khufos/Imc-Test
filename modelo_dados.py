import csv
from msilib.schema import tables
contacts = []
tabela ={}
arquivo = csv.reader(open('dataset.csv'),delimiter=';')
for [primeiro_nome,sobrenomes,peso,altura] in arquivo:
    contacts.append((primeiro_nome,sobrenomes,peso,altura))

for i in range(1,len(contacts)):
    nome = (contacts[i][0] + contacts[i][1]).upper()
    peso = (contacts[i][2])
    altura = (contacts[i][3])
    if peso != '':
        new_peso = float(peso.replace(",",".").strip())
        new_altura = float(altura.replace(",",".").strip())
        imc = (new_peso / new_altura**2)
        total = f"{imc:.2f}"
    tabela["Nome"] = nome
    tabela["Resultado"] = total
    for k, v in tabela.items():
        print(k, v)

