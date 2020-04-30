#from tkinter import *
import sqlite3
import os
import sys
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
  
conn = sqlite3.connect('DataBase/store.db')

c = conn.cursor()

result = c.execute('SELECT MAX(id) from inventory')

for r in result:
    id = r[0]

class DataBase():
    def __init__(self,master,*args,**kwargs):
        self.master = master
        self.frame_principal = Frame(self.master,width=1200,height=600,bg='Honeydew1')
        self.frame_principal.place(x=0,y=0)

        self.frame_secundario = Frame(self.master,width=1200,height=150,bg='lightsteelblue')
        self.frame_secundario.place(x=0,y=0)

        self.label_title = Label(self.frame_secundario,text='CADASTRAR PRODUTOS',font=('league gothic',90),bg='lightsteelblue')
        self.label_title.place(x=260,y=30)

        self.name_l = Label(self.master,text='Nome do produto: ',font=('arial',17,'bold'),bg='Honeydew1')
        self.name_l.place(x=0,y=150)

        self.stock_l = Label(self.master,text='Estoque: ',font=('arial',17,'bold'),bg='Honeydew1')
        self.stock_l.place(x=0,y=200)

        self.cp_l = Label(self.master,text='Preco de custo: ',font=('arial',17,'bold'),bg='Honeydew1')
        self.cp_l.place(x=0,y=250)

        self.sp_l = Label(self.master,text='Preco de venda: ',font=('arial',17,'bold'),bg='Honeydew1')
        self.sp_l.place(x=0,y=300)

        self.vendor_l = Label(self.master,text='Nome do fornecedor: ',font=('arial',17,'bold'),bg='Honeydew1')
        self.vendor_l.place(x=0,y=350)

        self.vendor_phone_l = Label(self.master,text='Contato do fornecedor: ',font=('arial',17,'bold'),bg='Honeydew1')
        self.vendor_phone_l.place(x=0,y=400)

        self.id_l = Label(self.master,text='ID do produto: ',font=('arial',17,'bold'),bg='Honeydew1')
        self.id_l.place(x=0,y=450)

        #CAIXAS DE TEXTOS
        self.name_e = Entry(self.master,width = 25,font=('arial',17,'bold'))
        self.name_e.place(x=310,y=150)

        self.stock_e = Entry(self.master,width = 25,font=('arial',17,'bold'))
        self.stock_e.place(x=310,y=200)

        self.cp_e = Entry(self.master,width = 25,font=('arial',17,'bold'))
        self.cp_e.place(x=310,y=250)

        self.sp_e = Entry(self.master,width = 25,font=('arial',17,'bold'))
        self.sp_e.place(x=310,y=300)

        self.vendor_e = Entry(self.master,width = 25,font=('arial',17,'bold'))
        self.vendor_e.place(x=310,y=350)

        self.vendor_phone_e = Entry(self.master,width = 25,font=('arial',17,'bold'))
        self.vendor_phone_e.place(x=310,y=400)

        self.id_e = Entry(self.master,width = 25,font=('arial',17,'bold'))
        self.id_e.place(x=310,y=450)

        self.btn_add = Button(self.frame_principal,width=10,height=2,font=('arial',17),text='CADASTRAR',bg='deepskyblue4',fg='black',command = self.get_itens)
        self.btn_add.place(x=310,y=520)

        self.btn_clear = Button(self.frame_principal,width=10,height=2,font=('arial',17),text='LIMPAR',bg='brown2',fg='black',command=self.clear_all)
        self.btn_clear.place(x=480,y=520)

        self.box_text = Text(self.master,width=60,height=18)
        self.box_text.place(x=710,y=150)
        self.box_text.insert(END,'Ultimo ID cadastrado no sistema foi: ' + str(id))

        imagem = PhotoImage(file="cadastronovo1.png")
        i = Label(root,image=imagem,bg='lightsteelblue')
        i.imagem = imagem
        i.place(x = 1030, y=45)
    
    def get_itens(self,*args,**kwargs):
        self.name = self.name_e.get()
        self.stock = self.stock_e.get()
        self.cp = self.cp_e.get()
        self.sp = self.sp_e.get()
        self.vendor = self.vendor_e.get()
        self.vendor_phone = self.vendor_phone_e.get()

        self.totalcp = (float(self.cp) * float(self.stock))
        self.totalsp = (float(self.sp) * float(self.stock))

        self.assumed_profit = float(self.totalsp - self.totalcp)

        if self.name == '' or self.stock == '' or self.cp == '' or self.sp == '':
            print('ERRO')
            #tkinter.messagebox.showinfo('Sistema de Vendas','Impossivel cadastrar produto sem preencher todos os campos')
        else:
            sql = "INSERT INTO inventory (name,stock,cp,sp,totalcp,totalsp,assumed_profit,vendor,vendor_phoneno) VALUES(?,?,?,?,?,?,?,?,?)"

            c.execute(sql,(self.name,self.stock,self.cp,self.sp,self.totalcp,self.totalsp,self.assumed_profit,self.vendor,self.vendor_phone))

            conn.commit()
            
            self.box_text.insert(END,"\n\nCadastrado " + str(self.name) + ' No Banco de Dados com o ID: ' + str(self.id_e.get()))

           #tkinter.messagebox.showinfo('Sistema de Vendas','Produto cadastrado com sucesso no Banco de Dados.')
    
    def clear_all(self,*args,**kwargs):
        self.name_e.delete(0,END)
        self.stock_e.delete(0,END)
        self.cp_e.delete(0,END)
        self.sp_e.delete(0,END)
        self.vendor_e.delete(0,END)
        self.vendor_phone_e.delete(0,END)


root = Tk()
root.geometry('1200x600')
root.resizable(False,False)
root.title('Cadastro de Produtos - Maria Luiza Armini Correa')
DB = DataBase(root)

root.mainloop()