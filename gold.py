from Tkinter import *
import os
import runpy

gold=Tk()

def open_home():
  gold.destroy()
  runpy.run_path("home.py")

def open_mf():
   gold.destroy()
   runpy.run_path("mf.py")
   
def open_re():
   gold.destroy()
   runpy.run_path("re.py")
   
def open_stocks():
   gold.destroy()
   runpy.run_path("stocks.py")
   
def open_cash():
   gold.destroy()
   runpy.run_path("cash.py")
   
def open_bonds():
   gold.destroy()
   runpy.run_path("bonds.py")

gold.title("LIT")
gold.geometry("1920x1080")

l1=Label(gold,text=" ", font="Lato 20").pack()
l2=Label(gold, text="L O N G - T E R M   I N V E S T M E N T   T R A C K E R", font="Lato 30").pack()

top = Frame(gold)
top.pack(side=TOP)

l3=Label(gold,text="Gold", font="Lato 20").pack()

mainoptions = ['Home', 'Stocks', 'Mutual Funds','Real estate','Gold', 'Cash', 'Bonds']
i=0

l1 = Button(gold,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command= open_home)
l1.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l2 = Button(gold,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command= open_stocks)
l2.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l3 = Button(gold,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command=open_mf)
l3.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l4 = Button(gold,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command=open_re)
l4.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l5 = Button(gold,text=mainoptions[i], font="Lato 20",fg='White',bg='Black')
l5.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l6 = Button(gold,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command=open_cash)
l6.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l7 = Button(gold,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command=open_bonds)
l7.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1
mainloop()

