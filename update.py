import sqlite3
import os
import sys
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

conn = sqlite3.connect('DataBase/store.db')

c = conn.cursor()

result = c.execute("SELECT MAX(id) from inventory")

for r in result:
    id = r[0]

class DataBase:
    def __init__(self,master,*args,**kwargs):
        self.master = master
        self.frame_principal = Frame(self.master,width=1200,height=600,bg='Honeydew1')
        self.frame_principal.place(x=0,y=0)

        self.frame_secundario = Frame(self.master,width=1200,height=150,bg='lightsteelblue')
        self.frame_secundario.place(x=0,y=0)

        self.label_title = Label(self.frame_secundario,text='ATUALIZAR PRODUTOS',font=('league gothic',90),bg='lightsteelblue')
        self.label_title.place(x=260,y=30)

        imagem = PhotoImage(file='atualizarnovo1.png')
        i = Label(master,image=imagem,bg='lightsteelblue')
        i.imagem = imagem
        i.place(x=1030,y=45)

        self.id_l = Label(master,text='Digite um ID: ',font=('arial',18,'bold'),bg='honeydew1')
        self.id_l.place(x=0,y=150)

        self.name_l = Label(master,text='Nome do Produto: ',font=('arial',18,'bold'),bg='honeydew1')
        self.name_l.place(x=0,y=200)

        self.stock_l = Label(master,text='Estoque: ',font=('arial',18,'bold'),bg='honeydew1')
        self.stock_l.place(x=0,y=250)

        self.cp_l = Label(master,text='Preco de Custo: ',font=('arial',18,'bold'),bg='honeydew1')
        self.cp_l.place(x=0,y=300)

        self.sp_l = Label(master,text='Preco de Venda: ',font=('arial',18,'bold'),bg='honeydew1')
        self.sp_l.place(x=0,y=350)

        self.totalcp_l = Label(master,text='Total Preco Custo: ',font=('arial',18,'bold'),bg='honeydew1')
        self.totalcp_l.place(x=0,y=400)

        self.totalsp_l = Label(master,text='Total Preco Venda: ',font=('arial',18,'bold'),bg='honeydew1')
        self.totalsp_l.place(x=0,y=450)

        self.vendor_l = Label(master,text='Nome do Fornecedor: ',font=('arial',18,'bold'),bg='honeydew1')
        self.vendor_l.place(x=0,y=500)

        self.vendor_phone_l = Label(master,text='Contato do Fornecedor: ',font=('arial',18,'bold'),bg='honeydew1')
        self.vendor_phone_l.place(x=0,y=550)

        self.id_e = Entry(self.master,width = 10,font=('arial',17,'bold'))
        self.id_e.place(x=310,y=150)

        self.name_e = Entry(self.master,width = 25,font=('arial',17,'bold'))
        self.name_e.place(x=310,y=200)

        self.stock_e = Entry(self.master,width = 25,font=('arial',17,'bold'))
        self.stock_e.place(x=310,y=250)

        self.cp_e = Entry(self.master,width = 25,font=('arial',17,'bold'))
        self.cp_e.place(x=310,y=300)

        self.sp_e = Entry(self.master,width = 25,font=('arial',17,'bold'))
        self.sp_e.place(x=310,y=350)

        self.totalcp_e = Entry(self.master,width = 25,font=('arial',17,'bold'))
        self.totalcp_e.place(x=310,y=400)

        self.totalsp_e = Entry(self.master,width = 25,font=('arial',17,'bold'))
        self.totalsp_e.place(x=310,y=450)

        self.vendor_e = Entry(self.master,width = 25,font=('arial',17,'bold'))
        self.vendor_e.place(x=310,y=500)

        self.vendor_phone_e = Entry(self.master,width = 25,font=('arial',17,'bold'))
        self.vendor_phone_e.place(x=310,y=550)

        self.btn_search = Button(self.master,width=9,height=1,text='PESQUISAR',font=('arial',14),bg='orange',command=self.search)
        self.btn_search.place(x=480,y=150)
        
        self.btn_att = Button(self.master,width=15,height=2,text='ATUALIZAR',font=('arial',14,'bold'),bg='Deepskyblue4',command=self.update)
        self.btn_att.place(x=690,y=540)

        self.tBox = Text(self.master,width=60,height=18)
        self.tBox.place(x=710,y=150)
        self.tBox.insert(END,'Ultimo cadastro com o ID: ' + str(id))

    def search(self,*args,**kwargs):
        sql = "SELECT * FROM inventory where id=?"
        result = c.execute(sql,self.id_e.get())
        for r in result:
            self.n1 = r[1] 
            self.n2 = r[2]
            self.n3 = r[3]
            self.n4 = r[4]
            self.n5 = r[5]
            self.n6 = r[6]
            self.n7 = r[7]
            self.n8 = r[8]
            self.n9 = r[9]
            
        conn.commit()

        self.name_e.delete(0,END)
        self.name_e.insert(0,str(self.n1))

        self.stock_e.delete(0,END)
        self.stock_e.insert(0,str(self.n2))

        self.cp_e.delete(0,END)
        self.cp_e.insert(0,str(self.n3))

        self.sp_e.delete(0,END)
        self.sp_e.insert(0,str(self.n4))

        self.vendor_e.delete(0,END)
        self.vendor_e.insert(0,str(self.n8))

        self.vendor_phone_e.delete(0,END)
        self.vendor_phone_e.insert(0,str(self.n9))

        self.totalcp_e.delete(0,END)
        self.totalcp_e.insert(0,str(self.n5))

        self.totalsp_e.delete(0,END)
        self.totalsp_e.insert(0,str(self.n6))

    def update(self,*args,**kwargs):
        self.u1 = self.name_e.get()
        self.u2 = self.stock_e.get()
        self.u3 = self.cp_e.get()
        self.u4 = self.sp_e.get()
        self.u5 = (float(self.u3) * float(self.u2))
        self.u6 = (float(self.u4) * float(self.u2))
        self.u7 = self.vendor_e.get()
        self.u8 = self.vendor_phone_e.get()

        sql = "UPDATE inventory set name=?,stock=?,cp=?,sp=?,totalcp=?,totalsp=?,vendor=?,vendor_phoneno=? WHERE id=?"
        c.execute(sql,(self.u1,self.u2,self.u3,self.u4,self.u5,self.u6, self.u7, self.u8,self.id_e.get()))
        conn.commit()

        #tkinter.messagebox.showinfo('Sistema de Vendas','Cadastro atualizado com sucesso!')

root = Tk()
root.geometry('1200x600')
root.resizable(False,False)
root.title('Atualizacao de Produtos - Maria Luiza Armini Correa')
DB = DataBase(root)

root.mainloop()