import csv
from menuconfig import *
import os

diretorio_base = os.path.dirname(os.path.abspath(".")) 
diretorio_data = os.path.join(diretorio_base, "dados")

class IMC:
        # Constructor
        def __init__(self,dados):
            self.dados = dados
            self.contacts = []
            self.tabela ={}
            self.banco_dados = []
           


        def arquivo(self):
            arquivo = csv.reader(open(self.dados+'.csv'),delimiter=';')
            for [primeiro_nome,sobrenomes,peso,altura] in arquivo:
                self.contacts.append((primeiro_nome,sobrenomes,peso,altura))
            #print(self.contacts)

        def filtro(self):
            for i in range(1,len(self.contacts)):
                nome = (self.contacts[i][0] + self.contacts[i][1]).upper()
                peso = (self.contacts[i][2])
                altura = (self.contacts[i][3])
                if peso != '':
                    new_peso = float(peso.replace(",",".").strip())
                    new_altura = float(altura.replace(",",".").strip())
                    imc = (new_peso / new_altura**2)
                    total = f"{imc:.2f}"
                self.tabela["Nome"] = nome
                self.tabela["Resultado"] = total
                self.banco_dados.append(self.tabela.copy())
            

        def cad_todos(self):
            for num, pessoas in enumerate(self.banco_dados):
                print(f'{num} - {pessoas["Nome"]} - {pessoas["Resultado"]}')

        def filto_pessoa(self,x):
            for num, pessoas in enumerate(self.banco_dados):
                if num == x:
                    return (f'{num} - {pessoas["Nome"]} - {pessoas["Resultado"]}')
            
              




imc = IMC(diretorio_data+"\dataset")
imc.arquivo()
imc.filtro()


while True:
    resp = menu(['Lista Usuários', 'Acessa usuarios', 'Sair do programa'])
    if resp == 1:
        print()
        imc.cad_todos()
    if resp == 2:
         i = int(input('Digite o numero da conta que você deseja acessar!:'))
         print()
         print(imc.filto_pessoa(i))
    if resp == 3:
        print('Obrigado por usar nosso dados:')
        break







