import tkinter
from tkinter.ttk import Combobox
import DB
import listener


def window():
    def click():
        link = DB.get_link()

        text.set(listener.get_valutes_value(link, listener.get_valutes_char_code(link, combo.get())))
        lbl.configure(textvariable=text)
        print(combo.get())

    window = tkinter.Tk()
    window.title('valute')
    window.geometry('400x250')

    text = tkinter.StringVar()
    text.set('Choose valute')

    lbl = tkinter.Label(window, textvariable=text)
    lbl.grid(column=0, row=2)

    btn = tkinter.Button(window, text="Get", command=click)
    btn.grid(column=0, row=1)

    combo = Combobox(window, values=listener.get_valutes_name(DB.link))
    combo.current(1)
    combo.grid(column=0, row=0)


    window.mainloop()