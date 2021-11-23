from tkinter import *
from tkinter import  messagebox
import sys
import os
import signal
import time
from subprocess import  *
from tkinter.scrolledtext import ScrolledText
import sqlite3





def file_previous_close():
    try:
        with open('home_id.txt', 'r') as f:
            lines = f.read().splitlines()
            last_line = lines[-1]
            page=lines[-2]
            if(page!='registration'):
                os.kill(int(last_line),signal.SIGKILL)
    except:
        print('first instance no need to close previous file')

#file_previous_close()

def writing_id():
    file_home_id=open("home_id.txt","w+")
    home_id=os.getpid()
    file_home_id.writelines('registration\n')
    file_home_id.writelines(str(home_id))
    file_home_id.close()
    print('writing id')
    print(home_id)
def write_message_no(number):
    file=open("message.txt","w+")
    file.writelines(number)
    file.close()

def login_details(username,password):
    file=open("login_details.txt","w+")
    file.writelines(username+'\n')
    file.writelines(password)
    file.close()

#writing_id()


class Home():



    def __init__(self,master):




        menu = Menu(master)
        master.config(menu=menu)

        home=Menu(menu)
        menu.add_cascade(label='Home',menu=home)
        home.add_command(label='Take a Tour!!',command=self.take_a_tour)
        home.add_command(label='Terms of Use',command=self.terms_of_use)
        home.add_separator()

        login_option=Menu(menu)
        menu.add_cascade(label='Register and Login',menu=login_option)
        login_option.add_command(label='Login',command=self.login)
        login_option.add_command(label='Admin Login',command=self.admin_login)
        login_option.add_separator()

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

        #can do a prompt to do yes or  no


        exit_button.add_command(label='Minimize',command=self.minimize)
        
    

        ##login frame starts here

        frame = Frame(master)
        self.username = StringVar(master)
        self.password = StringVar()
        self.first_name=StringVar()
        self.last_name = StringVar()
        self.dob=StringVar()
        self.email=StringVar()
        self.mobile_number=StringVar()
        self.dept = StringVar(master)
        self.post = StringVar(master)
        self.address_var=StringVar()
        self.dept.set("Select Dept:")  # default value
        self.post.set("Select Post:")
        


        dep_employee=Label(master,text="Dept:",bg="red",fg="white")
        #for options menu of dept of employee
        w = Label(master,bd = 5, textvariable= self.dept)
        w.pack(padx=15,pady=5)
        
        post_employee=Label(master,text="Post:")
        #for options menu of post of employee
        w1 = Label(master,bd=5,textvariable=self.post)
        w1.pack(padx=15,pady=5)

        employee_first_name=Label(master,text="First Name:",bg="red",fg="white")
        employee_first_name.pack(padx=15,pady=4)
        employee_first_name_entry=Label(master,bd=5,textvariable=self.first_name)
        employee_first_name_entry.pack(padx=24,pady=4)
        
        employee_last_name=Label(master,text="Last Name:",bg="red",fg="white")
        employee_last_name.pack(padx=15,pady=4)
        employee_last_name_entry=Label(master,bd=5,textvariable=self.last_name)
        employee_last_name_entry.pack(padx=24,pady=4)


        Label1 = Label(master, text='Username:',bg="red",fg="white")
        Label1.pack(padx=15, pady=5)
        entry1 = Entry(master, bd=5,textvariable=self.username)
        entry1.pack(padx=15, pady=5)


        email_label=Label(master,text='Email:',bg="red",fg="white")
        email_label.pack(padx=15,pady=6)
        email_entry=Entry(master,bd=5,textvariable=self.email)
        email_entry.pack(padx=15,pady=6)


        mobile_label=Label(master,text="Mobile:",bg="red",fg="white")
        mobile_label.pack(padx=15,pady=7)
        mobile_entry=Entry(master,bd=5,textvariable=self.mobile_number)
        mobile_entry.pack(padx=15,pady=7)

        Label2 = Label(master, text='Password: ',bg="red",fg="white")
        Label2.pack(padx=15, pady=9)
        entry2 = Entry(master,show="*" ,bd=5,textvariable=self.password)
        entry2.pack(padx=15, pady=9)

        address_label=Label(master,text='Address:',bg="red",fg="white")
        address_label.pack(padx=15,pady=10)

        large_font = ('Verdana', 30)
        address_entry=Entry(master,textvariable=self.address_var,bd=10,font=large_font)
        address_entry.pack(padx=15,pady=10)



        btn = Button(frame, text='Register',background="Brown", fg="White", command=self.register_submit)
        btn.pack(side=RIGHT, padx=5)
        frame.pack(padx=100, pady=19)
        
    def admin_login(self):
        import  adminlog
        call('python3 adminlog.py', shell=True)
        

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

    def login(self):
        print('login ')
        import login
        call('python3 login.py', shell=True)

    def report_infringement(self):
        ##message box
        messagebox.showerror("Report Infringement","If found any infringement please mail us at 19bcs1557@gmail.com or call us at 9145879325")



    def take_a_tour(self):
        ##take a tour of the app
        tour_take=Toplevel()
        tour_take.geometry("180x180")
        tour_take.title("Take a Tour")
        message=Message(tour_take,text="Press Register to Register an employee and fill the required details.Then Press Login to Login The Employee.")
        message.grid(row=0,column=1)
        button = Button(tour_take, text="Close", command=tour_take.destroy)
        button.grid(row=4, column=1)

        print('take a tour')

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

    def register_submit(self):
        #self.select_employee_dept=self.dept.get()
        #self.select_employee_post=self.post.get()
        self.username_call=self.username.get()
        #self.first_name_call=self.first_name.get()
        #self.last_name_call=self.last_name.get()
        self.email_call=self.email.get()
        self.mobile_number_call=self.mobile_number.get()
        self.password_call=self.password.get()
        self.address_call=self.address_var.get()
        
        try:
            conn = sqlite3.connect('portal_final.db')
            register_db_object = conn.cursor()
            login_db_object=conn.cursor()
            admin_register_db_object = conn.cursor()
           
        except:
            messagebox.showinfo("Failed", "Can't connect to the server")
            print("cant connect")
            
        try:
            admin_register_db_object.execute('SELECT * from admin_register where id="%s"' % (self.username_call))
            store = admin_register_db_object.fetchall()
            print(store)   
            if(len(store)==0):
                messagebox.showerror("Failed", "NO SUCH EMPLOYEE EXIST ")
                return
                               
            for i in range(0, len(store)):
                #self.username_call = store[i][1]
                self.first_name_call= store[i][1]
                self.first_name.set(self.first_name_call)
                self.last_name_call=store[i][2]
                self.last_name.set(self.last_name_call)
                self.select_employee_dept=store[i][3]
                self.dept.set(self.select_employee_dept)
                self.select_employee_post=store[i][4]
                self.post.set(self.select_employee_post)
           
            register_db_object.execute("INSERT INTO register (firstname,lastname,department,post,username,pwd,email,mobile,address) values (?,?,?,?,?,?,?,?,?)",(self.first_name_call,self.last_name_call,self.select_employee_dept,self.select_employee_post,self.username_call,self.password_call,self.email_call,self.mobile_number_call,self.address_call))
            conn.commit()
            login_db_object.execute("INSERT INTO main.login_details (username,password)  values (?,?)",(self.username_call,self.password_call))
            conn.commit()
            conn.close()
            counter=1
        except:
            counter=0
            messagebox.showinfo("Failed", "Can't Register :( Username Occupied ")

        
        try:
            print("Checking for mobile number")
            write_message_no(self.mobile_number_call)
        except:
            print("Can't Write Mobile Number")

        try:
            def send_email(user, pwd, recipient, subject, body):
                import smtplib

                FROM = user
                TO = recipient if isinstance(recipient, list) else [recipient]
                SUBJECT = subject
                TEXT = body

                # Prepare actual message
                message = """From: %s\nTo: %s\nSubject: %s\n\n%s
                """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.ehlo()
                server.starttls()
                server.login(user, pwd)
                server.sendmail(FROM, TO, message)
                server.close()

            email = 'dg325885@gmail.com'
            pwd = 'diksha@123'
            recipient = self.email_call
            subject = 'Registered EMS'
            body = 'Hi '+self.first_name_call+',\nYou have registered with Employee Management Portal!!!'+'\n Regards,\n EMS Team'
            send_email(email, pwd, recipient, subject, body)
            print("mailsent")


        except:
            messagebox.showinfo("Error while sending Mail","Mail can't be sent")

        if(counter!=0):
            messagebox.showinfo("Successfully Registered","Taking you to the Login Page")
            import login
            call('python login.py', shell=True)

   


root=Tk()
login_home=Home(root)
root.wm_geometry("1360x1200")
root.configure(background = "tan")
root.title("Register Here")
root.mainloop()
