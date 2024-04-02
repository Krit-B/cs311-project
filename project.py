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
    userEntry.grid(row=1,column=1,sticky='w')
    pwdEntry = Entry(loginFrame,show="*",textvariable=pwdInfo)
    pwdEntry.grid(row=2,column=1,sticky='w')

    Button(loginFrame,text="Reset",command = resetInfo).grid(row=3,column=0,pady=10)
    Button(loginFrame,text="Register",command = regiswindow).grid(row=3,column=1,pady=10)
    Button(loginFrame,text="Login",command = loginClicked).grid(row=3,column=2,pady=10)
    loginFrame.grid(row=0,column=0,columnspan=4,rowspan=4,sticky='news')

def loginClicked():
    global result
    if userInfo.get()=="":
        messagebox.showwarning("Admin:","Please Enter Your Username.")
        userEntry.focus_force()
    else:
        sql = "select * from customers where user=?" #change this
        cursor.execute(sql,[userInfo.get()])
        result = cursor.fetchall()
        if result:
            if pwdInfo.get()=="":
                messagebox.showwarning("Admin:","Please ENter Your Password.")
                pwdEntry.focus_force()
            else:
                sql = "select * from customers where user=? and pwd=?" #change this
                cursor.execute(sql,[userInfo.get(),pwdInfo.get()])
                result = cursor.fetchall()
                if result:
                    messagebox.showinfo("Admin:","Login Succesfully.")
                    moviePage(result[0])
                else:
                    messagebox.showwarning("Admin:","Incorrect Password.")
                    pwdEntry.select_range(0,END)
                    pwdEntry.focus_force()
    
def resetInfo():
    userEntry.delete(0,END)
    pwdEntry.delete(0,END)

def regiswindow() : #activity of week11
    global fullname,lastname,newuser,newpwd,cfpwd,regisframe
    #loginframe.destroy()
    # root.title("Welcome to User Registration : ")
    root.config(bg='#d2e69c')
    regisframe = Frame(root,bg='#8fd9a8')
    regisframe.rowconfigure((0,1,2,3,4,5,6),weight=1)
    regisframe.columnconfigure((0,1),weight=1)
    Label(regisframe,text="Registration Form",font="Garamond 26 bold",fg='#e4fbff',compound=LEFT,bg='#28b5b5').grid(row=0,column=0,columnspan=2,sticky='news',pady=10)
    Label(regisframe,text='Full name : ',bg='#8fd9a8',fg='#f6f5f5').grid(row=1,column=0,sticky='e',padx=10)
    fullname = Entry(regisframe,width=20,bg='#d3e0ea')
    fullname.grid(row=1,column=1,sticky='w',padx=10)
    Label(regisframe,text='Last name : ',bg='#8fd9a8',fg='#f6f5f5').grid(row=2,column=0,sticky='e',padx=10)
    lastname = Entry(regisframe,width=20,bg='#d3e0ea')
    lastname.grid(row=2,column=1,sticky='w',padx=10)
    Label(regisframe,text="Username : ",bg='#8fd9a8',fg='#f6f5f5').grid(row=3,column=0,sticky='e',padx=10)
    newuser = Entry(regisframe,width=20,bg='#d3e0ea')
    newuser.grid(row=3,column=1,sticky='w',padx=10)
    Label(regisframe,text="Password : ",bg='#8fd9a8',fg='#f6f5f5').grid(row=4,column=0,sticky='e',padx=10)
    newpwd = Entry(regisframe,width=20,bg='#a1cae2',show='*')
    newpwd.grid(row=4,column=1,sticky='w',padx=10)
    Label(regisframe,text="Confirm Password : ",bg='#8fd9a8',fg='#f6f5f5').grid(row=5,column=0,sticky='e',padx=10)
    cfpwd = Entry(regisframe,width=20,bg='#a1cae2',show='*')
    cfpwd.grid(row=5,column=1,sticky='w',padx=10)
    regisaction = Button(regisframe,text="Register Submit",command=registration)
    regisaction.grid(row=6,column=0,ipady=5,ipadx=5,pady=5,sticky='e')
    fullname.focus_force()
    loginbtn = Button(regisframe,text="Back to Login",command=backToLogin)
    loginbtn.grid(row=6,column=1,ipady=5,ipadx=5,pady=5,sticky='w',padx=10)
    regisframe.grid(row=0,column=0,columnspan=4,rowspan=4,sticky='news')

