import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
import numpy as np2

def ClickMe(name):
    B1.configure(text='Ihave been clicked    '+name.get())


##############################################
def Quit():
    win.quit()
    win.destroy()
    exit()
###############################################

if __name__ == '__main__':

#def Main():
    win=tk.Tk()
    win.title("First GUI")

    #Creating a tab control
    tabControl=ttk.Notebook(win)
    tab1=ttk.Frame(tabControl)
    tab2=ttk.Frame(tabControl)
    tabControl.add(tab1, text="Tab1")
    tabControl.add(tab2,text='tab2')
    tabControl.pack(fill='both')

    LF2=ttk.Labelframe(tab2,text=" Container Frame")
    LF2.grid(column=0,row=0, padx=10, pady=20)

    #This is a LabelFrame upon which the other widgets are located. It is itself located on the main window "win"
    LF1=ttk.Labelframe(tab1,text=" Container Frame")
    LF1.grid(column=0,row=0, padx=10, pady=20)

    #Preventing from resizeable
    ##win.resizable(0,0)

    #Creating a label
    L1=ttk.Label(LF1,text="Name").grid(column=0,row=0)

    #Creating a botton
    B1=ttk.Button(LF1,text="Enter", command= lambda : ClickMe(name))
    B1.grid(column=1, row=1)

    #Creating an entry
    name=tk.StringVar()
    E1=ttk.Entry(LF1,width=12,textvariable=name)
    E1.grid(column=0,row=1)

    #Creating combo box
    L2=tk.Label(LF1,text="Number of cores")
    L2.grid(column=0, row=2)

    CO1=ttk.Combobox(LF1,width=12)
    CO1.grid(column=0,row=3)
    CO1['values']=(1,2,3,4)
    CO1.current(1)

    #Creating check bottom
    Chb1=tk.Checkbutton(LF1, text='Disabled', state='disabled')
    Chb1.grid(column=0,row=4, sticky=tk.W)
    Chb1.select()

    tkV=tk.IntVar()
    Chb2=tk.Checkbutton(LF1, text='Enabled', variable=tkV)
    Chb2.grid(column=1,row=4, sticky=tk.W)
    Chb2.select()
    print" The value of check bottom is:", tkV.get()

    #Creating Scroll text widgets
    scrolW=30
    scrolH=3

    Scr1=scrolledtext.ScrolledText(LF1,width=scrolW, height=scrolH)
    Scr1.grid(column=0,row=5)


   #LbalFrame widget to get much more control over GUI design, it is better than grid layout manager
    labesframe=ttk.Labelframe(LF1, text="Labels in a frame")
    labesframe.grid(column=0, row=7,padx=20, pady=40)  #Ussing Padding to add space around the widget

    ttk.Label(labesframe,text="Label1").grid(column=0,row=0)
    ttk.Label(labesframe,text="Label2").grid(column=0,row=1)
    ttk.Label(labesframe,text="Label3").grid(column=0,row=2)

    #Add space around each child of LabelFrame widget as follow:
    for child in labesframe.winfo_children():
        print "the name of child:",child
        child.grid_configure(padx=8,pady=4)

    #Creating Menu bar for the main window
    menubar=tk.Menu(win)
    win.configure(menu=menubar)

    #Creating an object from "Menu" class which is child of "menubar" object created above
    fileMenu=tk.Menu(menubar, tearoff=0)
    fileMenu.add_command(label="Open")
    #Adding separating line
    fileMenu.add_separator()
    fileMenu.add_command(label="New")
    fileMenu.add_command(label="Exit", command=Quit)
    menubar.add_cascade(label="File", menu=fileMenu)

    #Creating second Menu inside the Menu bar
    helpMenu=tk.Menu(menubar, tearoff=0)
    helpMenu.add_command(label="About")
    menubar.add_cascade(label="Help", menu=helpMenu)



    win.mainloop()



