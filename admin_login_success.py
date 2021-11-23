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
        
        
        menu = Menu(master)
        master.config(menu=menu)

        home=Menu(menu)
        menu.add_cascade(label='Home',menu=home)
        home.add_command(label='Terms of Use',command=self.terms_of_use)
        home.add_separator()

        
        submenu = Menu(menu)
        menu.add_cascade(label='Help!!!', menu=submenu)
        submenu.add_command(label='Contact Us!',command=self.contact_us)
        submenu.add_command(label='FAQs', command=self.faq)
        submenu.add_command(label='Report Infringement', command=self.report_infringement)
        submenu.add_separator()

        about_us=Menu(menu)
        menu.add_cascade(label='About Us',menu=about_us)
        about_us.add_command(label='About us',command=self.about_us)
        about_us.add_separator()


        exit_button=Menu(menu)
        menu.add_cascade(label='Exit',menu=exit_button)
        exit_button.add_command(label='Exit',command=root.destroy)
        exit_button.add_command(label='Minimize',command=self.minimize)
        
    def about_us(self):
        top = Toplevel()
        top.geometry("200x200")
        top.title("About Us")
        msg = Message(top, text='This Employee management system will help you to manage '
                                'your employees data easily')
        msg.grid(row=0, column=15)
        button = Button(top, text="Dismiss", command=top.destroy)
        button.grid(row=4, column=15)

        ##declare a message box

    def faq(self):
        ##message box indicating faqs
        print('he')

    def report_infringement(self):
        ##message box
        messagebox.showerror("Report Infringement","If found any infringement please mail us at 19bcs1557@gmail.com or call us at 9145879325")
       

    def terms_of_use(self):
        string_terms="Privacy Statement Welcome EMS. By accessing or using this Software, you (User or you) agree to comply with the terms and conditions governing your use of any areas of the EMS.com web Software (the Software) as set forth below. USE OF Software Please read the Terms of Use (Terms) carefully before you start using the Software. By using the Software you accept and agree to be bound and abide by these Terms of Use and our Privacy Policy, found at incorporated herein by reference. If you do not agree to these Terms of Use or the Privacy Policy, you must not access or use the Software. This Software or any portion of this Software may not be reproduced, duplicated, copied, sold, resold, or otherwise exploited for any commercial purpose except as expressly permitted by EMS.com, Inc. EMS.com, Inc. and its affiliates reserve the right to refuse service, terminate accounts, and/or cancel orders in its discretion, including, without limitation, if EMS.com, Inc. believes that User conduct violates applicable law or is harmful to the interests of EMS.com, Inc. or its affiliates."
        dialog=Toplevel()
        dialog.geometry("400x400")
        dialog.title("Terms of Use")
        message=Message(dialog,text=string_terms)
        message.grid(row=0,column=0)
        button = Button(dialog, text="Close", command=dialog.destroy)
        button.grid(row=4, column=0)

    def contact_us(self):
        messagebox.showerror("Contact us ","In case of any dicrepancy or misbehaving of software Please contact us immediately.You can mail us at 19bcs1557@gmail.com or call us at 9145879325 ")

    def minimize(self):
        print('minimize the window')
        root.wm_state("iconic")

def upload_attendance():
    print('upload attendance')
    import attendance_upload
    call('python3 attendance.py', shell=True)
        
def add():
    print('add ')
    import ers_add
    call('python3 ers_add.py', shell=True)
    
def calcpayroll():
    print('calculate payroll ')
    import Employee_pay
    call('python3 Employee_pay.py', shell=True)

def send_message():
    import Send_message
    call('python3 Send_message.py', shell=True)

root=Tk()
f=Frame(root)
frame1=Frame(root)
frame2=Frame(root)
frame3=Frame(root)
label1=Label(root,text="Admin Home")
label1.config(font=('Italic',16,'bold'), justify=CENTER, background="Orange",fg="Yellow", anchor="center")
label1.pack(fill=X)

label2=Label(f,text="Select an action: ",font=('bold',12), background="Black", fg="White")
label2.pack(fill=X)
button1=Button(f,text="Add/Delete/Search", background="Brown", fg="White", command=add, width=8)
button1.pack(fill=X)
button2=Button(f,text="Upload Attendance", background="Brown", fg="white", command=upload_attendance, width=8)
button2.pack(fill=X)
button3=Button(f,text="Send Message", background="Brown", fg="white", command=send_message, width=8)
button3.pack(fill=X)
button4=Button(f,text="Calculate Payroll", background="Brown", fg="White", command=calcpayroll, width=8)
button4.pack(fill=X)
button4=Button(f,text="Close", background="Brown", fg="White", width=8, command=root.destroy)
button4.pack(fill=X)

f.configure(background="Black")
f.pack()
admin_login_home=Home(root)
root.wm_geometry("300x300")
root.configure(background = "black")
root.title("Admin Login")
root.mainloop()
