from tkinter import *
from tkinter import messagebox as msg
import mysql.connector as mysql
from PIL import Image, ImageTk
from tkinter import ttk
def adddonar():
    global count
    def clr():
        e1.delete(0,END)
        e2.delete(0,END)
        e3.set('')
        e4.set('')
        e5.delete('1.0',END)
        e6.delete(0,END)
        e7.delete(0,END)
        
    def add():
       name=e1.get()
       age=e2.get()
       phone=e6.get()
       if(e1.get()=="" or e2.get()=="" or e3.get()=="" or e4.get()=="" or e5.get('1.0',END)=="" or e6.get()=="" or e7.get()==""):
        msg.showinfo("Insert Status","PLEASE FILL ALL INFORMATION")
        return
       if(name.isalpha()!=TRUE):
         msg.showinfo("Insert Status","NAME MUST CONTAIN ALPHABETS ONLY")
         return 
       if(age.isdigit()!=TRUE):
         msg.showinfo("Insert Status","AGE MUST BE A NUMBER ONLY")
         return
        
       if(phone.isdigit()!=TRUE):
         msg.showinfo("Insert Status","PHONE NO MUST BE A NUMBER ONLY")
         return
       if(phone.isdigit()==TRUE and len(phone)<10):
         msg.showinfo("Insert Status","PHONE NO MUST CONTAIN 10 DIGITS")
         return 
         
       else:  
        con=mysql.connect(host="localhost",user="root",password="Harshal@1008",database="bld")
        cur=con.cursor()
        
        cur.execute("insert into reco values('"+e1.get()+"','"+e2.get()+"','"+e3.get()+"','"+e4.get()+"','"+e5.get('1.0',END)+"','"+e6.get()+"','"+e7.get()+"')")
        cur.execute("commit")
        

        
        
                    
        cur.execute("update bld_stock set PACKETS=PACKETS+1 where BLOOD_GROUP='"+e4.get()+"'")
        cur.execute("commit")
        con.close()
        msg.showinfo("insert status","successfully stored information...")
        w2.destroy()
    w2=Tk()
    w2.configure(bg="sky blue")
    w2.resizable(0,0)
    w2.title("DONAR FORM")
    
    Label(w2,text="*FILL DONAR FORM*",bg="sky blue").pack()                
    l1=Label(w2,text="FULL NAME:",bg="sky blue",font=("times new roman",10))
    l1.place(x=30,y=50)
    e1=Entry(w2)
    e1.focus()
    e1.place(x=120,y=50)
                    
    l2=Label(w2,text="AGE:",bg="sky blue",font=("times new roman",10))
    l2.place(x=30,y=80)
    e2=Entry(w2)
    e2.place(x=120,y=80)
                    
   
    
    l=Label(w2,text="SEX:",bg="sky blue",font=("times new roman",10))
    l.place(x=30,y=110)
    e3=ttk.Combobox(w2,state="readonly",width=17)
    e3['values']=("MALE","FEMALE","OTHER")
    e3.place(x=120,y=110)
                    
   
    l3=Label(w2,text="BLOOD GROUP:",bg="sky blue",font=("times new roman",10))
    l3.place(x=30,y=140)
    
    e4=ttk.Combobox(w2,state="readonly",width=17)
    e4['values']=("A+","B+","AB+","O+","O-")
    e4.place(x=120,y=140)
                    
    l4=Label(w2,text="ADDRESS:",bg="sky blue",font=("times new roman",10))
    l4.place(x=30,y=170)
    e5=Text(w2,height=2,width=16)
    e5.place(x=120,y=170)
                    
    l5=Label(w2,text="CONTACT NO:",bg="sky blue",font=("times new roman",10))
    l5.place(x=30,y=220)
    e6=Entry(w2)
    e6.place(x=120,y=220)
                    
    l6=Label(w2,text="DATE:",bg="sky blue",font=("times new roman",10))
    l6.place(x=30,y=250)
    e7=Entry(w2)
    e7.place(x=120,y=250)
    sub=Button(w2,text="SUBMIT",command=add,bg="green",fg="white",width=10,font=("times new roman",10))
    sub.place(x=110,y=280)
    res=Button(w2,text="RESET",command=clr,bg="green",fg="white",width=10,font=("times new roman",10))
    res.place(x=200,y=280)
    
    
    
    w2.geometry("400x400+100+50")
    w2.mainloop()
