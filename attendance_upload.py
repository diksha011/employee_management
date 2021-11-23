from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import time
from datetime import date
import sqlite3

root=Tk()                               #Main window 
f=Frame(root)
frame1=Frame(root)
frame2=Frame(root)
frame3=Frame(root)
root.title("Admin login- Employee Attendance System")
root.geometry("830x395")
root.configure(background="Black")

# variables
id = StringVar()
dates = StringVar()
status = StringVar()

def upload_attendance(id1,dates1,status1):
    try:
        conn = sqlite3.connect('portal_final.db')
        attendance_db_object = conn.cursor()
    except:
        messagebox.showinfo("Failed", "Can't connect to the server")
        print("can't connect")
    try:
        attendance_db_object.execute("INSERT OR REPLACE INTO attendance_whole (ID,date,status) values (?,?,?)",(id1,dates1,status1))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "attendance uploaded")
        counter=1
    except:
        counter=0
        messagebox.showerror("Failed", "error occured ")
        
      
        
# getting values of variables
def add_entries():
    id1 = id.get()
    id2  = id1.lower()
    print(id2)
    dates1 = time.strftime("%d/%m/%Y")
    dates.set(dates1)
    print(dates1)
    status1 = status.get() 
    print (status1)

    upload_attendance(id2, dates1, status1)
    
def upload_attendance_window():
    frame2.pack_forget()
    frame3.pack_forget()
    emp_id=Label(frame1,text="Enter ID of the employee: ",bg="red",fg="white")
    emp_id.grid(row=0,column=1,padx=10)
    e0=Entry(frame1,textvariable=id)
    e0.grid(row=0,column=2,padx=10)
    e0.focus()
    emp_first_name=Label(frame1,text="Enter Date: ",bg="red",fg="white")
    emp_first_name.grid(row=1,column=1,padx=10)
    e1=Label(frame1,textvariable=dates)
    e1.grid(row=1,column=2,padx=10)
    e1.focus()
    emp_stat=Label(frame1,text="Select Status: ",bg="red",fg="white")
    emp_stat.grid(row=3,column=1,padx=10)
    status.set("Select Option")
    e4=OptionMenu(frame1,status,"Select Option", "Present","Absent","Leave")
    e4.grid(row=3,column=2,padx=10)
    button4=Button(frame1,text="Add entries",command=add_entries)
    button4.grid(row=5,column=2,pady=10)
    
    frame1.configure(background="Red")
    frame1.pack(pady=10)
    
def clear_all():             #for clearing the entry widgets
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()  
    
def edit_attendance_window():
    clear_all()
    emp_id=Label(frame2,text="Enter ID of the employee You want to edit: ",bg="red",fg="white")
    emp_id.grid(row=0,column=1,padx=10)
    e0=Entry(frame2,textvariable=id)
    e0.grid(row=0,column=2,padx=10)
    e0.focus()
    emp_DATE=Label(frame2,text="Enter Date: ",bg="red",fg="white")
    emp_DATE.grid(row=1,column=1,padx=10)
    e1=Entry(frame2,textvariable=dates)
    e1.grid(row=1,column=2,padx=10)
    e1.focus()
    emp_stat=Label(frame2,text="Select New Status: ",bg="red",fg="white")
    emp_stat.grid(row=3,column=1,padx=10)
    status.set("Select Option")
    e4=OptionMenu(frame2,status,"Select Option", "Present","Absent","Leave")
    e4.grid(row=3,column=2,padx=10)
    button4=Button(frame2,text="MODIFY",command=add_entries)
    button4.grid(row=5,column=2,pady=10)
    
    frame2.configure(background="Red")
    frame2.pack(pady=10)
    
def display_attendance_window():
    clear_all()
    emp_date=Label(frame3,text="Enter Date: ",bg="red",fg="white")
    emp_date.grid(row=1,column=1,padx=10)
    e1=Entry(frame3,textvariable=dates)
    e1.grid(row=1,column=2,padx=10)
    e1.focus()
    button4=Button(frame3,text="Show",command=search_entry)
    button4.grid(row=5,column=2,pady=10)
    
    frame3.configure(background="Red")
    frame3.pack(pady=10)

def search_entry():
    date1 = dates.get()
    display_attendance(date1)

def display_attendance(date1):
    
    try:
        conn = sqlite3.connect('portal_final.db')
        attendance_db_object = conn.cursor()
    except:
        messagebox.showinfo("Failed", "Can't connect to the server")
        print("can't connect")
        
    try:
        ID = []
        status_list = []
        button_list = []
        attendance_db_object.execute('SELECT * from attendance_whole where date="%s"' % (date1))
        store = attendance_db_object.fetchall()
        print(store)        
        for j in range(0, len(store)):
            ID.append('var' + str(j))
            status_list.append('entry' + str(j))
            button_list.append(store[j][0])
        print(button_list)
        id_head = Label(frame3, text='ID:', font=("Courier", 18),background="Orange",fg="Yellow")
        id_head.grid(row=9, column=0)
        status_head = Label(frame3, text='Status:', font=("Courier", 18),background="Orange",fg="Yellow")
        status_head.grid(row=9, column=2)
        for i in range(0, len(store)):
            ID[i] = Label(frame3, text=store[i][0], font=("Courier", 12))
            ID[i].grid(row=10 + i, column=0)
            status_list[i] = Label(frame3, text=store[i][2],font=("Courier",12))
            status_list[i].grid(row=10+i,column=2)
    except:
        messagebox.showerror("Failed", "error occured ")
        
    
label1=Label(root,text="EMPLOYEE ATTENDANCE RECORD SYSTEM")
label1.config(font=('Italic',16,'bold'), justify=CENTER, background="Orange",fg="Yellow", anchor="center")
label1.pack(fill=X)

label2=Label(f,text="Select an action: ",font=('bold',12), background="Black", fg="White")
label2.pack(side=LEFT,pady=10)
button1=Button(f,text="upload_attendance", background="Brown", fg="White",command = upload_attendance_window, width=8)
button1.pack(side=LEFT,ipadx=20,pady=10)
button2=Button(f,text="Edit attendance", background="Brown", fg="white",command = edit_attendance_window, width=8)
button2.pack(side=LEFT,ipadx=20,pady=10)
button3=Button(f,text="Today's attendance", background="Brown", fg="white",command = display_attendance_window, width=8)
button3.pack(side=LEFT,ipadx=20,pady=10)
button6=Button(f,text="Close", background="Brown", fg="White", width=8, command=root.destroy)
button6.pack(side=LEFT,ipadx=20,pady=10)
f.configure(background="Black")
f.pack()

root.mainloop()