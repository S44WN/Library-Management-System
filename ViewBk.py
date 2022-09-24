from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

# root password and database
mypass = "samy" 
mydatabase="library2"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

# Table Name
bookTable = "books" 
    
def View(): 
    
    root = Tk()
    root.title("Viewing book")
    root.minsize(width=800,height=900)
    root.maxsize(width=800,height=900)
    

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#373a40")
    Canvas1.pack(expand=True,fill=BOTH)
        
        
    headingFrame1 = Frame(root,bd=0)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Viewing Books", bg='#ff414d', fg='black', font=('Consolas',18))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='#222831')
    labelFrame.place(relx=0.1,rely=0.35,relwidth=0.8,relheight=0.4)

    y = 0.25
    
    Label(labelFrame, text="%-10s%-35s%-25s%-15s"%('BID','Title','Author','Status'),bg='#222831', fg='white', font=('Consolas',10)).place(relx=0.07,rely=0.1)
    Label(labelFrame, text="--------------------------------------------------------------",bg='#222831', fg='white', font=('Consolas',12)).place(relx=0.05,rely=0.2)
    
    
    getBooks = "select * from "+bookTable
    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-10s%-35s%-25s%-15s"%(i[0],i[1],i[2],i[3]),bg='#222831', fg='white', font=('Consolas',10)).place(relx=0.07,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")

    
    quitBtn = Button(root,text="Quit",bg='#F05454', fg='black', bd=0, font=('Consolas',13), command=root.destroy)
    quitBtn.place(relx=0.37,rely=0.9, relwidth=0.28,relheight=0.08)
    
    root.mainloop()