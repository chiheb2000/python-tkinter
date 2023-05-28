from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import re

home = Tk()


home.geometry("900x600")
home.title('ATAST')
home.resizable(height=False,width=False)
fnom=''

###############################################Page Home##########################################################

def acc():
    canvas2.delete("all")
   
    canvas2.create_text(430, 40, text="Welcome To our Club", font=("Helvetica", 24, "bold"), fill="orange")
    login = Button(home, text="To Log in",  font=("Helvetica", 10, "bold"),bg="blue", fg="white" ,command=log)
    canvas2.create_window(620, 25, anchor="nw", window=login)
    new = Button(home, text="Create new account",  font=("Helvetica", 10, "bold"),bg="green", fg="white",command=Register)
    canvas2.create_window(700, 25, anchor="nw", window=new)
    ex = Button(home, text="Exit",font=("Helvetica", 10, "bold") , bg="red", fg="white", command=home.destroy)
    canvas2.create_window(850, 25, anchor="nw", window=ex)
    canvas2.create_image(250,70, anchor="nw", image=ll)
    team = Button(home, text="Our  Team",  font=("Helvetica", 10, "bold"),bg="#FFFFE4", fg="black",command=lambda:Team(fnom))
    canvas2.create_window(40, 80, anchor="nw", window=team)
    about = Button(home, text="About Us",  font=("Helvetica", 10, "bold"),bg="#FFFFE4", fg="black",command=lambda:aboutus(fnom))
    canvas2.create_window(40, 120, anchor="nw", window=about)
    act = Button(home, text="Our past events and participations",  font=("Helvetica", 10, "bold"),bg="#FFFFE4", fg="black",command=lambda:acty(fnom))
    canvas2.create_window(40, 160, anchor="nw", window=act)
    ifest = Button(home, text="I-FEST COMPETITION",  font=("Helvetica", 10, "bold"),bg="#FFFFE4", fg="black",command=lambda:Ifest(fnom))
    canvas2.create_window(40, 200, anchor="nw", window=ifest)
    contact = Button(home, text="Contact Us",  font=("Helvetica", 10, "bold"),bg="#FFFFE4", fg="black",command=lambda:contactus(fnom))
    canvas2.create_window(40, 240, anchor="nw", window=contact)

    
###############################################ifest##########################################################
def Ifest(fnom):
    # Effacer le canvas existant
    canvas2.delete("all")
    if fnom=='':
        button2 = Button(home, text="Home",font=("Helvetica", 12) , bg="orange", fg="white", command=acc)
        canvas2.create_window(0, 0, anchor="nw", window=button2)
        ex = Button(home, text="Exit",font=("Helvetica", 12) , bg="red", fg="white", command=home.destroy)
        canvas2.create_window(850, 0, anchor="nw", window=ex)
    else:
        button2 = Button(home, text="Home",font=("Helvetica", 12) , bg="orange", fg="white", command=lambda:welecome(fnom))
        canvas2.create_window(0, 0, anchor="nw", window=button2)
        logout = Button(home, text="To Log out",  font=("Helvetica", 12, "bold"),bg="red", fg="white" ,command=acc)
        canvas2.create_window(800, 0, anchor="nw", window=logout)

    canvas2.create_image(580,0, anchor="nw", image=ifest)
    canvas2.create_text(320,130, text="I-FEST2 NATIONAL ", font=("Helvetica", 25, "bold"), fill="red")
    canvas2.create_text(290,170, text="COMPETITION", font=("Helvetica", 25, "bold"), fill="black")
    canvas2.create_text(310,210, text="The International Festival of Engineering Science and Technology in Tunisia,", font=("Helvetica", 12, "bold"), fill="black")
    canvas2.create_text(355,240, text="is a 9-day-festival organized by ATAST,open for all students between the ages of 14 and 24.", font=("Helvetica", 12, "bold"), fill="black")
    canvas2.create_image(140,270, anchor="nw", image=ifest1)
 
 
###############################################Contactus##########################################################

