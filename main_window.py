from parser import sort_dict

# lib import
from tkinter import *
from tkinter.ttk import *

# main window
window = Tk()

# settings
window.title("LoopermanParserUI")
window.geometry("800x600")
window.resizable(False, False)
window["background"] = "#CCCCCC"

# #find_entry
# find_entry = Entry(background="#FFFFFF",
#                    foreground="black",
#                    font=("Consolas", 16))
# find_entry.pack(anchor=CENTER, padx=6, pady=6)

# hello_label
hello_label = Label(text="Hello, User!",
                    background="#FFFFFF",
                    foreground="black",
                    font=("Consolas", 16))

hello_label.pack(padx=6,
                 pady=6,
                 fill="x")

# sort_combobox
for value in sort_dict.values():
    if len(value) > 0:
        sort_box = Combobox(values=value,
                            state="readonly",
                            font=("Consolas", 16))
        sort_box.current(0)
        sort_box.pack(anchor=NW,
                      padx=6,
                      pady=6)

# parse_button
parse_button = Button(text="Parse It!", width=100)
parse_button.pack(
    anchor=NW,
    padx=100,
    pady=60)

window.mainloop()
