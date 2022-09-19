import csv
from encodings import utf_8
contacts = []
arquivo = csv.reader(open('dataset.csv'),delimiter=';')
for [primeiro_nome,sobrenomes,peso,altura] in arquivo:
    contacts.append((primeiro_nome,sobrenomes,peso,altura))
#print(contacts[1::])

with open('dataimc.txt','w',encoding=('utf-8')) as handle:
    for piece in contacts:
        handle.write(str(piece).strip() +'\n')













