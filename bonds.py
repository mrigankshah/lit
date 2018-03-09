from Tkinter import *
import os
import runpy

bonds=Tk()

def open_home():
  bonds.destroy()
  runpy.run_path("home.py")

def open_mf():
   bonds.destroy()
   runpy.run_path("mf.py")
   
def open_re():
   bonds.destroy()
   runpy.run_path("re.py")
   
def open_gold():
   bonds.destroy()
   runpy.run_path("gold.py")
   
def open_cash():
   bonds.destroy()
   runpy.run_path("cash.py")
   
def open_stocks():
   bonds.destroy()
   runpy.run_path("stocks.py")

bonds.title("LIT")
bonds.geometry("1920x1080")

l1=Label(bonds,text=" ", font="Lato 20").pack()
l2=Label(bonds, text="L O N G - T E R M   I N V E S T M E N T   T R A C K E R", font="Lato 30").pack()

top = Frame(bonds)
top.pack(side=TOP)

l3=Label(bonds,text="Bonds", font="Lato 20").pack()

mainoptions = ['Home', 'Stocks', 'Mutual Funds','Real estate','Gold', 'Cash', 'Bonds']
i=0

l1 = Button(bonds,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command= open_home)
l1.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l2 = Button(bonds,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command= open_stocks)
l2.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l3 = Button(bonds,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command=open_mf)
l3.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l4 = Button(bonds,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command=open_re)
l4.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l5 = Button(bonds,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command=open_gold)
l5.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l6 = Button(bonds,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command=open_cash)
l6.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l7 = Button(bonds,text=mainoptions[i], font="Lato 20",fg='White',bg='Black')
l7.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1
mainloop()

