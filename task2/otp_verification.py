import random
import smtplib
from tkinter import *


def generateOTP():
    randomCode = ''.join(str(random.randint(0, 9)) for i in range(6))
    return randomCode

sender = 'vidyachaudhari231@gmail.com'
password = 'jfmn vumr doji wvde'
code = generateOTP()


def Sender():
    receiver = receiverMail.get()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    Email(receiver, server)


def Email(receiver, server):
    msg = 'Hello! \n This is your OTP is ' + code
    server.sendmail(sender, receiver, msg)
    server.quit()


def checkOTP():
    if code == codeEntry.get():
        accept = Label(otp_verify, text='OTP verified Successfully!', fg='green', font=('Arial', 16))
        accept.place(x=230, y=350)
    else:
        refuse = Label(otp_verify, text='Please Enter Correct OTP!', fg='red', font=('Arial', 16))
        refuse.place(x=230, y=350)


otp_verify = Tk()
otp_verify.title('OTP Verification')
otp_verify.geometry('750x400')

emailMsg = Label(otp_verify, text="E-Mail", justify=LEFT, font=("Arial", 16), bd=3, bg="black",fg="white")
emailMsg.place(x=15, y=40)

receiverMail = Entry(otp_verify, text='mail.gmail.com', width=35, font=("Arial", 20), borderwidth=0)
receiverMail.place(x=100, y=40)
receiverM = StringVar()

sendOTP = Button(otp_verify, text="Send OTP", width=8, height=1, font=("Arial", 16), borderwidth=0, fg="white", bg="black",bd=3,command=Sender)
sendOTP.place(x=280, y=100)

otpMsg = Label(otp_verify, text="OTP", font=('Arial', 16), bg="black", fg="white")
otpMsg.place(x=15, y=210)

codeEntry = Entry(otp_verify, width=6, font=("Arial", 20), borderwidth=0)
codeEntry.place(x=100, y=210)

verify = Button(otp_verify, text="Verify OTP", width=8, height=1, font=("Arial", 16), borderwidth=0, fg="white", bg="black",bd=3,
                command=checkOTP)
verify.place(x=280, y=280)

otp_verify.mainloop()
