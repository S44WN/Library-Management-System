from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

#root password and database
mypass = "samy"
mydatabase="library2"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here
issueTable = "books_issued" #Issue Table
bookTable = "books" #Book Table


allBookids = [] #List To store all Book IDs

def returnn():
    
    global SubmitBtn,labelFrame,lb1,bookInfo1,quitBtn,root,Canvas1,status
    
    bookid = bookInfo1.get()

    extractBookid = "select bookid from "+issueTable
    try:
        cur.execute(extractBookid)
        con.commit()
        for i in cur:
            allBookids.append(i[0])
        
        if bookid in allBookids:
            checkAvail = "select status from "+bookTable+" where bookid = '"+bookid+"'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]
                
            if check == 'issued':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error","Book ID not present")
    except:
        messagebox.showinfo("Error","Can't fetch Book IDs")
    
    
    issueSql = "delete from "+issueTable+" where bookid = '"+bookid+"'"
  
    print(bookid in allBookids)
    print(status)
    updateStatus = "update "+bookTable+" set status = 'avail' where bookid = '"+bookid+"'"
    try:
        if bookid in allBookids and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success',"Book Returned Successfully")
        else:
            allBookids.clear()
            messagebox.showinfo('Message',"Please check the book ID")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
    
    allBookids.clear()
    root.destroy()
    
def returnBook(): 
    
    global bookInfo1,SubmitBtn,quitBtn,Canvas1,con,cur,root,labelFrame, lb1
    
    root = Tk()
    root.title("Returning book")
    root.minsize(width=800,height=900)
    root.maxsize(width=800,height=900)

    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#373a40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bd=0)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Returning Books", bg='#ff414d', fg='black', font=('Consolas',18))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='#222831')
    labelFrame.place(relx=0.1,rely=0.35,relwidth=0.8,relheight=0.4)   
        
    # Book ID to Delete
    lb1 = Label(labelFrame,text="Book ID : ", bg='#222831', fg='white', font=('Consolas',13))
    lb1.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="Return",bg='#F05454', fg='black', bd=0, font=('Consolas',13),command=returnn)
    SubmitBtn.place(relx=0.092,rely=0.9, relwidth=0.20,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#F05454', fg='black', bd=0, font=('Consolas',13), command=root.destroy)
    quitBtn.place(relx=0.70,rely=0.9, relwidth=0.20,relheight=0.08)
    
    root.mainloop()