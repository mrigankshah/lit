from Tkinter import *
import os
import runpy

cash=Tk()

def open_home():
  cash.destroy()
  runpy.run_path("home.py")

def open_mf():
   cash.destroy()
   runpy.run_path("mf.py")
   
def open_re():
   cash.destroy()
   runpy.run_path("re.py")
   
def open_gold():
   cash.destroy()
   runpy.run_path("gold.py")
   
def open_stocks():
   cash.destroy()
   runpy.run_path("stocks.py")
   
def open_bonds():
   cash.destroy()
   runpy.run_path("bonds.py")

cash.title("LIT")
cash.geometry("1920x1080")

l1=Label(cash,text=" ", font="Lato 20").pack()
l2=Label(cash, text="L O N G - T E R M   I N V E S T M E N T   T R A C K E R", font="Lato 30").pack()

top = Frame(cash)
top.pack(side=TOP)

l3=Label(cash,text="Cash", font="Lato 20").pack()

mainoptions = ['Home', 'Stocks', 'Mutual Funds','Real estate','Gold', 'Cash', 'Bonds']
i=0

l1 = Button(cash,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command= open_home)
l1.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l2 = Button(cash,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command= open_stocks)
l2.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l3 = Button(cash,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command=open_mf)
l3.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l4 = Button(cash,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command=open_re)
l4.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l5 = Button(cash,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command=open_gold)
l5.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l6 = Button(cash,text=mainoptions[i], font="Lato 20",fg='White',bg='Black')
l6.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l7 = Button(cash,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command=open_bonds)
l7.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1
mainloop()

