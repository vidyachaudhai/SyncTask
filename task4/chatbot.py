from tkinter import *

root = Tk()
root.configure(background="black")

def sendMsg():
    send = "You-> " + var1.get()
    txt.insert(END,"\n"+send)

    if(var1.get()=="Hi"):
        txt.insert(END,"\n"+"Jemmy -> Hi, HOw can I help you?")
    elif(var1.get()=="how are you?"):
        txt.insert(END,"\n"+"Jemmy -> I am good.")
    elif(var1.get()=="what is your name"):
        txt.insert(END,"\n"+"Jemmy -> I am Jemmy")
    elif(var1.get()=="Okay"):
        txt.insert(END,"\n"+"Okay, Thanks!")
    else:
        txt.insert(END,"\n"+"Sorry, I did,t get you.")

    var1.delete(0,END)
txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)
var1 = Entry(root,width=100)
send = Button(root, text = "SEND", command=sendMsg).grid(row=1,column=1)
var1.grid(row=1,column=0)
root.title("Chatnot")
root.mainloop()
        
