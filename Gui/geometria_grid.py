import tkinter
from tkinter import ttk

window=tkinter.Tk()
window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=3)
#### User data ####
user_label=ttk.Label(window, text='Usr name:')
user_label.grid(column=0,row=0,sticky=tkinter.W,padx=5,pady=5)

user_entry=ttk.Entry(window)
user_entry.grid(column=1,row=0,sticky=tkinter.E,padx=5,pady=5)
#### User password ####
passwd_label=ttk.Label(window, text='Password:')
passwd_label.grid(column=0,row=1,sticky=tkinter.W,padx=5,pady=5)

passwd_entry=ttk.Entry(window, show='*')
passwd_entry.grid(column=1,row=1,sticky=tkinter.E,padx=5,pady=5)
#### button login ####
login_button=ttk.Button(window,text='loggin')
login_button.grid(column=1,row=2,sticky=tkinter.W,padx=5,pady   =5)
login_button=ttk.Button(window,text='loggin1')
login_button.grid(column=0,row=2,sticky=tkinter.E,padx=5,pady=5)
login_button=ttk.Button(window,text='loggin2')
login_button.grid(column=2,row=2,sticky=tkinter.E,padx=5,pady=5)


window.mainloop()