def backToLogin():
    regisframe.destroy()
    loginPage()

def registration():
    # print("Hello from registration")
    if fullname.get() == "" :
        messagebox.showwarning("Admin: ","Please enter firstname")
        fullname.focus_force()
    elif lastname.get() == "" :
        messagebox.showwarning("Admin: ","Pleasse enter lastname")
        lastname.focus_force()
    elif newuser.get() == "" :
        messagebox.showwarning("Admin: ","Please enter a new username")
        newuser.focus_force()
    elif newpwd.get() == "" :
        messagebox.showwarning("Admin: ","Please enter a password")
        newpwd.focus_force()
    elif cfpwd.get() == "" :
        messagebox.showwarning("Admin: ","Please enter a confirm password")
        cfpwd.focus_force()
    else :
        sql = "select * from customers where user=?"
        cursor.execute(sql,[newuser.get()])
        result = cursor.fetchall()
        if result :
            messagebox.showerror("Admin:","The username is already exists")
            newuser.select_range(0,END)
            newuser.focus_force()
        else :
            if newpwd.get() == cfpwd.get() : #a new pwd / confirm is correct 
                #count number of customers    
                sql = "select count(*) from customers"
                cursor.execute(sql)
                result = cursor.fetchall()
                count = result[0][0]

                sql = "insert into customers values (?,?,?,?,?,?,?,?,?,?)"
                param = [count+1,fullname.get(),lastname.get(),newuser.get(),newpwd.get(),0,0,0,0,1]
                cursor.execute(sql,param)
                conn.commit()
                messagebox.showinfo("Admin:","Registration Successfully")
                newuser.delete(0,END)
                newpwd.delete(0,END)
                cfpwd.delete(0,END)
                fullname.delete(0,END)
                lastname.delete(0,END)
                backToLogin()
            else :
                messagebox.showwarning("Admin: ","Incorrect a confirm password\n Try again")
                cfpwd.selection_range(0,END)
                cfpwd.focus_force()

def moviePage(userlist):
    userinfo = userlist
    fullname = userlist[1]+" "+userlist[2]
    # print(userinfo)
    movieFrame = Frame(root,bg="#535C91")
    movieFrame.rowconfigure((0,1,2,3,4),weight=1)
    movieFrame.columnconfigure((0,1,2),weight=1)
    Label(movieFrame,bg="#070F2B").grid(row=0,column=0,columnspan=3,sticky='news')
    Label(movieFrame,text="Welcome, "+fullname,bg="#070F2B",fg="white").grid(row=0,column=0,columnspan=3,sticky='news')

    Button(movieFrame,text=moviesName[0]+"\n"+str(price[0]),compound='top',image=movies[0],command=lambda:seatPage(moviesName[0]),borderwidth=0,bg="#535C91").grid (row=1,ipady=10,column=0,sticky='news')
    Button(movieFrame,text=moviesName[1]+"\n"+str(price[1]),compound='top',image=movies[1],command=lambda:seatPage(moviesName[1]),borderwidth=0,bg="#535C91").grid (row=1,ipady=10,column=1,sticky='news')
    Button(movieFrame,text=moviesName[2]+"\n"+str(price[2]),compound='top',image=movies[2],command=lambda:seatPage(moviesName[2]),borderwidth=0,bg="#535C91").grid (row=1,ipady=10,column=2,sticky='news')

    movieFrame.grid(column=0,row=0,columnspan=4,rowspan=4,sticky='news')

def seatPage(movie):
    # print(movie)
    global seatFrame,chooseSeatFrame,selectedMovie
    selectedMovie = movie
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
        # print(moviesName[i],moviename)
        if moviesName[i] == moviename:
            return i
    return -1

