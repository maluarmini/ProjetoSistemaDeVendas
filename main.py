#from tkinter import *
import sqlite3
import os
import sys
from subprocess import call
try:
    from Tkinter import *
except ImportError:
    from tkinter import *


def click_cadastrar():
    call(["python","add_to_db.py"])

def click_atualizar():
    call(["python","update.py"])

def click_comprar():
    call(["python","pay.py"])

root = Tk()
root.geometry('1200x600')
root.resizable(False,False)
root.title('Sistema de Vendas - Maria Luiza Armini Correa')

frame_principal = Frame(root,width=1200,height=600,bg='deepskyblue4')
frame_principal.place(x=0,y=0)

frame_secundario = Frame(root,width=1200,height=150,bg='dodgerblue4')
frame_secundario.place(x=0,y=0)

label_title = Label(frame_secundario,text='SISTEMA DE VENDAS',font=('league gothic',90),bg='dodgerblue4')
label_title.place(x=280,y=30)

bt_cadastrar = Button(frame_principal,text='CADASTRAR PRODUTOS NO SISTEMA',font=('league gothic',20),bg='orange',width=70,height=3,command=click_cadastrar)
bt_cadastrar.place(x=280,y=200)

bt_atualizar = Button(frame_principal,text='ATUALIZAR PRODUTOS NO SISTEMA',font=('league gothic',20),bg='orange',width=70,height=3,command=click_atualizar)
bt_atualizar.place(x=280,y=310)

bt_compras = Button(frame_principal,text='NOVA COMPRA',font=('league gothic',20),bg='orange',width=70,height=3,command=click_comprar)
bt_compras.place(x=280,y=420)

imagem = PhotoImage(file="cadastro1.png")
i = Label(root,image=imagem,bg='deepskyblue4')
i.imagem = imagem
i.place(x = 200, y=230)

imagem = PhotoImage(file="atualizar1.png")
i = Label(root,image=imagem,bg='deepskyblue4')
i.imagem = imagem
i.place(x = 200, y=330)

imagem = PhotoImage(file="comprar1.png")
i = Label(root,image=imagem,bg='deepskyblue4')
i.imagem = imagem
i.place(x = 200, y=440)

imagem = PhotoImage(file="vendasnovo1.png")
i = Label(root,image=imagem,bg='dodgerblue4')
i.imagem = imagem
i.place(x = 1000, y=40)

root.mainloop()