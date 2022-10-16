import tkinter
from tkinter.ttk import Combobox



def window():
    def click():
        print('Hello')
        

    window = tkinter.Tk()
    window.title('video downloader')
    window.geometry('450x250')

    linkVideo = tkinter.StringVar()
    linkVideo.set('Link on video:')

    pathSave = tkinter.StringVar()
    pathSave.set('Path to save:')

    lblLink = tkinter.Label(window, textvariable=linkVideo)
    lblLink.grid(column=0, row=0)

    lblPathSave = tkinter.Label(window, textvariable=pathSave)
    lblPathSave.grid(column=0, row=1)

    btn = tkinter.Button(window, text="Download", command=click)
    btn.grid(column=2, row=1)

    entryLink = tkinter.Entry(window, width=50)
    entryLink.grid(column=1, row=0)

    entryPathSave = tkinter.Entry(window, width=50)
    entryPathSave.grid(column=1, row=1)


    window.mainloop()