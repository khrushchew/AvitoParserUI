from parser import sort_dict


#lib import
from tkinter import *
from tkinter.ttk import *

#main window
window = Tk()

#settings
window.title("LoopermanParserUI")
window.geometry("800x600")
window.resizable(False, False)
window["background"] = "#CCCCCC"

#find_entry
find_entry = Entry(background="#FFFFFF",
                   foreground="black",
                   font=("Consolas", 16))
find_entry.pack(anchor=CENTER, padx=6, pady=6)

#sort_combobox
for value in sort_dict.values():
    if len(value) > 0:
        sort_box = Combobox(textvariable=StringVar(value=value[0]), values=value, state="readonly")
        sort_box.pack(anchor=NW, padx=6, pady=6)
window.mainloop()
