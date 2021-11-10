import tkinter
from tkinter import  *

import pyodbc
import pandas as pd
from functions import *

window = Tk()
window.title("test")
window.geometry("650x600")
window.configure(background = "BLACK")


#mainframe = Frame(window)

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DVLN2DDBS01\EC;'
                      'Database=IAFF;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()


list_of_awards = cursor.execute('SELECT DISTINCT festivalcode from dbo.ArchiveEntryData')

results = [row for row in cursor.fetchall()]
appearing_results = flatten(results)
appearing_results.insert (0, "All")

print(type (appearing_results), appearing_results)
#in order to
#cursor.execute("SELECT DISTINCT interesting stuff(countries, companies etc)")
awards_selected = StringVar(window)

w = OptionMenu(window, awards_selected, *appearing_results)
awards = StringVar()
awards.set("All")

print("prin kalesoume to change dropdown")
awards = tkinter.Button(window, command = lambda change_dropdown(awards, awards_selected))
w.pack(side = LEFT)
window.mainloop()



