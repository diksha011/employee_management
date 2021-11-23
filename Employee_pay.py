import time
import datetime
from tkinter import *
from tkinter import messagebox 
import sqlite3
import tkinter

root=Tk()
root.title("Admin login - Employee payroll system")
root.geometry('1350x650+0+0')
root.configure(background="black")

Tops=Frame(root,width=1350,height=50,bd=8,bg="black")
Tops.pack(side=TOP)

f1=Frame(root,width=600,height=600,bd=8,bg="black")
f1.pack(side=LEFT)
f2=Frame(root,width=300,height=700,bd=8,bg="black")
f2.pack(side=RIGHT)

fla=Frame(f1,width=600,height=200,bd=8,bg="black")
fla.pack(side=TOP)
flb=Frame(f1,width=300,height=600,bd=8,bg="black")
flb.pack(side=TOP)

label1=Label(Tops,text="EMPLOYEE PAYMENT SYSTEM")
label1.config(font=('Italic',36,'bold'), justify=CENTER, background="Orange",fg="Yellow", anchor="center")
label1.pack(fill=X)


def exit():
  exit= tkinter.messagebox.askyesno("Employee system","Do you want to exit the system")
  if exit>0:
    root.destroy()
    return

def reset():
  Name.set("")
  department.set("")
  HoursWorked.set("")
  wageshour.set("")
  post.set("")
  NetPayable.set("")
  OverTimeBonus.set("")
  IDNumber.set("")
  txtpayslip.delete("1.0",END)
  
def enterinfo():
  txtpayslip.delete("1.0",END)
  txtpayslip.insert(END,"\t\tPay Slip\n\n")
  txtpayslip.insert(END,"Name :\t\t"+Name.get()+"\n\n")
  txtpayslip.insert(END,"Department :\t\t"+department.get()+"\n\n")
  txtpayslip.insert(END,"Post :\t\t"+post.get()+"\n\n")
  txtpayslip.insert(END,"ID Number :\t\t"+IDNumber.get()+"\n\n")
  txtpayslip.insert(END,"Hours Worked :\t\t"+HoursWorked.get()+"\n\n")
  txtpayslip.insert(END,"Net Payable :\t\t"+NetPayable.get()+"\n\n")
  txtpayslip.insert(END,"Wages per hour :\t\t"+wageshour.get()+"\n\n")



def weeklywages():
    txtpayslip.delete("1.0",END)
    hoursworkedperweek=float(HoursWorked.get())
    wagesperhours=float(wageshour.get())
    id = IDNumber.get()
    id0 = id.lower()
    try:
        conn = sqlite3.connect('portal_final.db')
        admin_register_db_object = conn.cursor()
        salary_db_object=conn.cursor()
    except:
        messagebox.showinfo("Failed", "Can't connect to the server")
        print("can't connect")
    try: 
        admin_register_db_object.execute('SELECT * from admin_register where id="%s"' % (id0))
        store = admin_register_db_object.fetchall()
        print(store)  
        if (len(store)==0):
            messagebox.showerror("Failed", "NO SUCH EMPLOYEE EXIST ")
            return
            
        for i in range(0, len(store)):
            Name.set(store[i][1])
            department.set(store[i][3])
            post.set(store[i][4])
  
        netpay=wagesperhours*hoursworkedperweek
      
        if hoursworkedperweek > 40:
            overtimehours=(hoursworkedperweek-40)+wagesperhours*1.5
            overtime="INR",str('%.2f'%(overtimehours))
            OverTimeBonus.set(overtime)
        
        elif hoursworkedperweek<=40:
            overtimehours=0
            overtime="INR",str('%.2f'%(overtimehours))
            OverTimeBonus.set(overtime)
                
        np = netpay + overtimehours
        netpays="INR",str('%.2f'%(np))
        NetPayable.set(netpays)
        
        salary_db_object.execute("INSERT INTO salary (ID,date,salary)  values (?,?,?)",(id0,time.strftime("%d/%m/%Y"),np))
        conn.commit()
        counter = 1
    except:
        counter = 0
        messagebox.showerror("Failed", "error occured ")
        
    return  
  
  
    

