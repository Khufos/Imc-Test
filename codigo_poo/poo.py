import csv
from dis import code_info
from optparse import Values
from menuconfig import *
import os

diretorio_base = os.path.dirname(os.path.abspath(".")) 
diretorio_data = os.path.join(diretorio_base, "dados")

class IMC:
    def __init__(self,arquivo):
        self.arquivo = arquivo
        self.dados= []
        self.tabela ={}
        self.banco_dados = []

    def ler_arquivo(self):
        arquivo = csv.reader(open(self.arquivo+'.csv'),delimiter=';')
        for [primeiro_nome,sobrenomes,peso,altura] in arquivo:
            self.dados.append((primeiro_nome,sobrenomes,peso,altura))
        #print(self.contacts)

    def calcula_imc(self):
        for index, values in enumerate(self.dados):
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
            self.tabela["Nome"] = nome
            self.tabela["Resultado"] = total
            self.banco_dados.append(self.tabela.copy())
            


    def listar_usuarios(self):
        for num, pessoas in enumerate(self.banco_dados):
            print(f'{pessoas["Nome"]}  {pessoas["Resultado"]}')

    def filtar_nomes(self,x):
        for num, pessoas in enumerate(self.banco_dados):
            if num == x:
                return (f'{num} - {pessoas["Nome"]}  {pessoas["Resultado"]}')

imc = IMC(diretorio_data+"\dataset")
imc.ler_arquivo()
imc.calcula_imc()


while True:
    resp = menu(['Lista Usuários', 'Acessa usuarios', 'Sair do programa'])
    if resp == 1:
        print()
        imc.listar_usuarios()
    if resp == 2:
         i = int(input('Digite o numero da conta que você deseja acessar!:'))
         print()
         print(imc.filtar_nomes(i))
    if resp == 3:
        print('Obrigado por usar nosso dados:')
        break







