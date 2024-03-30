import sqlite3
from tkinter import *
from tkinter import messagebox,ttk

def connection():
    global conn,cursor
    conn = sqlite3.connect("db/customers.db")
    cursor = conn.cursor()

def mainWindow():
    root = Tk()
    w,h = 1024,900
    x = root.winfo_screenwidth()/2-w/2
    y = root.winfo_screenheight()/2-h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.config(bg="#B5C0D0")
    root.option_add("*font","Helvetica 16 bold")
    root.rowconfigure((0,1,2,3),weight=1)
    root.columnconfigure((0,1,2,3),weight=1)
    return root

def loginPage():
    global userEntry,pwdEntry
    loginFrame.rowconfigure((0,1,2,3,4),weight=1)
    loginFrame.columnconfigure((0,1,2),weight=1)

    Label(loginFrame,text = "Login",bg="#535C91").grid(row=0,column=0,columnspan=3)
    Label(loginFrame,text = "Username: ",bg="#535C91").grid(row=1,column=0,sticky='e')  
    Label(loginFrame,text = "Password: ",bg="#535C91").grid(row=2,column=0,sticky='e')
    userEntry = Entry(loginFrame,textvariable=userInfo)
    userEntry.grid(row=1,column=1,columnspan=2,sticky='w')
    pwdEntry = Entry(loginFrame,show="*",textvariable=pwdInfo)
    pwdEntry.grid(row=2,column=1,columnspan=2,sticky='w')

    Button(loginFrame,text="Reset",command = resetInfo).grid(row=3,column=0,pady=10)
    Button(loginFrame,text="Register",command = registeration).grid(row=3,column=1,pady=10)
    Button(loginFrame,text="Login",command = loginClicked).grid(row=3,column=2,pady=10)
    loginFrame.grid(row=0,column=0,columnspan=4,rowspan=4,sticky='news')

def loginClicked():
    global result
    if userInfo.get()=="":
        messagebox.showwarning("Admin:","Please Enter Your Username.")
        userEntry.focus_force()
    else:
        sql = "select * from Customers where username=?" #change this
        cursor.execute(sql,[userInfo.get()])
        result = cursor.fetchall()
        if result:
            if pwdInfo.get()=="":
                messagebox.showwarning("Admin:","Please ENter Your Password.")
                pwdEntry.focus_force()
            else:
                sql = "select * from Customers where username=? and password=?" #change this
                cursor.execute(sql,[userInfo.get(),pwdInfo.get()])
                result = cursor.fetchall()
                if result:
                    messagebox.showinfo("Admin:","Login Succesfully.")
                    welcomPage(result[0])
                else:
                    messagebox.showwarning("Admin:","Incorrect Password.")
                    pwdEntry.select_range(0,END)
                    pwdEntry.focus_force()
    
def resetInfo():
    userEntry.delete(0,END)
    pwdEntry.delete(0,END)

def registeration():
    print("this is registration page")

def checkoutPage(root):
    loginFrame.grid_forget()
    checkoutFrame.rowconfigure((0,1,2,3,4,5,6),weight=1)
    checkoutFrame.columnconfigure((0,1,2,3),weight=1)

    Label(checkoutFrame,text="Movie",bg="#B5C0D0").grid(row=0,column=0)
    Label(checkoutFrame,text="Amount",bg="#B5C0D0").grid(row=0,column=1)
    Label(checkoutFrame,text="Price",bg="#B5C0D0").grid(row=0,column=2)
    Label(checkoutFrame,text="Total",bg="#B5C0D0").grid(row=0,column=3)

    for i in range(len(movies)):
        movieImg = Label(checkoutFrame,image=movies[i],text=moviesName[i],compound='top',bg="#B5C0D0").grid(row=i+1,column=0)
        Label(checkoutFrame,text="Amount",bg="#B5C0D0").grid(row=i+1,column=1)
        Label(checkoutFrame,text="Price",bg="#B5C0D0").grid(row=i+1,column=2)
        Label(checkoutFrame,text="Total",bg="#B5C0D0").grid(row=i+1,column=3)

    Checkbutton(checkoutFrame,text="Discount for Membership",bg="#B5C0D0").grid(row=4,column=0,columnspan=4)
    Button(checkoutFrame,text="Checkout",bg="#B5C0D0",width=10).grid(row=5,column=1)
    Button(checkoutFrame,text="Back",bg="#B5C0D0",width=10).grid(row=5,column=2)
    checkoutFrame.grid(row=0,column=0,columnspan=4,rowspan=4,sticky='news')

def moviePage():

    movieFrame = Frame(root,bg="#535C91")
    movieFrame.rowconfigure((0,1,2,3,4),weight=1)
    movieFrame.columnconfigure((0,1,2),weight=1)

    Label(movieFrame,bg="#070F2B").grid(row=0,column=0,columnspan=3,sticky='news')

    Button(movieFrame,text=moviesName[0]+"\n"+str(price[0]),compound='top',image=movies[0],command=lambda:seatPage(moviesName[0]),borderwidth=0,bg="#535C91").grid (row=1,ipady=10,column=0,sticky='news')
    Button(movieFrame,text=moviesName[1]+"\n"+str(price[1]),compound='top',image=movies[1],command=lambda:seatPage(moviesName[1]),borderwidth=0,bg="#535C91").grid (row=1,ipady=10,column=1,sticky='news')
    Button(movieFrame,text=moviesName[2]+"\n"+str(price[2]),compound='top',image=movies[2],command=lambda:seatPage(moviesName[2]),borderwidth=0,bg="#535C91").grid (row=1,ipady=10,column=2,sticky='news')

    movieFrame.grid(column=0,row=0,columnspan=4,rowspan=4,sticky='news')