#=============================== Variables ========================================================
Name=StringVar()
department=StringVar()
HoursWorked=StringVar()
wageshour=StringVar()
Payable=StringVar()
NetPayable=StringVar()
OverTimeBonus=StringVar()
post=StringVar()
IDNumber=StringVar()
TimeOfOrder=StringVar()
DateOfOrder=StringVar()

DateOfOrder.set(time.strftime("%d/%m/%Y"))

#================================ Label Widget =================================================

lblName=Label(fla,text="Name",font=('arial',16,'bold'),bd=20,fg="white",bg="black").grid(row=0,column=2)
lbldept=Label(fla,text="Department",font=('arial',16,'bold'),bd=20,fg="white",bg="black").grid(row=1,column=0)
lblpost=Label(fla,text="Post",font=('arial',16,'bold'),bd=20,fg="white",bg="black").grid(row=1,column=2)
lblIDNumber=Label(fla,text="ID Number",font=('arial',16,'bold'),bd=20,fg="white",bg="black").grid(row=0,column=0)
lblHoursWorked=Label(fla,text="Hours Worked",font=('arial',16,'bold'),bd=20,fg="white",bg="black").grid(row=2,column=0)
lblHourlyRate=Label(fla,text="Hourly Rate",font=('arial',16,'bold'),bd=20,fg="white",bg="black").grid(row=2,column=2)
lblOverTime=Label(fla,text="OverTime",font=('arial',16,'bold'),bd=20,fg="white",bg="black").grid(row=3,column=0)
lblNetPay=Label(fla,text="Net Pay",font=('arial',16,'bold'),bd=20,fg="white",bg="black").grid(row=3,column=2)

#=============================== Entry Widget =================================================

etxname=Label(fla,textvariable=Name,font=('arial',16,'bold'),bd=16,width=20,justify='left', relief = "ridge")
etxname.grid(row=0,column=3)

etxdept=Label(fla,textvariable=department,font=('arial',16,'bold'),bd=16,width=20,justify='left', relief = "ridge")
etxdept.grid(row=1,column=1)

etxpost=Label(fla,textvariable=post,font=('arial',16,'bold'),bd=16,width=20,justify='left', relief = "ridge")
etxpost.grid(row=1,column=3)

etxhoursworked=Entry(fla,textvariable=HoursWorked,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxhoursworked.grid(row=2,column=1)

etxwagesperhours=Entry(fla,textvariable=wageshour,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxwagesperhours.grid(row=2,column=3)

etxnin=Entry(fla,textvariable=IDNumber,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxnin.grid(row=0,column=1)

etxnetpay=Label(fla,textvariable=NetPayable,font=('arial',16,'bold'),bd=16,width=20,justify='left', relief = "ridge")
etxnetpay.grid(row=3,column=3)

etxovertime=Label(fla,textvariable=OverTimeBonus,font=('arial',16,'bold'),bd=16,width=20,justify='left', relief = "ridge")
etxovertime.grid(row=3,column=1)

#=============================== Text Widget ============================================================

payslip=Label(f2,textvariable=DateOfOrder,font=('arial',21,'bold'),fg="white",bg="red").grid(row=0,column=0)
txtpayslip=Text(f2,height=22,width=34,bd=16,font=('arial',13,'bold'),fg="white",bg="tan")
txtpayslip.grid(row=1,column=0)

#=============================== buttons ===============================================================

btnsalary=Button(flb,text='Weekly Salary',padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=14,background="Brown", fg="White",command=weeklywages).grid(row=0,column=0)

btnreset=Button(flb,text='Reset',padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=14,command=reset,background="Brown", fg="White").grid(row=0,column=1)

btnpayslip=Button(flb,text='View Payslip',padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=14,command=enterinfo,background="Brown", fg="White").grid(row=0,column=2)

btnexit=Button(flb,text='Exit System',padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=14,command=exit,background="Brown", fg="White").grid(row=0,column=3)

root.mainloop()


