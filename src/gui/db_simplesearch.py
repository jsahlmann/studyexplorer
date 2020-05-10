'''
Simple search:

https://clinicaltrials.gov/ct2/results?
recrs= (recruiting and not yet recruiting studies)
cond=alzheimer
term=acetylcholinesteraseinhibitor
cntry=DE
state=
city=
dist=

https://www.python-kurs.eu/tkinter_entry_widgets.php
'''
from tkinter import Frame
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Tk
from tkinter import Toplevel
from tkinter import TOP, LEFT, RIGHT, YES, X


fields = 'Status', 'Condition or disease', 'Other terms', 'Country'

def fetch(entries):
   for entry in entries:
      field = entry[0]
      text  = entry[1].get()
      print('%s: "%s"' % (field, text)) 

def cancel():
   print("cancel")

def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=20, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
   return entries

def show_db(root):
   dbox = Toplevel(root)
   dbox.transient(root)
   dbox.geometry('640x480')
   dbox.grab_set()
   dbox.title("Simple search")
   ents = makeform(dbox, fields)
   dbox.bind('<Return>', (lambda event, e=ents: fetch(e)))   
   b1 = Button(dbox, text='Search', command=(lambda e=ents: fetch(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(dbox, text='Cancel', command=(lambda e=ents: cancel()))
   b2.pack(side=LEFT, padx=5, pady=5)
   print(type(ents))
   return ents

if __name__ == '__main__':
   root = Tk()
   root.title("Simple search")
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
   b1 = Button(root, text='Search',
          command=(lambda e=ents: fetch(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(root, text='Cancel', command=root.quit)
   b2.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()