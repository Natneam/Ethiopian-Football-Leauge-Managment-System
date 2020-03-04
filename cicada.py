#Authors
# ===============================
# CICADA 3301
# ===============================
# Natneam Mesele --------- ATR/9672/11
# Bruk Ayalew    --------- ATR/4451/11
# Mintesinot Bezabih ----- ATR/9596/11
# Nuredin Yesuf ---------- ATR/0100/11
# Hailemariam Fekadie ---- ATR/4338/11



from tkinter import *
from tkinter import ttk
import sys
from result import *
from table import *
from fixture import *
from team_information import *
from proj import *
root = Tk()
root.title("Ethiopian Football League  Management System")
root.geometry("900x500")
root.resizable(0,0)
root.call('wm', 'iconphoto', root._w,PhotoImage(file='favicon.png'))

def adminpanel():
    adminlogframe.destroy()
    global adminpanelframe
    adminpanelframe = Frame()
    adminpanelframe.pack()
    headerLabel = Label(adminpanelframe, width = 600 , height = 3 ,\
        text = "Hello Admin", \
        bg = "lightblue" , fg = "black" ,font=('Verdana',15))
    headerLabel.pack()
    TransferBtn = Button(adminpanelframe , text ="TRANSFER AND UPDATE" , width=30 , command = insert )
    Update_result_Btn = Button(adminpanelframe  , text = "Update Result" , width = 30  , command = week1)
    Update_result_Btn.pack(ipady=15 , pady =26)
    Update_result_Btn.pack(ipady=15 , pady =26)
    TransferBtn.pack(ipady=15 , pady =100)
    def backhome():
        adminpanelframe.destroy()
        return mainwindow()
    Button(adminpanelframe , text = "Log out", width = 20 , command = backhome).pack(padx = 10 ,ipady = 10 , side = RIGHT)

def guestpanel():
    mainframe.destroy()
    global guestframe
    guestframe = Frame()
    guestframe.pack()
    headerLabel = Label(guestframe, width = 600 , height = 3 ,\
        text = "Hello User", \
        bg = "lightblue" , fg = "black" ,font=('Verdana',15))
    headerLabel.pack()

    clubsBtn = Button(guestframe , text ="Clubs" , width=30 , command = team )
    clubsBtn.pack(ipady=15 , pady =30)
    FixtureBtn = Button(guestframe ,text = "Results" , width = 30 ,  command = fweek1 )
    FixtureBtn.pack(ipady=15 , pady =30)
    TabelBtn = Button(guestframe ,text = "Table" , width = 30, command = tableintable )
    TabelBtn.pack(ipady=15 , pady =30)
    def backhome():
        guestframe.destroy()
        return mainwindow()
    Button(guestframe , text = "Home", width = 20 , command = backhome).pack(padx = 10 , ipady = 10 , side = RIGHT)

def adminlogin():
    mainframe.destroy()
    global adminlogframe
    adminlogframe = Frame()
    adminlogframe.pack(side=TOP)
    descriptionLabel = Label(adminlogframe , text = "Admin Login Form" ,\
         bg = "lightblue" , fg = "black" , width = 400 , height = 3 , font=('Verdana',15))

    nameLabel = Label(adminlogframe , text = "User name *")
    passwordLabel = Label(adminlogframe , text = "Password *")
    name = StringVar()
    password = StringVar()

    nameEntry = Entry(adminlogframe , width = 30 , textvariable = name )
    passwordEntry = Entry(adminlogframe , width = 30 , textvariable = password,show = "*")
 
    def isValid():
        if password.get() == '3301' and name.get() == 'cicada':
            return (adminpanel())
        else:
            from tkinter import messagebox as mBox
            mBox.showinfo('Ethiopian Football League  Management System' , 'wrong username or password')
    loginButton = Button(adminlogframe , text="log in", command = lambda: isValid())


    descriptionLabel.pack()

    nameLabel.pack(ipady = 10, pady = 33)
    nameEntry.pack()
    passwordLabel.pack(ipady = 10 , pady = 33)
    passwordEntry.pack()
    loginButton.pack(ipady = 3 , ipadx = 15 , pady = 33)

    def backhome():
        adminlogframe.destroy()
        return mainwindow()
    Button(adminlogframe , text = "Home", width = 20 , command = backhome).pack(padx = 10 ,ipady = 10 , side = RIGHT)


def mainwindow():
    global mainframe
    mainframe = Frame()
    mainframe.pack(side=TOP)
    headerLabel = Label(mainframe, width = 600 , height = 3 ,\
        text = "Ethiopian Football League  Management System", \
        bg = "lightblue" , fg = "black" ,font=('Verdana',15))
    headerLabel.pack(side = TOP)
    def exitwindow():
        sys.exit()
    adminBtn = Button(mainframe , text = "ADMIN" , height = 1 , width = 20 , command = adminlogin)
    gstBtn = Button(mainframe , text = "GUEST" , height = 1 , width = 20 , command = guestpanel)
    exttBtn = Button(mainframe , text = "EXIT" , height = 1 , width = 20 , command = exitwindow)

    adminBtn.pack(ipady = 10 , pady = 60)
    gstBtn.pack(ipady = 10 , pady = 60)
    exttBtn.pack(ipady = 10 , pady = 20 , padx = 20 , side=RIGHT)

mainwindow()

root.mainloop()