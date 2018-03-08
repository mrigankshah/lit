from Tkinter import *

master = Tk()
def show_entry_fields():
	a = e1.get()
	b = e2.get()
	username='Mrigank'
	password='potty'
	if a==username :
		if b==password :  
			print("You're logged in\n")
			master.destroy()
		else :
			print("Wrong password")
	else :
		print("Wrong username")


Label(master, text="First Name").grid(row=0)
Label(master, text="Password").grid(row=1)

e1 = Entry(master)
e2 = Entry(master, show="*")

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Login', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
master.quit
mainloop( )