def contactus(fnom):
    # Effacer le canvas existant
    canvas2.delete("all")
    if fnom=='':
        button2 = Button(home, text="Home",font=("Helvetica", 12) , bg="orange", fg="white", command=acc)
        canvas2.create_window(0, 0, anchor="nw", window=button2)
        ex = Button(home, text="Exit",font=("Helvetica", 12) , bg="red", fg="white", command=home.destroy)
        canvas2.create_window(850, 0, anchor="nw", window=ex)
    else:
        button2 = Button(home, text="Home",font=("Helvetica", 12) , bg="orange", fg="white", command=lambda:welecome(fnom))
        canvas2.create_window(0, 0, anchor="nw", window=button2)
        logout = Button(home, text="To Log out",  font=("Helvetica", 12, "bold"),bg="red", fg="white" ,command=acc)
        canvas2.create_window(800, 0, anchor="nw", window=logout)

    canvas3 = Canvas(home, bg="white", width=500, height=200)
    canvas2.create_window(200,100, anchor="nw", window=canvas3)
    canvas3.create_text(260, 20, text="Contact : ", font=("Helvetica", 20, "bold"), fill="black")
    canvas3.create_text(250, 80, text="e-mail: epi.atastclub@gmail.com", font=("Helvetica", 20, "bold"), fill="orange")
    canvas3.create_text(250,150, text="phone: +216 24 611 837", font=("Helvetica", 20, "bold"), fill="orange")    

    
###############################################Page activity##########################################################

def acty(fnom):
    canvas2.delete("all")
    if fnom=='':
        button2 = Button(home, text="Home",font=("Helvetica", 12) , bg="orange", fg="white", command=acc)
        canvas2.create_window(0, 0, anchor="nw", window=button2)
        ex = Button(home, text="Exit",font=("Helvetica", 12) , bg="red", fg="white", command=home.destroy)
        canvas2.create_window(850, 0, anchor="nw", window=ex)
    else:
        button2 = Button(home, text="Home",font=("Helvetica", 12) , bg="orange", fg="white", command=lambda:welecome(fnom))
        canvas2.create_window(0, 0, anchor="nw", window=button2)
        logout = Button(home, text="To Log out",  font=("Helvetica", 12, "bold"),bg="red", fg="white" ,command=acc)
        canvas2.create_window(800, 0, anchor="nw", window=logout)

    
    canvas2.create_text(150, 70, text="Participants in I-FEST competition", font=("Helvetica", 13, "bold"), fill="orange")
    canvas2.create_image(20,100, anchor="nw", image=ab1)
    canvas2.create_image(320,100, anchor="nw", image=ab3)
    canvas2.create_text(450, 70, text="Robotics WORKSHOP", font=("Helvetica", 14, "bold"), fill="orange")
    canvas2.create_image(600,100, anchor="nw", image=ab2)
    
    canvas2.create_text(730, 70, text="Info Session", font=("Helvetica", 14, "bold"), fill="orange")

    canvas2.create_image(20,300, anchor="nw", image=ab4)
    
###############################################aboutus##########################################################
    
def aboutus(fnom):
    canvas2.delete("all")
    if fnom=='':
        
        button2 = Button(home, text="Home",font=("Helvetica", 12) , bg="orange", fg="white", command=acc)
        canvas2.create_window(0, 0, anchor="nw", window=button2)
        ex = Button(home, text="Exit",font=("Helvetica", 12) , bg="red", fg="white", command=home.destroy)
        canvas2.create_window(850, 0, anchor="nw", window=ex)
    else:
        button2 = Button(home, text="Home",font=("Helvetica", 12) , bg="orange", fg="white", command=lambda:welecome(fnom))
        canvas2.create_window(0, 0, anchor="nw", window=button2)
        logout = Button(home, text="To Log out",  font=("Helvetica", 12, "bold"),bg="red", fg="white" ,command=acc)
        canvas2.create_window(800, 0, anchor="nw", window=logout)

    canvas2.create_text(460, 50, text="WHAT IS ATAST ?", font=("Helvetica", 25, "bold"), fill="red")

    canvas2.create_text(440, 100, text="ATAST is more then association, it's a concept, a family. Founded especially for you. ", font=("Helvetica", 14), fill="black")
    canvas2.create_text(450, 140, text="Be ATASTIEN,Open your mind feed it science and technology for Tunisia,the world and for all Humanity ", font=("Helvetica", 14), fill="black")
    canvas2.create_text(440, 190, text="ATAST:THINK AGAIN...BE DIFFERENT!!!", font=("Helvetica", 14,"bold"), fill="orange")

    canvas2.create_image(50,250, anchor="nw", image=aa)
    canvas2.create_image(530,250, anchor="nw", image=ab)
    
###############################################Team##########################################################

