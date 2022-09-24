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


    
def modify(): 
    
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, bookInfo5, Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("Modifying Books")
    root.minsize(width=800,height=900)
    root.maxsize(width=800,height=900)

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#373a40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bd=0)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.08)

    headingLabel = Label(headingFrame1, text="Modifying Books", bg='#ff414d', fg='black', font=('Consolas',18))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='#222831')
    labelFrame.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.6)  
        
    # Book ID to modify
    lb1 = Label(labelFrame,text="Book ID of book to modify: ", bg='#222831', fg='white', font=('Consolas',13))
    lb1.place(relx=0.05,rely=0.1)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.45,rely=0.1, relwidth=0.30)


    Label(labelFrame, text="%-10s%-35s%-25s%-15s"%('BID','Title','Author','Status'),bg='#222831', fg='white', font=('Consolas',10)).place(relx=0.07,rely=0.2)
    Label(labelFrame, text="--------------------------------------------------------------",bg='#222831', fg='white', font=('Consolas',12)).place(relx=0.05,rely=0.25)


    #modification--
    lb1 = Label(labelFrame,text="Fill with Modifications : ", bg='#222831', fg='white', font=('Consolas',13))
    lb1.place(relx=0.05,rely=0.4)


    # Book ID to modify
    lb2 = Label(labelFrame,text="Book ID : ", bg='#222831', fg='white', font=('Consolas',13))
    lb2.place(relx=0.05,rely=0.50)
        
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.20,rely=0.50, relwidth=0.55)


    # Book ID to modify
    lb3 = Label(labelFrame,text="Title : ", bg='#222831', fg='white', font=('Consolas',13))
    lb3.place(relx=0.05,rely=0.55)
        
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.20,rely=0.55, relwidth=0.55)


    # Book ID to modify
    lb4 = Label(labelFrame,text="Author : ", bg='#222831', fg='white', font=('Consolas',13))
    lb4.place(relx=0.05,rely=0.60)
        
    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.20,rely=0.60, relwidth=0.55)


    # Book ID to modify
    lb5 = Label(labelFrame,text="Status : ", bg='#222831', fg='white', font=('Consolas',13))
    lb5.place(relx=0.05,rely=0.65)
        
    bookInfo5 = Entry(labelFrame)
    bookInfo5.place(relx=0.20,rely=0.65, relwidth=0.55)


    Label(labelFrame, text="%-10s%-35s%-25s%-15s"%('BID','Title','Author','Status'),bg='#222831', fg='white', font=('Consolas',10)).place(relx=0.07,rely=0.75)
    Label(labelFrame, text="--------------------------------------------------------------",bg='#222831', fg='white', font=('Consolas',12)).place(relx=0.05,rely=0.80)
    


    def searchBook():

        bookid = bookInfo1.get()
    
        getBooks = "select * from "+bookTable+" where bookid = '"+bookid+"'"

        try:
            cur.execute(getBooks)
            con.commit()
            for i in cur:
                Label(labelFrame, text="%-10s%-35s%-25s%-15s"%(i[0],i[1],i[2],i[3]),bg='#222831', fg='white', font=('Consolas',10)).place(relx=0.07,rely=0.3)
                
        except:
            messagebox.showinfo("Failed to fetch files from database")


    def modifyBook():

        bookid = bookInfo1.get()
        bookid_updt = bookInfo2.get()
        title_updt = bookInfo3.get()
        author_updt = bookInfo4.get()
        status_updt = bookInfo5.get()

        updatebookid = "update "+bookTable+" set bookid = "+bookid_updt+" where bookid = "+bookid
        updateTitle = "update "+bookTable+" set title = '"+title_updt+"' where bookid = "+bookid
        updateAuthor = "update "+bookTable+" set author = '"+author_updt+"' where bookid = "+bookid
        updateStatus = "update "+bookTable+" set status = '"+status_updt+"' where bookid = "+bookid
    
        getBooks = "select * from "+bookTable+" where bookid = "+bookid

        try:
            #updates....
            cur.execute(updatebookid)
            con.commit()
            cur.execute(updateTitle)
            con.commit()
            cur.execute(updateAuthor)
            con.commit()
            cur.execute(updateStatus)
            con.commit()

        except:
            messagebox.showinfo("Failed to modify files in database")


        try:
            #displaying updates......
            cur.execute(getBooks)
            con.commit()
            for i in cur:
                Label(labelFrame, text="%-10s%-35s%-25s%-15s"%(i[0],i[1],i[2],i[3]),bg='#222831', fg='white', font=('Consolas',10)).place(relx=0.07,rely=0.85)
                
        except:
            messagebox.showinfo("Failed to fetch files from database")


    

    #Submit Button
    SubmitBtn = Button(labelFrame,text="Find",bg='#F05454', fg='black', bd=0, font=('Consolas',13),command=searchBook)
    SubmitBtn.place(relx=0.8, rely=0.1, relwidth=0.12, relheight=0.04)


    #modify Button
    ModifyBtn = Button(labelFrame,text="Modify",bg='#F05454', fg='black', bd=0, font=('Consolas',13),command=modifyBook)
    ModifyBtn.place(relx=0.8, rely=0.65, relwidth=0.12, relheight=0.04)


    quitBtn = Button(root,text="Quit",bg='#F05454', fg='black', bd=0, font=('Consolas',13), command=root.destroy)
    quitBtn.place(relx=0.37,rely=0.9, relwidth=0.28,relheight=0.08)
    
    
    root.mainloop()