def showSeatMenu():
    # global seatA1,seatA2,seatA3,seatA4,seatB1,seatB2,seatB3,seatB4,seatC1,seatC2,seatC3,seatC4
    # chooseSeat = ""
    # if findOption.get()=="A":
    #     chooseSeat = "seatA"
    #     seatA1=Checkbutton(chooseSeatFrame,image=seatImg,compound='top',text="Seat A1",bg="green").grid(row=0,column=0)
    #     seatA2=Checkbutton(chooseSeatFrame,image=seatImg,compound='top',text="Seat A2",bg="green").grid(row=0,column=1)
    #     seatA3=Checkbutton(chooseSeatFrame,image=seatImg,compound='top',text="Seat A3",bg="green").grid(row=0,column=2)
    #     seatA4=Checkbutton(chooseSeatFrame,image=seatImg,compound='top',text="Seat A4",bg="green").grid(row=0,column=3)
    #     seatCheck(chooseSeat)
    # elif findOption.get()=="B":
    #     chooseSeat = "seatB"
    #     seatB1=Checkbutton(chooseSeatFrame,image=seatImg,compound='top',text="Seat B1",bg="green").grid(row=0,column=0)
    #     seatB2=Checkbutton(chooseSeatFrame,image=seatImg,compound='top',text="Seat B2",bg="green").grid(row=0,column=1)
    #     seatB3=Checkbutton(chooseSeatFrame,image=seatImg,compound='top',text="Seat B3",bg="green").grid(row=0,column=2)
    #     seatB4=Checkbutton(chooseSeatFrame,image=seatImg,compound='top',text="Seat B4",bg="green").grid(row=0,column=3)
    #     seatCheck(chooseSeat)
    # elif findOption.get()=="C":
    #     chooseSeat = "seatC"
    #     seatC1=Checkbutton(chooseSeatFrame,image=seatImg,compound='top',text="Seat C1",bg="green").grid(row=0,column=0)
    #     seatC2=Checkbutton(chooseSeatFrame,image=seatImg,compound='top',text="Seat C2",bg="green").grid(row=0,column=1)
    #     seatC3=Checkbutton(chooseSeatFrame,image=seatImg,compound='top',text="Seat C3",bg="green").grid(row=0,column=2)
    #     seatC4=Checkbutton(chooseSeatFrame,image=seatImg,compound='top',text="Seat C4",bg="green").grid(row=0,column=3)
    #     seatCheck(chooseSeat)
    global seat
    seatOption = {"A":["A1","A2","A3","A4"],
                  "B":["B1","B2","B3","B4"],
                  "C":["C1","C2","C3","C4"]}

    choosenRow = findOption.get()
    slist = seatList.get(choosenRow)
    for i, seatNumber in enumerate(seatOption[choosenRow]):
        seat = Checkbutton(chooseSeatFrame,image=seatImg,compound='top',text=seatNumber,variable=slist[i],onvalue=1,offvalue=0,bg="green").grid(row=0,column=i)

    Button(chooseSeatFrame,text="Check Out",command=checkout).grid(row=2,column=0,columnspan=4)

def seatCheck(seat):
    sql = '''
            select %s from customers;
          '''%(seat)
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)

def backToMenu():
    seatFrame.destroy()
    for i in range(4):
        seatVarAList[i].set(0)
        seatVarBList[i].set(0)
        seatVarCList[i].set(0)
    moviePage(result[0])

def checkout():
    # messagebox.showinfo("Checkout","Checkout Success")
    seatA =seatList.get("A")   #local
    seatB =seatList.get("B") #local
    seatC = seatList.get("C")   #local
    
    # for i,item in enumerate(seatA):
    #     print(item.get())
    print("Checkout")

    # print(findOption.get()) #global
    # print(selectedMovie) # global
    checkoutPage(seatA,seatB,seatC)
    # seatFrame.grid_forget()


