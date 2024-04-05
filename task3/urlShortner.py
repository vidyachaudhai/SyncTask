
from tkinter import *
import pyshorteners

window = Tk()
window.geometry("400x270")
# window.configure(bg="pink")

#function
def shorten():
    url = var1.get()
    s = pyshorteners.Shortener().tinyurl.short(url)

    var2.insert(END,s)


#lable
Label(window, text="Enter url link ", font=("Arial 16 bold"), bg="black", fg="white").pack(fill=X)

var1 = Entry(window, font=("10"),bd=3,width=40)
var1.pack(pady=30, padx=35)

Button(window, text="Click Me", font=("Arial 12 bold"), bg="Black", fg="white", command=shorten).pack()

var2 = Entry(window, font=("Arial 16 bold"), width=25)
var2.pack(pady=30)

mainloop()