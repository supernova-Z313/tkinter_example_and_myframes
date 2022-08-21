import tkinter
from tkinter import Frame, IntVar, Menu, Tk, Variable, Widget
from tkinter import ttk
from tkinter.constants import ACTIVE, DISABLED, NORMAL, SCROLL 
from tkinter import scrolledtext
from tkinter import Menu
import time

mygui = tkinter.Tk()
mygui.title("beautiful gui ")
mygui.resizable(True, True)

# tabControl = ttk.Notebook(mygui)
# tab1 = ttk.Frame(tabControl)
# tabControl.add(tab1, text='Tab 1')
# tabControl.pack(expand=1, fill="both")

a = ttk.Label(mygui,text = "good for eating")
a.grid(column = 0, row = 0)
mygui.geometry("500x300")
# ===========================================
# def click_me():
#     bb.configure(text = "fuck u")
#     a.configure(foreground = "red")
#     a.configure(text = "bad")
    
# bb = ttk.Button(mygui, text = " for start fuck " , command = click_me)
# bb.grid(column = 1, row = 1)
# ===========================================

def mmd():
    global v, vv, vvv
    if vvv == 0:
        pass
    elif vvv == 1:
        c = ttk.Label(mygui, text = v + vv)
        c.grid(column = 1, row = 2)
        bb.configure(state='disabled')
        check1.configure(state='disabled')
        name_entered.configure(state='disabled')
        # name_entered.destroy()
        number_chosen.configure(state='disabled')

def click_me():
    global v, vv, vvv, vi
    v = name.get()
    vv = number.get()
    vvv = mig.get()
    bmm = texts.get("1.0", tkinter.END)
    a2 = ttk.Label(mygui, text = "we save your text and your sorakh was hacked khkhkhkh:  \n" + bmm)
    a2.grid(column = 0, row = 9, columnspan=3)
    bb.configure(text = " clicked ")
    a.configure(foreground = "red")
    a.configure(text = "bad")
    colcall()
    mmd()

bb = ttk.Button(mygui, text = " for start fuck " , command = click_me ) 
bb.grid(column = 1, row = 1, sticky = tkinter.E)

number = tkinter.StringVar()
# lis = [1,2]
number_chosen = ttk.Combobox(mygui, width=12, textvariable=number)# , values= lis , state='readonly'
listim = [1,2,3,4,5,6,7,8,9,10]
number_chosen['value'] = (listim)
number_chosen.grid(column = 0, row = 2)
number_chosen.current(0)


name = tkinter.StringVar()
name_entered = ttk.Entry(mygui, width=12, textvariable=name)
name_entered.grid(column=0, row=1)
name_entered.focus()

mig = tkinter.IntVar()
check1 = tkinter.Checkbutton(mygui, text = "migoly? ", variable = mig) # state = "normal","active", "disable"
check1.select()
check1.grid(column = 0, row = 5, sticky = tkinter.W)# , sticky = tkinter.* -><- ...


coler = "#03fc77" # hex cod
def colcall():
    mame = bib.get()
    if mame == 1:
        mygui.configure(background = coler)
        col1.configure(background="Red")

bib = IntVar()
col1 = tkinter.Radiobutton(mygui, text = 'ziba', variable = bib, value = 1)#  , command = colcall
col1.grid(column = 0, row = 6, columnspan = 5, sticky = tkinter.W)
col1.select()

texts = scrolledtext.ScrolledText(mygui, width = 30, height = 7, wrap = tkinter.WORD)
texts.grid(column= 0, row = 8, columnspan = 3)
# column=start, columnspan=finish, ..., rowspan

frames1 = ttk.LabelFrame(mygui, text = "result", border = 2)
frames1.grid(column = 2, row = 4)

kirt = tkinter.Label(frames1, background = "Gold", height = 1, width = 2, relief = "solid", bd= 2)
# , border = bd ,relief = [solid,sunken,groove,ridge,flat,raised],borderwidth = 3
kirt.grid(column = 0, row = 0)
kirt1 = tkinter.Label(frames1, text = "nmigoly?")
kirt1.grid(column = 1, row = 0)

mamebar = Menu(mygui)
mygui.config(menu=mamebar)

def quit():
    mygui.quit()
    mygui.destroy()
    exit()


file_menu = Menu(mamebar, tearoff=0)# clean the ---- from menu
file_menu.add_command(label="New")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

file_menu2 = Menu(mamebar, tearoff=0)
file_menu2.add_command(label="about")

mamebar.add_cascade(label="File", menu=file_menu)
mamebar.add_cascade(label="more", menu=file_menu2)

ssss = ttk.Style()
ssss.theme_use('default')
ssss.configure('TNotebook.Tab', background="green3")

mygui.configure(background = "#bea9d4")
mygui.mainloop()

# for i in range(100):
#     time.sleep(0.25)
#     print(i)