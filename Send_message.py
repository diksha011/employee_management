from tkinter import *
from tkinter import  messagebox
import sys
import os
import signal
import time
from subprocess import  call
import  xlrd
import xlwt
import sqlite3
import datetime

class Home():
    def __init__(self,master):
        self.date = datetime.date.today()
        

        #message box code


        message_label=Label(master,text="   Message to Employees   ",font=("Courier", 30),background="Orange",fg="Yellow")
        message_label.grid(row=0,column=0)
        self.message_variable=StringVar()
        large_font = ('Verdana', 24)
        message_entry = Entry(master, textvariable=self.message_variable, bd=10, font=large_font)
        message_entry.grid(row=4,column=0)
        message_submit=Button(master,text='Send to all the Employees',font=("Courier", 18),command=self.send_message,background="Brown", fg="White")
        message_submit.grid(row=8,column=0)


    def send_message(self):
        messagebox.showinfo("Message Sent","Your Message has been Sent")
        message_value=self.message_variable.get()
        date=self.date
        try:
            conn = sqlite3.connect('portal_final.db')
            message_insert=conn.cursor()
            message_insert.execute("INSERT into message_alerts(message,date) values(?,?) ",(message_value,date))
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error","Internal Servor Error Occured")




root=Tk()
admin_login_home=Home(root)
root.wm_geometry("600x250")
root.configure(background = "black")
root.title("Admin Login - Send message")
root.mainloop()
