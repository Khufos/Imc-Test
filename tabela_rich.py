
from turtle import left
from rich.table import Table
import csv
from rich.console import Console
from calc import massa
contacts = []
tabela ={}

table = Table(title='Tabela IMC')
table.add_column("Nome",justify=left,style='red')
table.add_column("Peso",style='green')
table.add_column("Altura",style='purple')
table.add_column("Resultado",style='yellow')
table.add_column("Indice de Massa Corporal",style="blue")


console = Console()
arquivo = csv.reader(open('dataset.csv'),delimiter=';')
for [primeiro_nome,sobrenomes,peso,altura] in arquivo:
    contacts.append((primeiro_nome,sobrenomes,peso,altura))

for i in range(1,len(contacts)):
    nome = (contacts[i][0] + " " + contacts[i][1]).upper()
    peso = (contacts[i][2])
    altura = (contacts[i][3])
    if peso != '':
        new_peso = float(peso.replace(",",".").strip())
        new_altura = float(altura.replace(",",".").strip())
        imc = (new_peso / new_altura**2)
        total = f"{imc:.2f}"
        table.add_row(nome,peso,altura,total,massa(imc))

console.print(table)