def Team(fnom):
    canvas2.delete("all")
    if fnom=='':
        
        button2 = Button(home, text="Home",font=("Helvetica", 12) , bg="orange", fg="white", command=acc)
        canvas2.create_window(0, 0, anchor="nw", window=button2)
        ex = Button(home, text="Exit",font=("Helvetica", 12) , bg="red", fg="white", command=home.destroy)
        canvas2.create_window(850, 0, anchor="nw", window=ex)
    else:
        button2 = Button(home, text="Home",font=("Helvetica", 12) , bg="orange", fg="white", command=lambda:welecome(fnom))
        canvas2.create_window(0, 0, anchor="nw", window=button2)
        logout = Button(home, text="To Log out",  font=("Helvetica", 12, "bold"),bg="red", fg="white" ,command=acc)
        canvas2.create_window(800, 0, anchor="nw", window=logout)
        
    canvas2.create_image(210,10, anchor="nw", image=team)
    

###############################################Page user##########################################################

    
def welecome(fnom):
    canvas2.delete("all")
    
    
    
    canvas2.create_image(250,70, anchor="nw", image=ll)

    canvas2.create_text(450, 40, text="Welcome," + fnom  , font=("Helvetica", 24, "bold"), fill="orange")
    login = Button(home, text="To Log out",  font=("Helvetica", 12, "bold"),bg="red", fg="white" ,command=acc)
    canvas2.create_window(800, 0, anchor="nw", window=login)
  
    team = Button(home, text="Our  Team",  font=("Helvetica", 10, "bold"),bg="#FFFFE4", fg="black",command=lambda:Team(fnom))
    canvas2.create_window(40, 80, anchor="nw", window=team)
    about = Button(home, text="About Us",  font=("Helvetica", 10, "bold"),bg="#FFFFE4", fg="black",command=lambda:aboutus(fnom))
    canvas2.create_window(40, 120, anchor="nw", window=about)
    act = Button(home, text="Our past events and participations",  font=("Helvetica", 10, "bold"),bg="#FFFFE4", fg="black",command=lambda:acty(fnom))
    canvas2.create_window(40, 160, anchor="nw", window=act)
    ifest = Button(home, text="I-FEST COMPETITION",  font=("Helvetica", 10, "bold"),bg="#FFFFE4", fg="black",command=lambda:Ifest(fnom))
    canvas2.create_window(40, 200, anchor="nw", window=ifest)
    contact = Button(home, text="Contact Us",  font=("Helvetica", 10, "bold"),bg="#FFFFE4", fg="black",command=lambda:contactus(fnom))
    canvas2.create_window(40, 240, anchor="nw", window=contact)
    news = Button(home, text="News",  font=("Helvetica", 10, "bold"),bg="#FFFFE4", fg="black",command=lambda:new(fnom))
    canvas2.create_window(40, 280, anchor="nw", window=news)
    
###############################################Page notification##########################################################

def new(fnom):
    canvas2.delete("all")
    
    back = Button(home, text="Home",  font=("Helvetica", 12, "bold"),bg="orange", fg="white" ,command=lambda:welecome(fnom))
    canvas2.create_window(0, 0, anchor="nw", window=back)
    logout = Button(home, text="To Log out",  font=("Helvetica", 12, "bold"),bg="red", fg="white" ,command=acc)
    canvas2.create_window(800, 0, anchor="nw", window=logout)
    
    canvas4 = Canvas(home, bg="white", width=350, height=400)
    canvas2.create_window(30,50, anchor="nw", window=canvas4)
    canvas4.create_text(120, 20, text="Meeting on 30/03/2023: ", font=("Helvetica", 15, "bold"), fill="red")
    canvas4.create_text(130, 50, text="Start of meeting: 2 p.m.", font=("Helvetica", 15), fill="black")
    canvas4.create_text(150, 90, text="IMPORTANT POINTS :", font=("Helvetica", 13), fill="black")
    canvas4.create_text(170, 150, text="-Discussed on event with atast club isitcom. ", font=("Helvetica", 13), fill="black")
    canvas4.create_text(160, 200, text="-Discuss our opening plan of our CLUB.", font=("Helvetica", 13), fill="black")
    canvas4.create_text(180, 260, text="-Our participation in the robotics competition  ", font=("Helvetica", 13), fill="black")
    canvas4.create_text(150, 290, text="on 07/05/2023 at ENIM.", font=("Helvetica", 13), fill="black")
    
    canvas5 = Canvas(home, bg="white", width=350, height=400)
    canvas2.create_window(430,50, anchor="nw", window=canvas5)
    canvas5.create_text(120, 20, text="Meeting on 09/04/2023: ", font=("Helvetica", 15, "bold"), fill="red")
    canvas5.create_text(130, 50, text="Start of meeting: 10:30 p.m.", font=("Helvetica", 15), fill="black")
    canvas5.create_text(150, 90, text="IMPORTANT POINTS :", font=("Helvetica", 13), fill="black")
    canvas5.create_text(150, 130, text="-The workshops and activities planned for", font=("Helvetica", 12), fill="black")
    canvas5.create_text(150, 150, text="our next action in favor of children, which ", font=("Helvetica", 12), fill="black")
    canvas5.create_text(170, 170, text=" will be held on 04/14/2023 from 1 p.m. to 4 p.m.", font=("Helvetica", 12), fill="black")
    canvas5.create_text(150, 210, text="The scheduled workshops are : ", font=("Helvetica", 13, "bold"), fill="black")
    canvas5.create_text(130, 240, text="• Robotics workshop", font=("Helvetica", 13), fill="black")
    canvas5.create_text(170, 260, text="• Mini-kitchen + DIY workshop", font=("Helvetica", 13), fill="black")
    canvas5.create_text(130, 280, text="• Scratch workshop", font=("Helvetica", 13), fill="black")
    canvas5.create_text(140, 310, text="The planned activities are:", font=("Helvetica", 13, "bold"), fill="black")
    canvas5.create_text(140, 340, text="• Animation / Music", font=("Helvetica", 13), fill="black")
    canvas5.create_text(190, 360, text="• Movie (Big Hero) / documentary", font=("Helvetica", 13), fill="black")
    canvas5.create_text(120, 380, text="• Coffee break", font=("Helvetica", 13), fill="black")




    
    
    
