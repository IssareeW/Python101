from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox #to show message box

GUI=Tk() #หน้าจอหลัก
GUI.title('My Balance') #program name
GUI.geometry('600x600') #program size

L1=Label(GUI,text='My Account Balance',font=('Tahoma', 15),fg='pink') #Program Name shown on UI with font and size
L1.place(x=20,y=30)
########################
def Button1():#def = function to store many commands, Button2 is name of function
    text='Successfully saved'
    messagebox.showinfo('Saved!',text)
b1=Button(GUI,text='Save',command=Button1) #button name and ผูกกับ function ที่กำหนดไว้
#b1.pack() #position of button
b1.place(x=410,y=200)


b2=ttk.Button(GUI,text='Show Recent Data') #button name
#b2.pack(ipadx=20,ipady=30) #position of button with pixel size of x & y
b2.place(x=50,y=200) #place button at x & y

def Button3():#def = function to store many commands, Button2 is name of function
    text='Already canceled'
    messagebox.showwarning('Canceled!',text) #show warning
Fb3=Frame(GUI) #คล้ายกระดาน
Fb3.place(x=300,y=190)
b3=ttk.Button(Fb3,text='Cancel',command=Button3) #button name and ผูกกับ function 
b3.pack(ipadx=10,ipady=10)

def Button4():#def = function to store many commands, Button2 is name of function
    text='No Historical Data'
    messagebox.showerror('Historical Data',text) #show error when clicking
Fb4=Frame(GUI)
Fb4.place(x=170,y=200)
b4=ttk.Button(GUI,text='Show Historical Data',command=Button4) #button name
b4.place(x=170,y=200) #place button at x & y



GUI.mainloop()
