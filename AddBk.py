from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql


def bookRegister():
    
    bookid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status = bookInfo4.get()
    status = status.lower()
    
    insertBooks = "insert into "+bookTable+" values('"+bookid+"','"+title+"','"+author+"','"+status+"')"
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success',"Book added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    print(bookid)
    print(title)
    print(author)
    print(status)


    root.destroy()
    
def addBook(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("Adding book")
    root.minsize(width=800,height=900)
    root.maxsize(width=800,height=900)
    
    # root passwaord and database
    mypass = "samy"
    mydatabase="library2"

    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()
    
    # book table name
    bookTable = "books"

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#373a40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bd=0)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Adding Books", bg='#ff414d', fg='black', font=('Consolas',18))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='#222831')
    labelFrame.place(relx=0.1,rely=0.35,relwidth=0.8,relheight=0.4)
        
    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='#222831', fg='white', font=('Consolas',13))
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.4,rely=0.2, relwidth=0.55, relheight=0.08)
        
    # Title
    lb2 = Label(labelFrame,text="Title : ", bg='#222831', fg='white', font=('Consolas',13))
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.4,rely=0.35, relwidth=0.55, relheight=0.08)
        
    # Book Author
    lb3 = Label(labelFrame,text="Author : ", bg='#222831', fg='white', font=('Consolas',13))
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.4,rely=0.50, relwidth=0.55, relheight=0.08)
        
    # Book Status
    lb4 = Label(labelFrame,text="Status(Avail/issued) : ", bg='#222831', fg='white', font=('Consolas',12))
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.4,rely=0.65, relwidth=0.55, relheight=0.08)
        
    #Submit Button
    SubmitBtn = Button(root,text="Submit",bg='#F05454', fg='black', bd=0, font=('Consolas',13), command=bookRegister)
    SubmitBtn.place(relx=0.092,rely=0.9, relwidth=0.20,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#F05454', fg='black', bd=0, font=('Consolas',13), command=root.destroy)
    quitBtn.place(relx=0.70,rely=0.9, relwidth=0.20,relheight=0.08)
    
    root.mainloop()