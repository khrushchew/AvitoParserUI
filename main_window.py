from parser import take_for_sort_box

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
                   foreground="white",
                   font=("Consolas", 16))
find_entry.pack(anchor=CENTER, padx=6, pady=6)

#sort_combobox
sort_box = Combobox(values=take_for_sort_box())


window.mainloop()
