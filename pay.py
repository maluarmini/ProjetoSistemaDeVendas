import sqlite3
from subprocess import call
import datetime
import math

try:
    from tkinter import *
except ImportError:
    from Tkinter import *

conn = sqlite3.connect('DataBase/store.db')

c = conn.cursor()

data = datetime.datetime.now().date()

products_list = []
products_preco = []
products_quantidade = []
products_id = []
labels_list = []

class Aplication:
    def __init__(self,master,*args,**kwargs):
        self.master = master
        self.frame_principal = Frame(self.master,width=1200,height=600,bg='Honeydew1')
        self.frame_principal.place(x=0,y=0)

        self.frame_secundario = Frame(self.master,width=1200,height=150,bg='lightsteelblue')
        self.frame_secundario.place(x=0,y=0)

        self.label_title = Label(self.frame_secundario,text='NOVA COMPRA',font=('league gothic',90),bg='lightsteelblue')
        self.label_title.place(x=360,y=30)

        imagem = PhotoImage(file='comprarnovo1.png')
        i = Label(self.master,image=imagem,bg='lightsteelblue')
        i.imagem = imagem
        i.place(x = 890, y=45)

        self.left = Frame(self.frame_principal,width=700,height=600,bg='Honeydew1')
        self.left.pack(side = LEFT)
        
        self.right = Frame(self.frame_principal, width=500, height = 600, bg='Honeydew2')
        self.right.pack(side=RIGHT)

        self.data_l = Label(self.right,text='Data: ' + str(data),font=('arial',15,'bold'),bg='Honeydew2')
        self.data_l.place(x=0,y=150)

        self.produto_l = Label(self.right,text='Produto ',font=('arial',15,'bold'),bg='Honeydew2')
        self.produto_l.place(x=0,y=200)

        self.produto_l = Label(self.right,text='Quantidade ',font=('arial',15,'bold'),bg='Honeydew2')
        self.produto_l.place(x=170,y=200)

        self.produto_l = Label(self.right,text='Valor ',font=('arial',15,'bold'),bg='Honeydew2')
        self.produto_l.place(x=370,y=200)

        self.inserir_l = Label(self.left,text='Produto ID: ',font=('arial',15,'bold'),bg='Honeydew1')
        self.inserir_l.place(x=0,y=150)

        self.inserir_e = Entry(self.left,width=10,font=('arial',18))
        self.inserir_e.place(x=150,y=150)

        self.btn_search = Button(self.left,text='Pesquisar',width=10, height=1,bg='orange',fg='black',font=('arial',11,'bold'),command=self.jx)
        self.btn_search.place(x=290,y=150)

        self.productname = Label(self.left,text='',font=('arial',20,'bold'),bg='Honeydew1')
        self.productname.place(x=0,y=200)

        self.productpreco = Label(self.left,text='',font=('arial',20,'bold'),bg='Honeydew1')
        self.productpreco.place(x=0,y=250)

        self.total = Label(self.right,text='Total: ',font=('arial',30,'bold'),bg='Honeydew2',fg='red')
        self.total.place(x=0,y=560)

    def jx(self,*args,**kwargs):
        self.get_id = self.inserir_e.get()

        sql = "SELECT * FROM inventory WHERE id=?"

        result = c.execute(sql,self.get_id,)

        for self.r in result:
            self.get_id = self.r[0]
            self.get_name = self.r[1]
            self.get_preco = self.r[4]
            self.get_stock = self.r[2]

        self.productname.configure(text='Nome Produto: ' + str(self.get_name))
        self.productpreco.configure(text='Preco: R$ ' + str(self.get_preco))

        self.qtd_l = Label(self.left,text='Quantidade:', font=('arial',18,'bold'),bg='Honeydew1')
        self.qtd_l.place(x=0,y=300)

        self.qtd_e = Entry(self.left,width=20,bd="0",font=('arial',18,'bold'))
        self.qtd_e.place(x=190,y=300)
        
        self.desconto_l = Label(self.left,text='Desconto:', font=('arial',18,'bold'),bg='Honeydew1')
        self.desconto_l.place(x=0,y=370)

        self.desconto_e = Entry(self.left,width=20,bd="0",font=('arial',18,'bold'))
        self.desconto_e.place(x=190,y=370)
        self.desconto_e.insert(END,0)

        self.btn_carrinho = Button(self.left,text='Adicionar ao Carrinho',width=20, height=2,bg='orange',fg='black',font=('arial',10,'bold'),command=self.carrinho)
        self.btn_carrinho.place(x=290,y=410)

        self.troco_1 = Label(self.left,text='Total Pago: ', font=('arial',18,'bold'),bg='Honeydew1')
        self.troco_1.place(x=0,y=470)

        self.troco_e = Entry(self.left,width=20,bd="0",font=('arial',18,'bold'),bg='lemonchiffon')
        self.troco_e.place(x=190,y=470)

        self.btn_troco = Button(self.left,text='Calcular Troco',width=20, height=2,bg='tomato',fg='black',font=('arial',10,'bold'),command=self.calcular_troco)
        self.btn_troco.place(x=290,y=510)
    
    def calcular_troco(self,*args,**kwargs):
        self.amount_give = float(self.troco_e.get())
        self.our_total = float(sum(products_preco))
        self.to_give = self.amount_give - self.our_total

        self.c_amount = Label(self.left,text='Troco: R$' + str(self.to_give),font=('arial',30,'bold'),bg='honeydew1',fg='red')
        self.c_amount.place(x=0,y=560)
    
    def carrinho(self,*args,**kwrags):
        self.quantidade_value = int(self.qtd_e.get())
        if self.quantidade_value > int(self.get_stock):
            print('Falta No Estoque')
        else:
            self.final_preco = ((float(self.quantidade_value) * float(self.get_preco)) - float(self.desconto_e.get()))
            products_list.append(self.get_name)
            products_preco.append(self.final_preco)
            products_quantidade.append(self.quantidade_value)
            products_id.append(self.get_id)

            self.x_index = 0  
            self.y_index = 250
            self.counter = 0

            for self.p in products_list:
                self.tempname = Label(self.right,text=str(products_list[self.counter]),font=('arial',18,'bold'),bg='honeydew2',fg='black')
                self.tempname.place(x=0,y=self.y_index)
                labels_list.append(self.tempname)

                self.tempqtd = Label(self.right,text=str(products_quantidade[self.counter]),font=('arial',18,'bold'),bg='honeydew2',fg='black')
                self.tempqtd.place(x=300,y=self.y_index)
                labels_list.append(self.tempqtd)

                self.temppreco = Label(self.right,text="R$"+str(products_preco[self.counter]),font=('arial',16,'bold'),bg='honeydew2',fg='black')
                self.temppreco.place(x=370,y=self.y_index)
                labels_list.append(self.temppreco)

                self.y_index += 40
                self.counter += 1

                self.total.configure(text='Total: R$' + str(sum(products_preco)))

                self.qtd_l.place_forget()
                self.qtd_e.place_forget()
                self.desconto_l.place_forget()
                self.desconto_e.place_forget()
                self.productname.configure(text="")
                self.productpreco.configure(text="")
                self.btn_carrinho.destroy()
                self.inserir_e.focus()
                self.inserir_e.delete(0,END)



root = Tk()
root.geometry('1200x600')
root.resizable(False,False)
root.title('Sistema de Vendas - Maria Luiza Armini Correa')
app = Aplication(root)

root.mainloop()