###############################################Page authentification##########################################################

def aut(email,passw):
    em = email.get()
    password = passw.get()
     
    if em in users:
       user=users[em]
       if user[2] == password:
            messagebox.showinfo("Hello", user[0])
            welecome(user[0])
       else:
           
           messagebox.showerror("Error","verify your information!!!")
        
    else:
        messagebox.showerror("Error","verify your information!!!")
        
           
            
###############################################Page Login##########################################################
            
    
def log():
    canvas2.delete("all")
   

    canvas2.create_text(470, 50, text="Login to your account", font=("Helvetica", 20, "bold"), fill="black")


    label_nom = Label(home, text="Email :", font=("verdana",10,"italic bold"),bg="#EEEEC9")
    email = Entry(home, font=("Helvetica", 14))
    canvas2.create_window(320, 100, anchor="nw", window=label_nom)
    canvas2.create_window(400, 100, anchor="nw", window=email)

    label_passw = Label(home, text="Password :", font=("verdana",10,"italic bold"),bg="#EEEEC9")
    passw = Entry(home, font=("Helvetica", 14),show="*")
    canvas2.create_window(300, 180, anchor="nw", window=label_passw)
    canvas2.create_window(400, 180,  anchor="nw",window=passw)

    button_submit = Button(home, text="To Log in", font=("Helvetica", 12), bg="blue", fg="white", command=lambda:aut(email,passw))
    canvas2.create_window(450, 230, anchor="nw", window=button_submit)
    canvas2.create_text(380,300, text="Don't have an account?", anchor="nw", font=("Helvetica", 12), fill="black")
    button_new=Button(home, text="Create an Account", font=("Helvetica", 11), bg="green", fg="white", command=Register)
    canvas2.create_window(550, 295, anchor="nw", window=button_new)
    # Ajouter un bouton "Retour" en bas de la page
    button2 = Button(home, text="Home",font=("Helvetica", 13) , bg="orange", fg="white", command=acc)
    canvas2.create_window(0, 0, anchor="nw", window=button2)
    ex = Button(home, text="Exit",font=("Helvetica", 12) , bg="red", fg="white", command=home.destroy)
    canvas2.create_window(860, 0, anchor="nw", window=ex)

###############################################procedure submit##########################################################

def submit(lnom,fnom,passw,nom,classe,combo):
    lnom = lnom.get()
    fnom = fnom.get()
    pss = passw.get()
    email = nom.get()
    tel = classe.get()
    etablissement = combo.get()

    l=[]

    if fnom=='' :
        messagebox.showwarning("Error", "Your first name PLS!!")
    elif lnom=='' :
        messagebox.showwarning("Error", "Your Last name PLS!!")
    elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        messagebox.showwarning("Error", "Invalid email address!")
    elif pss=='':
        messagebox.showwarning("Error", "Invalid pass!")
    elif tel=='':
        messagebox.showwarning("Error", "Invalid Class")
    elif not etablissement:
        messagebox.showwarning("Error", "Please select your Establishment!!")
           

    else:
          if email in users:
              
             messagebox.showerror("Error","Email is already Used.")
          else:
                messagebox.showinfo("Success", "Your form has been submitted successfully!")
                welecome(fnom)
                l.append(fnom)
                l.append(email)
                l.append(pss)
                users[email] = l
                print(users)  
