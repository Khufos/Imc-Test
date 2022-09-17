from codecs import utf_8_decode, utf_8_encode
from hashlib import new
from tkinter.messagebox import showinfo
from opcode import hasjabs
from tkinter import *
from tkinter import ttk
import csv


class Tela:
    
    def __init__(self, window):
        self.window = window
        self.window.title("Calculo IMC ")
        #self.window.geometry("400x400")
        #self.window.resizable(width=0, height=0)
        self.tree= ttk.Treeview(self.window, selectmode='browse',column=("Column1","Column2","Column3","Column4"),show='headings')
    
        #--------Show cabeçario -------------""
        self.tree.column("Column1",width=200,minwidth=50,stretch=NO)
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

        self.contacts = []
        self.resultado = []
        arquivo = csv.reader(open('dataset.csv'),delimiter=';')
        for [primeiro_nome,sobrenomes,peso,altura] in arquivo:
            self.contacts.append((primeiro_nome,sobrenomes,peso,altura))
        for i in range(1,len(self.contacts)):
            nome = (self.contacts[i][0] + self.contacts[i][1]).upper()
            peso = (self.contacts[i][2])
            altura = (self.contacts[i][3])
            if peso != '':
                new_peso = float(peso.replace(",",".").strip())
                new_altura = float(altura.replace(",",".").strip())
                imc = (new_peso / new_altura**2)
                total = f"{imc:.2f}"
                self.resultado.append((nome,peso,altura,total))      
        for contact in self.resultado:
            self.tree.insert('', END, values=contact)
        self.tree.grid(row=0,column=0)


            

    
       
window=Tk()
Tela(window)
window.mainloop()