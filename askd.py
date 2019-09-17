import pandas as pd

from tkinter import *
 
window = Tk()


    
 
window.title("GMRVF")
window.geometry('800x400')
lbl = Label(window, text="WELCOME,PLEASE PROVIDE YOUR LOGIN DETAILS", font=("Comic Sans", 20))
lbl.grid(column=1,row=0)

l=["anusha"]
Label(window, text='username').grid(row=2)
Label(window, text='password').grid(row=3)
e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=2,column=1)
e2.grid(row=3,column=1)


def dialog1():
    
    username=e1.get()
    password = e2.get()
    
        
    def clicked():
        window1=Tk()
        window1.title("detail checking")
        window1.geometry('700x300')
        def dialog2():
            adhaar=int(e3.get())
            file = pd.ExcelFile('Book1.xlsx')
            file.sheet_names
            f1 = file.parse('Sheet1')
            if (f1.ID == adhaar).any():
                lbl5=Label(window1,text="Already registered",font=("Comic Sans",20))
                lbl5.grid(row=4,column=1)
                
                
            else:
                lbl6=Label(window1,text="new applicant",font=("Comic Sans",20))
                lbl6.grid(row=4,column=1)
                
                
        lbl2=Label(window1,text="LOGIN SUCCESSFUL", font=("Comic Sans",20))
        lbl2.grid(row=1)
        lbl1=Label(window1, text="Enter aadhar number ")
        lbl1.grid(row=2)
        e3=Entry(window1)
        e3.grid(column=1,row=2)
        btn1=Button(window1,text='ENTER',command=dialog2)
        btn1.grid(column=1,row=3)
        def dialog4():
            name=e4.get()
            dob=e5.get()
            fname=e6.get()
            file = pd.ExcelFile('Book1.xlsx')
            file.sheet_names
            f1 = file.parse('Sheet1')
            if (f1.Name == name & f1.DOB == dob & f1.Fname == fname).any():
                
                lbl10=Label(window1,text="Already registered",font=("Comic Sans",10))
                lbl10.grid(row=3,column=2)
            else:
                 lbl11=Label(window1,text="new applicant",font=("Comic Sans",10))
                 lbl11.grid(row=3,column=2)
                
                 
        def dialog3():
            lbl7=Label(window1,text="Enter Name",font=("Comic Sans",10))
            lbl7.grid(column=1,row=7)
            e4=Entry(window1)
            e4.grid(column=2,row=7)
            lbl8=Label(window1,text="Enter DOB")
            lbl8.grid(column=1,row=8)
            e5=Entry(window1)
            e5.grid(column=2,row=8)
            lbl9=Label(window1,text="Father's Name",font=("Comic Sans",10))
            lbl9.grid(column=1,row=9)
            e6=Entry(window1)
            e6.grid(column=2,row=9)
            btn2=Button(window1,text="Check",command=dialog4)
            btn2.grid(column=1,row=10)
        lbl13=Label(window1,text="Do you want to check more details",font=("Comic Sans",10))
        lbl13.grid(column=2,row=5)
        rad1=Radiobutton(window1,text="YES",value=1,command=dialog3)
        rad1.grid(column=2,row=6)
        rad2=Radiobutton(window1,text="NO",value=2)
        rad2.grid(column=3,row=6)

            
        
     
        
        window1.mainloop()
    if (username == 'admin' and  password == 'secret'):
        Label(window,text='Correct Login').grid(row=5,column=1)
        clicked()
        
    else:
        Label(window,text='Invalid Login').grid(row=5,column=1)
    

    

btn = Button(window, text = 'Check Login',command = dialog1)
btn.grid(column=1 , row =4)

     
window.mainloop()