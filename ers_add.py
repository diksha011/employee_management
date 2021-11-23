#Employee Record System 
from tkinter import*
from tkinter import messagebox
import sys
import os
import signal
import time
from subprocess import  *
import sqlite3



root=Tk()                               #Main window 
f=Frame(root)
frame1=Frame(root)
frame2=Frame(root)
frame3=Frame(root)
root.title("Admin login - Employee Record System")
root.geometry("830x395")
root.configure(background="Black")

scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

firstname=StringVar()                    #Declaration of all variables
lastname=StringVar()
id=StringVar()
dept=StringVar()
designation=StringVar()
remove_id = StringVar()
remove_firstname=StringVar()
remove_lastname=StringVar()
searchid = StringVar()


def emp_dict(id,fname,lname,dept,post):                   #To add a new entry and check if entry already exist in excel sheet
    #print("done")
    try:
        conn = sqlite3.connect('portal_final.db')
        admin_register_db_object = conn.cursor()
    except:
        messagebox.showinfo("Failed", "Can't connect to the server")
        print("cant connect")
    
    try:
        admin_register_db_object.execute("INSERT OR REPLACE INTO admin_register (id, firstname,lastname,department,post) values (?,?,?,?,?)",(id,fname,lname,dept,post))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Employee added")
        counter=1
    except:
        counter=0
        messagebox.showinfo("Failed", "Can't Register :( Username Occupied ")
    
    
def add_entries():                       #to append all data and add entries on click the button
    i = id.get()
    i1 = i.lower()
    f=firstname.get()
    f1=f.lower()
    l=lastname.get()
    l1=l.lower()
    d=dept.get()
    d1=d.lower()
    de=designation.get()
    de1=de.lower()
    emp_dict(i1,f1,l1,d1,de1)


def add_info():                                           #for taking user input to add the enteries
    frame2.pack_forget()
    frame3.pack_forget()
    emp_id=Label(frame1,text="Enter ID of the employee: ",bg="red",fg="white")
    emp_id.grid(row=0,column=1,padx=10)
    e0=Entry(frame1,textvariable=id)
    e0.grid(row=0,column=2,padx=10)
    e0.focus()
    emp_first_name=Label(frame1,text="Enter first name of the employee: ",bg="red",fg="white")
    emp_first_name.grid(row=1,column=1,padx=10)
    e1=Entry(frame1,textvariable=firstname)
    e1.grid(row=1,column=2,padx=10)
    e1.focus()
    emp_last_name=Label(frame1,text="Enter last name of the employee: ",bg="red",fg="white")
    emp_last_name.grid(row=2,column=1,padx=10)
    e2=Entry(frame1,textvariable=lastname)
    e2.grid(row=2,column=2,padx=10)
    emp_dept=Label(frame1,text="Select department of employee: ",bg="red",fg="white")
    emp_dept.grid(row=3,column=1,padx=10)
    dept.set("Select Option")
    e4=OptionMenu(frame1,dept,"Select Option", "IT","Operations","Sales & Marketting","Human Resource","Security","Admin")
    e4.grid(row=3,column=2,padx=10)
    emp_desig=Label(frame1,text="Select designation of Employee: ",bg="red",fg="white")
    emp_desig.grid(row=4,column=1,padx=10)
    designation.set("Select Option")
    e5=OptionMenu(frame1,designation,"Select Option","Manager","Asst Manager","Project Manager","Team Lead","Senior Tester", 
                  "Junior Tester","Senior Developer","Junior Developer","Intern")
    e5.grid(row=4,column=2,padx=10)
    button4=Button(frame1,text="Add entries",command=add_entries)
    button4.grid(row=5,column=2,pady=10)
    
    frame1.configure(background="Red")
    frame1.pack(pady=10)
    
def clear_all():             #for clearing the entry widgets
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()

    
def remove_emp():                #for taking user input to remove enteries
    clear_all()
    emp_id=Label(frame2,text="Enter ID of the employee",bg="red",fg="white")
    emp_id.grid(row=0,column=1,padx=10)
    e=Entry(frame2,textvariable=remove_id)
    e.grid(row=0,column=2,padx=10)
    e.focus()
    emp_first_name=Label(frame2,text="Enter first name of the employee",bg="red",fg="white")
    emp_first_name.grid(row=1,column=1,padx=10)
    e6=Entry(frame2,textvariable=remove_firstname)
    e6.grid(row=1,column=2,padx=10)
    e6.focus()
    emp_last_name=Label(frame2,text="Enter last name of the employee",bg="red",fg="white")
    emp_last_name.grid(row=2,column=1,padx=10)
    e7=Entry(frame2,textvariable=remove_lastname)
    e7.grid(row=2,column=2,padx=10)
    remove_button=Button(frame2,text="Click to remove",command=remove_entry)
    remove_button.grid(row=3,column=2,pady=10)
    frame2.configure(background="Red")
    frame2.pack(pady=10)

