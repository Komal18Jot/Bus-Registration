import pymysql as pm
backend = pm.connect(host= "localhost",user ="root",passwd ="C-suite1")
db=backend.cursor()
db.execute("create database if not exists busregister")
db.execute("use busregister")
db.execute("create table if not exists bus(BusNo int(4) primary key,origin varchar(255),\
           dest varchar(255),Rate int(5),KM int(5))")
backend.commit()
 
from tkinter import *
root=Tk()
root.geometry("700x600")
root.title("Bus Registry")
root.resizable(0,0)
root.configure(background="Blue")
 
def reg():
   values=(busno.get(),origin.get(),dest.get(),rate.get(),km.get())
   db.execute("insert into bus values(%s,%s,%s,%s,%s)",values)
   backend.commit()
 
busno=StringVar(root)
origin=StringVar(root)
dest=StringVar(root)
rate=StringVar(root)
km=StringVar(root)
 
label=Label(root, text="Bus Resgistration", bg="#DBF3FA",fg="purple", font=("calibri 50 underline"))
label1=Label(root, text="Bus Number :",bg="silver",fg="Black", font=("Calibri 27 bold"))
label2=Label(root, text="Origin :",bg="silver",fg="Black", font=("Calibri 27 bold"))
label3=Label(root, text="Destination :",bg="silver",fg="Black", font=("Calibri 27 bold"))
label4=Label(root, text="Rate :",bg="silver",fg="Black", font=("Calibri 27 bold"))
label5=Label(root, text="Kilometers :",bg="silver",fg="Black", font=("Calibri 27 bold"))
 
ent1=Entry(root, textvariable=busno)
ent2=Entry(root, textvariable=origin)
ent3=Entry(root, textvariable=dest)
ent4=Entry(root, textvariable=rate)
ent5=Entry(root, textvariable=km)
 
b1=Button(root,text="Register", height=1, width=20,bg="#A44801", borderwidth=4,command=reg,font="Calibri 35 bold")
 
label.place(x=80, y=0)
label1.place(x=25, y=150)
label2.place(x=25, y=200)
label3.place(x=25, y=250)
label4.place(x=25, y=300)
label5.place(x=25, y=350)
 
ent1.place(x=235, y=150, height=40, width = 450)
ent2.place(x=235, y=200, height=40, width = 450)
ent3.place(x=235, y=250, height=40, width = 450)
ent4.place(x=235, y=300, height=40, width = 450)
ent5.place(x=235, y=350, height=40, width = 450)
 
b1.place(x=100,y=450)
root.mainloop()
