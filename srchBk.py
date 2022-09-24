from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

# root password and database
mypass = "samy"
mydatabase="library2"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

bookTable = "books" #Book Table


    
def search(): 
    
    global bookInfo1,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("Searching Book")
    root.minsize(width=800,height=900)
    root.maxsize(width=800,height=900)

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#373a40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bd=0)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Searching Books", bg='#ff414d', fg='black', font=('Consolas',18))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='#222831')
    labelFrame.place(relx=0.1,rely=0.35,relwidth=0.8,relheight=0.4)  
        
    # Book ID to search
    lb2 = Label(labelFrame,text="Book ID : ", bg='#222831', fg='white', font=('Consolas',13))
    lb2.place(relx=0.05,rely=0.3)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.20,rely=0.3, relwidth=0.55)

    Label(labelFrame, text="%-10s%-35s%-25s%-15s"%('BID','Title','Author','Status'),bg='#222831', fg='white', font=('Consolas',10)).place(relx=0.07,rely=0.5)
    Label(labelFrame, text="--------------------------------------------------------------",bg='#222831', fg='white', font=('Consolas',12)).place(relx=0.05,rely=0.6)

    def searchBook():

        bookid = bookInfo1.get()
    
        getBooks = "select * from "+bookTable+" where bookid = '"+bookid+"'"

        y = 0.65

        try:
            cur.execute(getBooks)
            con.commit()
            for i in cur:
                Label(labelFrame, text="%-10s%-35s%-25s%-15s"%(i[0],i[1],i[2],i[3]),bg='#222831', fg='white', font=('Consolas',10)).place(relx=0.07,rely=y)
                y += 0.1
        except:
            messagebox.showinfo("Failed to fetch files from database")

    
    #Submit Button
    SearchBtn = Button(labelFrame,text="Search",bg='#F05454', fg='black', bd=0, font=('Consolas',13),command=searchBook)
    SearchBtn.place(relx=0.77,rely=0.3, relwidth=0.12, relheight=0.06)
    
    quitBtn = Button(root,text="Quit",bg='#F05454', fg='black', bd=0, font=('Consolas',13), command=root.destroy)
    quitBtn.place(relx=0.37,rely=0.9, relwidth=0.28,relheight=0.08)
    
    
    root.mainloop()