###############################################Page new account##########################################################
   
def Register():

    canvas2.delete("all")
   

    canvas2.create_text(450, 50, text="Register", font=("Helvetica", 24, "bold"), fill="black")

    label_nom = Label(home, text="First name :", font=("verdana",10,"italic bold"),bg="#EEEEC9")
    fnom = Entry(home, font=("Helvetica", 14))
    canvas2.create_window(100, 100, anchor="nw", window=label_nom)
    canvas2.create_window(200, 100, anchor="nw", window=fnom)

    label_lnom = Label(home, text="Last name :", font=("verdana",10,"italic bold"),bg="#EEEEC9")
    lnom = Entry(home, font=("Helvetica", 14))
    canvas2.create_window(500, 100, anchor="nw", window=label_lnom)
    canvas2.create_window(600, 100, anchor="nw", window=lnom)

    label_email = Label(home, text="Email :", font=("verdana",10,"italic bold"),bg="#EEEEC9")
    nom = Entry(home, font=("Helvetica", 14))
    canvas2.create_window(100, 160, anchor="nw", window=label_email)
    canvas2.create_window(200, 160, anchor="nw", window=nom)


    label_passw = Label(home, text="Password :", font=("verdana",10,"italic bold"),bg="#EEEEC9")
    passw = Entry(home, font=("Helvetica", 14))
    canvas2.create_window(500, 160, anchor="nw", window=label_passw)
    canvas2.create_window(600, 160,  anchor="nw",window=passw)
 
    label_class = Label(home, text="Class :", font=("verdana",10,"italic bold"),bg="#EEEEC9")
    classe = Entry(home, font=("Helvetica", 14))
    canvas2.create_window(100, 220, anchor="nw", window=label_class)
    canvas2.create_window(200, 220,  anchor="nw",window=classe)
 
    label_fac = Label(home, text="Establishment :", font=("verdana",10,"italic bold"),bg="#EEEEC9")
    combo = ttk.Combobox(home, values=["EPI-Business School", "EPI DIGITAL SCHOOL", "EPI-Polytechnique"])
    canvas2.create_window(500, 220, anchor="nw", window=label_fac)
    canvas2.create_window(650, 220,  anchor="nw",window=combo)


    button_submit = Button(home, text="To Log in", font=("Helvetica", 12), bg="green", fg="white",command=lambda: submit(lnom,fnom,passw,nom,classe,combo))
    canvas2.create_window(400, 280, anchor="nw", window=button_submit)
   
    button2 = Button(home, text="Home",font=("Helvetica", 12) , bg="orange", fg="white", command=acc)
    canvas2.create_window(0, 0, anchor="nw", window=button2)
    ex = Button(home, text="Exit",font=("Helvetica", 12) , bg="red", fg="white", command=home.destroy)
    canvas2.create_window(860, 0, anchor="nw", window=ex)
    
###############################################varible global##########################################################

logo = PhotoImage(file="logo.png")
atast = PhotoImage(file="atast.png")
bgm = PhotoImage(file="aa.png")
team = PhotoImage(file="membre.png")
ll = PhotoImage(file="EpiLogo2 (3).png")
aa = PhotoImage(file="lg.png")
ab = PhotoImage(file="ab.png")
ab1 = PhotoImage(file="1.png")
ab2 = PhotoImage(file="info session A0 (1).png")
ab3 = PhotoImage(file="3.png")
ab4 = PhotoImage(file="4.png")
ifest = PhotoImage(file="ifest.png")
ifest1 = PhotoImage(file="5.png")
# Create Canvas
canvas1 = Canvas(home, width=900, height=80)
canvas2 = Canvas(home, width=900, height=480)
canvas3 = Canvas(home, width=900, height=40)
canvas1.create_image(60, 20, image=logo)
canvas1.create_image(450, 30, image=atast)
canvas1.create_image(850, 30, image=bgm)
canvas1.place(x='0',y='0')
canvas2.place(x='0',y='80')
canvas3.place(x='0',y='560')
canvas1['bg']='#E9E996'
canvas2['bg']='#FFFFE4'
canvas3['bg']='#DCDCDC'
canvas3.create_text(450, 20, text="© 2023 - ATAST", font=("Helvetica", 12, "bold"), fill="red")


users = {
    "chiheb@gmail.com": ["chiheb", "chiheb@gmail.com", "123"],
    }
acc()
# Execute tkinter
home.mainloop()
