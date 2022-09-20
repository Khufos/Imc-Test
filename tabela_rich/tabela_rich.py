
from turtle import left
from rich.table import Table
import csv
from rich.console import Console
from calc import massa
import os
diretorio_base = os.path.dirname(os.path.abspath(".")) 
diretorio_data = os.path.join(diretorio_base, "dados")
#==================================================================#
dados= []
tabela ={}
#==================================================================#
table = Table(title='Tabela IMC')
table.add_column("Nome",justify=left,style='red')
table.add_column("Peso",style='green')
table.add_column("Altura",style='purple')
table.add_column("Resultado",style='yellow')
table.add_column("Indice de Massa Corporal",style="blue")
#========================================================================#
console = Console()
arquivo = csv.reader(open(diretorio_data+"\dataset.csv"),delimiter=';')
for [primeiro_nome,sobrenomes,peso,altura] in arquivo:
    dados.append((primeiro_nome,sobrenomes,peso,altura))
#========================================================================
for index, values in enumerate(dados):
    if index == 0:
        continue
    nome = (values[0]+" " + " "+values[1]).strip().upper().replace("   ", " ")
    peso = values[2]
    altura = values[3]  
    if peso != '':
        new_peso = float(peso.replace(",","."))
        new_altura = float(altura.replace(",","."))
    imc = (new_peso / new_altura**2)
    total = f"{imc:.2f}"
    table.add_row(nome,peso,altura,total,massa(imc))
console.print(table)