def remove_entry():  #to remove entry from excel sheet
    rsi = remove_id.get()
    rsi1 = rsi.lower()
    print(rsi1)
    rsf=remove_firstname.get()
    rsf1=rsf.lower()
    print(rsf1)
    rsl=remove_lastname.get()
    rsl1=rsl.lower()
    print(rsl1)
    try:
        conn = sqlite3.connect('portal_final.db')
        admin_register_db_object = conn.cursor()
    except:
        messagebox.showinfo("Failed", "Can't connect to the server")
        print("cant connect")
    
    try:
        admin_register_db_object.execute("DELETE FROM admin_register WHERE id =? ",(rsi1,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Done","Successfully removed the Employee record")
        counter=1
    except:
        counter=0
        messagebox.showinfo("Failed", "No such employee exist")
    
    clear_all()
    
def search_emp():     #can implement search by 1st name,last name,emp id, designation
    clear_all()
    emp_id=Label(frame3,text="Enter ID of the employee",bg="red",fg="white")   #to take user input to seach
    emp_id.grid(row=1,column=1,padx=10)
    e8=Entry(frame3,textvariable=searchid)
    e8.grid(row=1,column=2,padx=10)
    e8.focus()
    search_button=Button(frame3,text="Click to search",command=search_entry)
    search_button.grid(row=3,column=2,pady=10)
    
    frame3.configure(background="Red")
    frame3.pack(pady=10)
    
def search_entry():
    id0 = searchid.get()
    search_database (id0)
    
def search_database(id0):
    try:
        conn = sqlite3.connect('portal_final.db')
        admin_register_db_object = conn.cursor()
    except:
        messagebox.showinfo("Failed", "Can't connect to the server")
        print("can't connect")
        
           
    try:
        first_name = []
        last_name = []
        post_list = []
        dept_list = []
        button_list = []
        admin_register_db_object.execute('SELECT * from admin_register where id="%s"' % (id0))
        store = admin_register_db_object.fetchall()
        print(store)   
        if(len(store)==0):
            messagebox.showerror("Failed", "NO SUCH EMPLOYEE EXIST ")
            return
            
        for j in range(0, len(store)):
            first_name.append('var' + str(j))
            last_name.append('var' + str(j))
            dept_list.append('var' + str(j))
            post_list.append('entry' + str(j))
            button_list.append(store[j][0])
        print(button_list)
        first_name_head = Label(frame3, text='First name:', font=("Courier", 14),background="Orange",fg="Yellow")
        first_name_head.grid(row=9, column=0)
        last_name_head = Label(frame3, text='Last name:', font=("Courier", 14),background="Orange",fg="Yellow")
        last_name_head.grid(row=9, column=1)
        dept_head = Label(frame3, text='Department:', font=("Courier", 14),background="Orange",fg="Yellow")
        dept_head.grid(row=9, column=2)
        post_head = Label(frame3, text='Post:', font=("Courier", 14),background="Orange",fg="Yellow")
        post_head.grid(row=9, column=3)
        for i in range(0, len(store)):
            first_name[i] = Label(frame3, text=store[i][1], font=("Courier", 12))
            first_name[i].grid(row=10 + i, column=0)
            last_name[i] = Label(frame3, text=store[i][2], font=("Courier", 12))
            last_name[i].grid(row=10 + i, column=1)
            dept_list[i] = Label(frame3, text=store[i][3],font=("Courier",12))
            dept_list[i].grid(row=10+i,column=2)
            post_list[i] = Label(frame3, text=store[i][4],font=("Courier",12))
            post_list[i].grid(row=10+i,column=3)
    except:
        messagebox.showerror("Failed", "error occured ")
    

        
#Main window buttons and labels
        
label1=Label(root,text="EMPLOYEE RECORD SYSTEM")
label1.config(font=('Italic',16,'bold'), justify=CENTER, background="Orange",fg="Yellow", anchor="center")
label1.pack(fill=X)

label2=Label(f,text="Select an action: ",font=('bold',12), background="Black", fg="White")
label2.pack(side=LEFT,pady=10)
button1=Button(f,text="Add", background="Brown", fg="White", command=add_info, width=8)
button1.pack(side=LEFT,ipadx=20,pady=10)
button2=Button(f,text="Remove", background="Brown", fg="white", command=remove_emp, width=8)
button2.pack(side=LEFT,ipadx=20,pady=10)
button1=Button(f,text="Search", background="Brown", fg="White", command=search_emp, width=8)
button1.pack(side=LEFT,ipadx=20,pady=10)
button6=Button(f,text="Close", background="Brown", fg="White", width=8, command=root.destroy)
button6.pack(side=LEFT,ipadx=20,pady=10)
f.configure(background="Black")
f.pack()

root.mainloop()
