import tkinter as tk
import tkinter.ttk as ttk
from tkinter import simpledialog
 
 
class Window:
    def __init__(self, master):
        self.master = master
        columns = ("email", "salary")
 
        self.tree= ttk.Treeview(self.master, columns=columns ,height = 20)
        self.tree.pack(padx = 5, pady = 5)
 
        self.tree.heading('#0', text='Name')
        self.tree.heading('email', text='Email')
        self.tree.heading('salary', text='Salary')
 
        self.read_data()
 
 
    def read_data(self):
        with open('data.txt') as handle:
            for line in handle.readlines():
                nome,sobrenome,peso, altura = line.strip().split()
                nome = nome[1:-1]
                print(nome)
                '''self.tree.insert('', tk.END, iid = nome, 
                                    text = temp[0], values = temp[1:])'''
 
 
root = tk.Tk()
window = Window(root)
root.mainloop()