def seatPage(movie):
    # print(movie)
    global seatFrame,chooseSeatFrame
    seatFrame = Frame(root,bg="#535C91")
    seatFrame.rowconfigure((0,1,2,3,4,5,6,7,8),weight=1)
    seatFrame.columnconfigure((0,1,2,3),weight=1)

    chooseSeatFrame = Frame(root,bg="#535C91")
    chooseSeatFrame.rowconfigure((0,1,2),weight=1)
    chooseSeatFrame.columnconfigure((0,1,2,3),weight=1)
    chooseSeatFrame.grid(row=3,column=0,columnspan=4,sticky='news')

    Label(seatFrame,image=movies[getIndex(movie)],bg="#070F2B").grid(row=0,column=0,columnspan=4,sticky='news')
    Label(seatFrame,text=movie,bg="#070F2B",fg="#B5C0D0").grid(row=1,column=0,columnspan=4,sticky='news')
    choices = ['A','B','C']

    global findOption
    findOption = StringVar()
    findOption.set(choices[0])
    option = OptionMenu(seatFrame,findOption,*choices)
    option.grid(row=2,column=0,sticky='e')
    Button(seatFrame,image=searchImg,command=showSeatMenu,borderwidth=0,bg="#535C91").grid(row=2,column=2,sticky='w')

    Button(seatFrame,text="Back",command=backToMenu,bg="#B5C0D0",width=10).grid(row=2,column=3)
    seatFrame.grid(row=0,column=0,columnspan=4,rowspan=4,sticky='news')

def getIndex(moviename):
    for i in range(len(moviesName)):
        print(moviesName[i],moviename)
        if moviesName[i] == moviename:
            return i
    return -1

def showSeatMenu():
    global seat1,seat2,seat3,seat4
    chooseSeat = ""
    if findOption.get()=="A":
        chooseSeat = seatA
        seat1=Checkbutton(chooseSeatFrame,image=seatImg,compound='top',text="Seat A1",bg="red").grid(row=0,column=0)
        seat2=Checkbutton(chooseSeatFrame,image=seatImg,compound='top',text="Seat A2",bg="red").grid(row=0,column=1)
        seat3=Checkbutton(chooseSeatFrame,image=seatImg,compound='top',text="Seat A3",bg="red").grid(row=0,column=2)
        seat4=Checkbutton(chooseSeatFrame,image=seatImg,compound='top',text="Seat A4",bg="red").grid(row=0,column=3)
    elif findOption.get()=="B":
        chooseSeat = seatB
        seat1=Checkbutton(chooseSeatFrame,image=seatImg,compound='top',text="Seat B1",bg="red").grid(row=0,column=0)
        seat2=Checkbutton(chooseSeatFrame,image=seatImg,compound='top',text="Seat B2",bg="red").grid(row=0,column=1)
        seat3=Checkbutton(chooseSeatFrame,image=seatImg,compound='top',text="Seat B3",bg="red").grid(row=0,column=2)
        seat4=Checkbutton(chooseSeatFrame,image=seatImg,compound='top',text="Seat B4",bg="red").grid(row=0,column=3)
    elif findOption.get()=="C":
        chooseSeat = seatC
        seat1=Checkbutton(chooseSeatFrame,image=seatImg,compound='top',text="Seat C1",bg="red").grid(row=0,column=0)
        seat2=Checkbutton(chooseSeatFrame,image=seatImg,compound='top',text="Seat C2",bg="red").grid(row=0,column=1)
        seat3=Checkbutton(chooseSeatFrame,image=seatImg,compound='top',text="Seat C3",bg="red").grid(row=0,column=2)
        seat4=Checkbutton(chooseSeatFrame,image=seatImg,compound='top',text="Seat C4",bg="red").grid(row=0,column=3)
    
    Button(chooseSeatFrame,text="Check Out",command=checkout).grid(row=2,column=0,columnspan=4)

def backToMenu():
    seatFrame.destroy()
    moviePage()

def seatCheck():
    sql='''select ? from customers'''
    cursor.execute(sql,[chooseSeat])
    result = cursor.fetchall()
    print(result)

def checkout():
    messagebox.showinfo("Checkout","Checkout Success")
#---------main-------------------
connection()
root = mainWindow()
userInfo,pwdInfo,sspy = StringVar(),StringVar(),StringVar()
searchImg = PhotoImage(file="images\search.png")
movie1Img = PhotoImage(file="images/movie1.png")
movie2Img = PhotoImage(file="images/movie2.png")
movie3Img = PhotoImage(file="images/movie3.png")
seatImg = PhotoImage(file="images/seat.png").subsample(10,10)
movies = [movie1Img,movie2Img,movie3Img]
moviesName = ["Your Name","Weathering with You","Suzume no Tojimari"]
price = [160,220,280]
seatA={"A1":0,"A2":0,"A3":0,"A4":0}
seatB={"B1":0,"B2":0,"B3":0,"B4":0}
seatC={"C1":0,"C2":0,"C3":0,"C4":0}
seats = [seatA,seatB,seatC]
loginFrame = Frame(root,bg="#535C91")
checkoutFrame = Frame(root,bg="#070F2B")
seatFrame = Frame(root,bg="#FFE6E6")
loginPage()
# checkoutPage(root)
# moviePage()
root.mainloop()