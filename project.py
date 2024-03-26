import sqlite3
from tkinter import *
from tkinter import messagebox,ttk

def connection():
    global conn,cursor
    conn = sqlite3.connect("db/customers.db")
    cursor = conn.cursor()

def mainWindow():
    root = Tk()
    w,h = 1024,800
    x = root.winfo_screenwidth()/2-w/2
    y = root.winfo_screenheight()/2-h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.config(bg="#B5C0D0")
    root.option_add("*font","Helvetica 16 bold")
    root.rowconfigure((0,1,2,3),weight=1)
    root.columnconfigure((0,1,2,3),weight=1)
    return root

def loginPage(root):
    global userEntry,pwdEntry
    loginFrame.rowconfigure((0,1,2,3,4),weight=1)
    loginFrame.columnconfigure((0,1),weight=1)

    Label(loginFrame,text = "Login",bg="#FFBE98").grid(row=0,column=0,columnspan=2)
    Label(loginFrame,text = "Username: ",bg="#FFBE98").grid(row=1,column=0,sticky='e')  
    Label(loginFrame,text = "Password: ",bg="#FFBE98").grid(row=2,column=0,sticky='e')
    userEntry = Entry(loginFrame)
    userEntry.grid(row=1,column=1,sticky='w')
    pwdEntry = Entry(loginFrame)
    pwdEntry.grid(row=2,column=1,sticky='w')

    Button(loginFrame,text="Reset",command = loginClicked).grid(row=3,column=0,pady=10)
    Button(loginFrame,text="Login",command = loginClicked).grid(row=3,column=1,pady=10)
    loginFrame.grid(row=0,column=0,columnspan=4,rowspan=4,sticky='news')

def loginClicked():
    print()
    

def checkoutPage(root):
    loginFrame.grid_forget()
    checkoutFrame.rowconfigure((0,1,2,3,4,5,6),weight=1)
    checkoutFrame.columnconfigure((0,1,2,3),weight=1)

    Label(checkoutFrame,text="Movie",bg="#B5C0D0").grid(row=0,column=0)
    Label(checkoutFrame,text="Amount",bg="#B5C0D0").grid(row=0,column=1)
    Label(checkoutFrame,text="Price",bg="#B5C0D0").grid(row=0,column=2)
    Label(checkoutFrame,text="Total",bg="#B5C0D0").grid(row=0,column=3)

    for i in range(len(movies)):
        Label(checkoutFrame,image=movies[i],text=moviesName[i],compound='top',bg="#B5C0D0").grid(row=i+1,column=0)
        Label(checkoutFrame,text="Amount",bg="#B5C0D0").grid(row=i+1,column=1)
        Label(checkoutFrame,text="Price",bg="#B5C0D0").grid(row=i+1,column=2)
        Label(checkoutFrame,text="Total",bg="#B5C0D0").grid(row=i+1,column=3)

    Checkbutton(checkoutFrame,text="Discount for Membership",bg="#B5C0D0").grid(row=4,column=0,columnspan=4)
    Button(checkoutFrame,text="Checkout",bg="#B5C0D0",width=10).grid(row=5,column=1)
    Button(checkoutFrame,text="Back",bg="#B5C0D0",width=10).grid(row=5,column=2)
    checkoutFrame.grid(row=0,column=0,columnspan=4,rowspan=4,sticky='news')

def seatPage(root):
    seatFrame.rowconfigure((0,1,2,3),weight=1)
    seatFrame.columnconfigure((0,1),weight=1)
    Label(seatFrame,text="Seat",bg="#FFE6E6").grid(row=1,column=0,sticky='e')
    seat = ttk.Combobox(seatFrame,value=seats[0],textvariable=sspy).grid(row=1,column=1,sticky='w')
    Button(seatFrame,text="Buy",bg="#FFE6E6",width=10).grid(row=3,column=0)
    seatFrame.grid(row=0,column=0,columnspan=4,rowspan=4,sticky='news')

# def occupy():


#---------main-------------------
connection()
root = mainWindow()
userInfo,pwdInfo,sspy = StringVar(),StringVar(),StringVar()
movie1Img = PhotoImage(file="images/movie1.png").subsample(2,2)
movie2Img = PhotoImage(file="images/movie2.png").subsample(2,2)
movie3Img = PhotoImage(file="images/movie3.png").subsample(2,2)
movies = [movie1Img,movie2Img,movie3Img]
moviesName = ["Your Name","Weathering with You","Suzume no Tojimari"]
price = [160,220,280]
seat1=["A1","A2","A3","A4","A5","B1","B2","B3","B4","B5"]
seat2=["A1","A2","A3","A4","A5","B1","B2","B3","B4","B5"]
seat3=["A1","A2","A3","A4","A5","B1","B2","B3","B4","B5"]
seats = [seat1,seat2,seat3]
loginFrame = Frame(root,bg="#FFBE98")
checkoutFrame = Frame(root,bg="#222831")
seatFrame = Frame(root,bg="#FFE6E6")
loginPage(root)
# checkoutPage(root)
# seatPage(root)
root.mainloop()