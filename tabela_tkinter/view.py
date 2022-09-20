from codecs import utf_8_decode, utf_8_encode
from hashlib import new
from tkinter.messagebox import showinfo
from opcode import hasjabs
from tkinter import *
from tkinter import ttk
import os
import csv
diretorio_base = os.path.dirname(os.path.abspath(".")) 
diretorio_data = os.path.join(diretorio_base, "dados")

class Tela:
    
    def __init__(self, window):
        self.window = window
        self.window.title("Calculo IMC ")
        #self.window.geometry("400x400")
        #self.window.resizable(width=0, height=0)
        self.tree= ttk.Treeview(self.window, selectmode='browse',column=("Column1","Column2","Column3","Column4"),show='headings')
    
        #--------Show cabeçario -------------""
        self.tree.column("Column1",width=250,minwidth=50,stretch=NO)
        self.tree.heading("#1",text='Nome')
        #===========================================================#
        self.tree.column("Column2",width=120,minwidth=50,stretch=NO)
        self.tree.heading("#2",text='Peso(kg)')
         #===========================================================#
        self.tree.column("Column3",width=100,minwidth=50,stretch=NO)
        self.tree.heading("#3",text='Altura(m)')
        #============================================================
        self.tree.column("Column4",width=120,minwidth=50,stretch=NO)
        self.tree.heading("#4",text='Resultado do IMC')
        dados = []
        self.resultado = []
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
            self.resultado.append((nome,peso,altura,total))   
               
        
        for contact in self.resultado:
            self.tree.insert('', END, values=contact)
        self.tree.grid(row=0,column=0)


            

    
       
window=Tk()
Tela(window)
window.mainloop()