def checkoutPage(seatA,seatB,seatC):
    # loginFrame.grid_forget()
    checkoutFrame.rowconfigure((0,1,2,3,4,5,6),weight=1)
    checkoutFrame.columnconfigure((0,1,2,3),weight=1)

    # Label(checkoutFrame,text="Movie",bg="#B5C0D0").grid(row=0,column=0)
    # Label(checkoutFrame,text="Amount",bg="#B5C0D0").grid(row=0,column=1)
    # Label(checkoutFrame,text="Price",bg="#B5C0D0").grid(row=0,column=2)
    # Label(checkoutFrame,text="Total",bg="#B5C0D0").grid(row=0,column=3)

    # for i in range(len(movies)):
    #     movieImg = Label(checkoutFrame,image=movies[i],text=moviesName[i],compound='top',bg="#B5C0D0").grid(pady=20,row=i+1,column=0)
    #     Label(checkoutFrame,text="Amount",bg="#B5C0D0").grid(row=i+1,column=1)
    #     Label(checkoutFrame,text="Price",bg="#B5C0D0").grid(row=i+1,column=2)
    #     Label(checkoutFrame,text="Total",bg="#B5C0D0").grid(row=i+1,column=3)

    count = countSeat(seatA)+countSeat(seatB)+countSeat(seatC)
    
    Label(checkoutFrame,text="Checkout",bg="#B5C0D0").grid(row=0,column=0,columnspan=4)
    Label(checkoutFrame,image=movies[getIndex(selectedMovie)],bg="#B5C0D0").grid(row=1,column=0,columnspan=4)
    Label(checkoutFrame,text="Number of seats: %d"%(count),bg="#B5C0D0").grid(row=2,column=0,columnspan=4)

    Checkbutton(checkoutFrame,text="Discount for Membership",bg="#B5C0D0").grid(row=4,column=0,columnspan=4)
    Button(checkoutFrame,text="Checkout",bg="#B5C0D0",width=10).grid(row=5,column=1)
    Button(checkoutFrame,text="Back",bg="#B5C0D0",width=10).grid(row=5,column=2)
    checkoutFrame.grid(row=0,column=0,columnspan=4,rowspan=4,sticky='news')

def countSeat(seat):
    count = 0
    for i,item in enumerate(seat):
        if item == 1:
            count+=1
    return count

#---------main-------------------
connection()
root = mainWindow()
userInfo,pwdInfo,sspy = StringVar(),StringVar(),StringVar()
seatVarA1,seatVarA2,seatVarA3,seatVarA4 = IntVar(),IntVar(),IntVar(),IntVar()
seatVarB1,seatVarB2,seatVarB3,seatVarB4 = IntVar(),IntVar(),IntVar(),IntVar()
seatVarC1,seatVarC2,seatVarC3,seatVarC4 = IntVar(),IntVar(),IntVar(),IntVar()
seatVarAList = [seatVarA1,seatVarA2,seatVarA3,seatVarA4]
seatVarBList = [seatVarB1,seatVarB2,seatVarB3,seatVarB4]
seatVarCList = [seatVarC1,seatVarC2,seatVarC3,seatVarC4]
seatList = {"A":seatVarAList,"B":seatVarBList,"C":seatVarCList}
searchImg = PhotoImage(file="images\search.png")
#Should i add same larger image for moviePage ?
movie1Img = PhotoImage(file="images/movie1.png").subsample(2,2)
movie2Img = PhotoImage(file="images/movie2.png").subsample(2,2)
movie3Img = PhotoImage(file="images/movie3.png").subsample(2,2)
seatImg = PhotoImage(file="images/seat.png").subsample(10,10)
movies = [movie1Img,movie2Img,movie3Img]
moviesName = ["Your Name","Weathering with You","Suzume no Tojimari"]
price = [160,220,280]
loginFrame = Frame(root,bg="#535C91")
checkoutFrame = Frame(root,bg="#B5C0D0")
seatFrame = Frame(root,bg="#FFE6E6")
loginPage()
# checkoutPage()
# moviePage()
root.mainloop()