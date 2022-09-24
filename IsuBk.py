from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

# root password and database
mypass = "samy"
mydatabase="library2"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

#table names
issueTable = "books_issued" 
bookTable = "books"
    
#List To store all Book IDs
allBookids = [] 

def issue():
    
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
    bookid = inf1.get()
    issueto = inf2.get()

    issueBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()
    
    
    extractBookid = "select bookid from "+ bookTable
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
                
            if check == 'avail' or check == "Avail":
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error","Book ID not present")
    except:
        messagebox.showinfo("Error","Can't fetch Book IDs")
    
    issueSql = "insert into "+issueTable+" values ('"+bookid+"','"+issueto+"')"
    show = "select * from "+issueTable
    
    updateStatus = "update "+bookTable+" set status = 'issued' where bookid = '"+bookid+"'"
    try:
        if bookid in allBookids and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success',"Book Issued Successfully")
            root.destroy()
        else:
            allBookids.clear()
            messagebox.showinfo('Message',"Book Already Issued")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
    print(bookid)
    print(issueto)
    
    allBookids.clear()
    
def issueBook(): 
    
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
    root = Tk()
    root.title("Issuing book")
    root.minsize(width=800,height=900)
    root.maxsize(width=800,height=900)
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#373a40")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bd=0)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Issuing Books", bg='#ff414d', fg='black', font=('Consolas',18))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='#222831')
    labelFrame.place(relx=0.1,rely=0.35,relwidth=0.8,relheight=0.4)  
        
    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='#222831', fg='white', font=('Consolas',13))
    lb1.place(relx=0.05,rely=0.2)
        
    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    # Issued To Student name 
    lb2 = Label(labelFrame,text="Issued To : ", bg='#222831', fg='white', font=('Consolas',13))
    lb2.place(relx=0.05,rely=0.6)
        
    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3,rely=0.6, relwidth=0.62)
    
    
    #Issue Button
    issueBtn = Button(root, text="Issue", bg='#F05454', fg='black', bd=0, font=('Consolas',13), command=issue)
    issueBtn.place(relx=0.092,rely=0.9, relwidth=0.20,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#F05454', fg='black', bd=0, font=('Consolas',13), command=root.destroy)
    quitBtn.place(relx=0.70,rely=0.9, relwidth=0.20,relheight=0.08)
    
    root.mainloop()
    