def fetch():
        con=mysql.connect(host="localhost",user="root",password="Harshal@1008",database="bld")
        cur=con.cursor()
        cur.execute("select * from reco order by blood_group asc")

        rows=cur.fetchall()
        
        con.close()
        r=Tk()
        r.geometry("500x500+100+50")
        
        r.title("DONAR RECORDS")
        
        l1=ttk.Treeview(r,height=len(rows),columns=(1,2,3,4,5,6,7),show="headings",selectmode='browse')
        l1.grid()

        
        
        l1.heading(1,text="NAME")
        l1.heading(2,text="AGE")
        l1.heading(3,text="SEX")
        l1.heading(4,text="BLOOD GRP")
        l1.heading(5,text="ADDRESS")
        l1.heading(6,text="CONTACT NO")
        l1.heading(7,text="DATE")
        
        for i in rows:
            l1.insert('','end',values=i)
            
           
        
        r.mainloop()
def fetch1():
        con=mysql.connect(host="localhost",user="root",password="Harshal@1008",database="bld")
        cur=con.cursor()
        cur.execute("select * from bld_stock ")

        rows=cur.fetchall()
        
        con.close()
        r1=Tk()
        r1.configure(bg="grey")
        r1.geometry("500x500+100+50")
        r1.title("BLOOD STOCK")
        r1.resizable(0,0)
        
        l1=ttk.Treeview(r1,height=len(rows),columns=(1,2),show="headings")
        l1.pack()
        l1.heading(1,text="BLOOD GROUP")
        l1.heading(2,text="NO OF PACKETS")
        
        
        for i in rows:
            l1.insert('','end',values=i)
            
           
        
        r1.mainloop()
def fetch3():
    def srch(): 
        con=mysql.connect(host="localhost",user="root",password="Harshal@1008",database="bld")
        cur=con.cursor()
        cur.execute("select * from reco where blood_group='"+e11.get()+"' order by blood_group asc" )

        rows=cur.fetchall()
        
        con.close()
        l1=ttk.Treeview(r2,height=15,columns=(1,2,3,4,5,6,7),show="headings")
    
        l1.place(x=5,y=100)
        l1.heading(1,text="NAME")
        l1.heading(2,text="AGE")
        l1.heading(3,text="SEX")
        l1.heading(4,text="BLOOD GRP")
        l1.heading(5,text="ADDRESS")
        l1.heading(6,text="CONTACT NO")
        l1.heading(7,text="DATE")
        
        for i in rows:
            l1.insert('','end',values=i)
        
    r2=Tk()
    r2.title("SEARCH DONAR")
    r2.geometry("1000x500+100+50")
    e11=ttk.Combobox(r2)
    e11['values']=("A+","B+","AB+","O+","O-")
    e11.place(x=500,y=20)
    b1=Button(r2,text="SEARCH",command=srch,bg="green",fg="white")
    b1.place(x=650,y=20)
    
    r2.mainloop()
        
        
                    
        
root=Tk()
c=Canvas(root,bg="blue",height=400,width=700)

img4 = ImageTk.PhotoImage(Image.open(r"C:\Users\sudhakar mankar\Desktop\q.jpg"))

btn1 = ImageTk.PhotoImage(Image.open(r"C:\Users\sudhakar mankar\Desktop\w1.png"))

root.geometry("960x480+100+50")
photo = PhotoImage(file = r"C:\Users\sudhakar mankar\Desktop\w1.png")
root.iconphoto(False, photo)
back=Label(root,image=img4)
root.title("Blood Bank")
back.place(x=0,y=0,relwidth=1,relheight=1)
l1=Label(root,text=" BLOOD BANK ",fg="orange",bg="#123456",font=("times new roman",20))
l1.pack(side=TOP,fill=X)
l12=Label(root,text=" DONATE BLOOD SAVE LIFE ",fg="orange",bg="#123456",font=("times new roman",20))
l12.pack(side=BOTTOM,fill=X)
root.resizable(0,0)
b1=Button(root,text="ADD DONAR",command=adddonar,width=30,bg="green",fg="white",relief=GROOVE,font=("times new roman",10))
b1.place(x=450,y=100)
b2=Button(root,text="SEARCH DONAR",width=30,bg="green",fg="white",relief=GROOVE,command=fetch3,font=("times new roman",10))
b2.place(x=450,y=150)
b3=Button(root,text="VIEW BLOOD STOCK",width=30,bg="green",fg="white",relief=GROOVE,command=fetch1,font=("times new roman",10))
b3.place(x=450,y=200)
b4=Button(root,text="VIEW DONAR LIST",width=30,bg="green",fg="white",relief=GROOVE,command=fetch,font=("times new roman",10))
b4.place(x=450,y=250)
b5=Button(root,text="EXIT",bg="green",width=30,command=root.destroy,fg="white",relief=GROOVE,font=("times new roman",10))
b5.place(x=450,y=300)
c.pack()
root.mainloop()
