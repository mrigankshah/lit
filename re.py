from Tkinter import *
import os
import runpy

re=Tk()

def open_home():
  re.destroy()
  runpy.run_path("home.py")

def open_mf():
   re.destroy()
   runpy.run_path("stocks.py")
   
def open_stocks():
   re.destroy()
   runpy.run_path("stocks.py")
   
def open_gold():
   re.destroy()
   runpy.run_path("gold.py")
   
def open_cash():
   re.destroy()
   runpy.run_path("cash.py")
   
def open_bonds():
   re.destroy()
   runpy.run_path("bonds.py")

re.title("LIT")
re.geometry("1920x1080")

l1=Label(re,text=" ", font="Lato 20").pack()
l2=Label(re, text="L O N G - T E R M   I N V E S T M E N T   T R A C K E R", font="Lato 30").pack()

top = Frame(re)
top.pack(side=TOP)

l3=Label(re,text="Real Estate", font="Lato 20").pack()

mainoptions = ['Home', 'Stocks', 'Mutual Funds','Real estate','Gold', 'Cash', 'Bonds']
i=0

l1 = Button(re,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command= open_home)
l1.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l2 = Button(re,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command=open_stocks)
l2.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l3 = Button(re,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command=open_mf)
l3.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l4 = Button(re,text=mainoptions[i], font="Lato 20",fg='White',bg='Black')
l4.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l5 = Button(re,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command=open_gold)
l5.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l6 = Button(re,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command=open_cash)
l6.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1

l7 = Button(re,text=mainoptions[i], font="Lato 20",fg='White',bg='Black', command=open_bonds)
l7.place(x = 0, y = 200 + i*51, width=200, height=50)
i+=1
mainloop()

