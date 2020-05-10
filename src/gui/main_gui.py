'''
Main program for the application iO Pipline-Recherche.

https://www.python-kurs.eu/tkinter_menus.php
'''

from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import db_simplesearch

global root

def NewSimpleSearch():
    print("New simple search!")
    db_simplesearch.show_db(root)

def NewAdvancedSearch():
    print("New advanced search!")
def OpenFile():
    name = askopenfilename()
    print(name)
def SaveAsFile():
    name = asksaveasfilename()
    print(name)
def NewNotebook():
    name = askopenfilename()
    print(name)
def OpenNotebook():
    name = askopenfilename()
    print(name)
def SaveNotebook():
    name = askopenfilename()
    print(name)
def SaveAsNotebook():
    name = askopenfilename()
    print(name)
def About():
    print ("This is a simple example of a menu")
    
root = Tk()
root.title("iO Pipline-Recherche")
root.geometry('800x600')
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="Search", menu=filemenu)
filemenu.add_command(label="New simple search", command=NewSimpleSearch)
filemenu.add_command(label="New advanced search", command=NewAdvancedSearch)
filemenu.add_command(label="Open search...", command=OpenFile)
filemenu.add_command(label="Save search as...", command=SaveAsFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

notemenu = Menu(menu)
menu.add_cascade(label="Notes", menu=notemenu)
notemenu.add_command(label="New notebook", command=NewNotebook)
notemenu.add_command(label="Save notebook", command=SaveNotebook)
notemenu.add_command(label="Save notebook as...", command=SaveAsNotebook)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

mainloop()