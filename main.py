import colorama
 from colorama import Fore, Back, Style
 colorama.init(autoreset=True)
 class color:
    BLACK = '\033[90m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
 employ=[]
 def insertemp():
    import pickle
    f=open("employ.dat","ab+")
    employ=[]
    ans=1
    while(ans!=0):
        employ=[]
        i=int(input("\nEnter Id(5 digit no.): "))
        employ.append(i)
        name=input("Enter Name: ")
        employ.append(name)
        sal=float(input("Enter Salary: "))
        employ.append(sal)
        desig=input("Enter Designation: ")
        employ.append(desig)
        pickle.dump(employ,f)
        ans=int(input(Fore.RED + "\nDo you want to enter more: "))
    f.close()
 def displayemp():
    import pickle
    f=open("employ.dat","rb+")
    bnm=[]
    found=0
    print (color.BOLD + color.RED + "\n\n\t\t\t\t\t\tLIST OF EMPLOYEES ")
    
print("_____________________________________________________________________________
 ____________________________________________________\n\n")
    print(color.BLUE+ color.BOLD+"{}\t\t\t{}\t\t\t{}\t\t\t{}".format('EMP. ID','EMP.
 NAME','EMP. SALARY','EMP. DESIGNATION'))
    
print("_____________________________________________________________________________
 _____________________________________________________")
    print(color.BOLD)
    try:
        while True:
            bnm=pickle.load(f)
            
print("\n{}\t\t\t{}\t\t\t\t\t\t{}\t\t\t\t\t{}".format(bnm[0],bnm[1],bnm[2],bnm[3]))
    except EOFError:
        pass
    f.close()
 def searchemp():
    import pickle
    f=open("employ.dat","rb+")
    cvb=[]
    i=int(input("\nEnter the id of the employee to be searched: "))
    found=0
    try:
        while True:
            cvb=pickle.load(f)
            if(cvb[0]==i):
                print("\n",cvb)
                found=1
    except EOFError:
        if(found==0):
            print(Fore.RED + "\nEmployee not found!")
 def modifyemp():
    import pickle
    f=open("employ.dat","rb")
    t=open("employee.dat","wb")
    zxc=[]
    i=int(input(Fore.BLUE + "\nEnter the id of the employee whose details have to be
 modified: "))
    found=0
    try:
        while True:
            zxc=pickle.load(f)
            if(zxc[0]!=i):
                found=1
                pickle.dump(zxc,t)
            else:
                zxc[1]=input("\nEnter new name: ")
                zxc[2]=float(input("Enter new salary: "))
                zxc[3]=input("Enter new designation: ")
                pickle.dump(zxc,t)
    except EOFError:
        if(found==0):
            print(Fore.RED + "\nProvided employee id not found!!")
    f.close()
    t.close()
    print(Fore.BLUE + " \n\nList of employees after modification:-")
    f=open("employ.dat","wb")
    t=open("employee.dat","rb")
    print (color.BOLD + color.RED + "\n\n\t\t\t\t\t\tLIST OF EMPLOYEES ")
    
print("_____________________________________________________________________________
 ____________________________________________________\n\n")
    print(color.BLUE+ color.BOLD+"{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}".format('EMP. 
ID','EMP. NAME','EMP. SALARY','EMP. DESIGNATION'))
    
print("_____________________________________________________________________________
 _____________________________________________________")
    print(color.BOLD)
    try:
        while True:
            zxc=pickle.load(t)
            pickle.dump(zxc,f)
            
print("\n{}\t\t\t{}\t\t\t\t\t{}\t\t\t\t{}".format(zxc[0],zxc[1],zxc[2],zxc[3]))
    except EOFError:
        pass
    f.close()
    t.close()   
def deleteemp():
    import pickle
    f=open("employ.dat","rb")
    t=open("tempo.dat","wb")
    li=[]
    r=int(input("Enter the employee id whose details have to be deleted: "))
    found=0
    try:
        while True:
            li=pickle.load(f)
            if(li[0]!=r):
                pickle.dump(li,t)
            else:
                print(color.RED + color.BOLD + "\nDetails of this employee has to be
 deleted: ")
                print(li)
                found=1
    except EOFError:
        if(found==0):
            print(color.BOLD + color.RED + "Provided employee id is not present in 
the record")
    f.close()
    t.close()
    print(color.BLUE + color.BOLD + "\nEmployee details left after deletion are: ")
    f=open("employ.dat","wb")
    t=open("tempo.dat","rb")
    a=[]
    print (color.BOLD + color.RED + "\n\n\t\t\t\t\t\tLIST OF EMPLOYEES ")
    
print("_____________________________________________________________________________
 ____________________________________________________\n\n")
    print(color.BLUE+ color.BOLD+"{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}".format('EMP. 
ID','EMP. NAME','EMP. SALARY','EMP. DESIGNATION'))
    
print("_____________________________________________________________________________
 _____________________________________________________")
    print(color.BOLD)
    try:
        while True:
            a=pickle.load(t)
            pickle.dump(a,f)
            print("\n{}\t\t\t{}\t\t\t\t\t{}\t\t\t\t{}".format(a[0],a[1],a[2],a[3]))
    except EOFError:
        pass
    f.close()
    t.close()
 def addroom():
    import pickle
    f4=open("HOTEL.dat","ab+")
    ans=1
    while(ans!=0):
        rec1=[]
        rono=int(input("\nEnter the room no.: "))
        rec1.append(rono)
        rtype=input("Enter the room type: ")
        rec1.append(rtype)
        rate=float(input("Enter the rate of the room: "))
        rec1.append(rate)
        status=input("Enter the status of the room: ")
        rec1.append(status)
        pickle.dump(rec1,f4)
        ans=int(input(Fore.RED + "\nDo you want to enter more(yes-1/no-0): "))
    f4.close()   
def displayroom():
    import pickle
    f=open("HOTEL.dat","rb+")
    nmc=[]
    found=0
    print (color.BOLD + color.RED + "\n\n\t\t\t\t\t\tLIST OF ROOMS ")
    
print("_____________________________________________________________________________
 ____________________________________________________\n\n")
    print(color.BLUE+ color.BOLD+"{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}".format('ROOM 
NO.','ROOM TYPE','RATE','STATUS'))
    
print("_____________________________________________________________________________
 _____________________________________________________")
    print(color.BOLD)
    try:
        while True:
            nmc=pickle.load(f)
            
print("\n{}\t\t\t\t{}\t\t\t\t\t{}\t\t\t\t{}".format(nmc[0],nmc[1],nmc[2],nmc[3]))
    except EOFError:
        pass
    f.close()
 def searchroom():
    import pickle
    f=open("HOTEL.dat","rb+")
    cvb=[]
    i=int(input("\nEnter the room no. to be searched: "))
    found=0
    try:
        while True:
            cvb=pickle.load(f)
            if(cvb[0]==i):
                print("\n",cvb)
                found=1
    except EOFError:
        if(found==0):
            print(Fore.RED + "\nRoom not found!")
 def modifyroom():
    import pickle
    f=open("HOTEL.dat","rb")
    t=open("HOTELS.dat","wb")
    zxc=[]
    i=int(input(Fore.BLUE + "\nEnter the room no. whose details have to be modified:
 "))
    found=0
    try:
        while True:
            zxc=pickle.load(f)
            if(zxc[0]!=i):
                found=1
                pickle.dump(zxc,t)
            else:
                zxc[1]=input("\nEnter the new room type: ")
                zxc[2]=float(input("Enter the new room rate : "))
                zxc[3]=input("Enter the new status of room: ")
                pickle.dump(zxc,t)
    except EOFError:
        if(found==0):
            print(Fore.RED + "\nProvided room no. is not present in the record!!")
    f.close()
    t.close()
    print(Fore.BLUE + " \n\nList of rooms after modification:-")
    f=open("HOTEL.dat","wb")
    t=open("HOTELS.dat","rb")
    print (color.BOLD + color.RED + "\n\n\t\t\t\t\t\tLIST OF ROOMS ")
    
print("_____________________________________________________________________________
____________________________________________________\n\n")
    print(color.BLUE+ color.BOLD+"{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}".format('ROOM 
NO.','ROOM TYPE','RATE','STATUS'))
    
print("_____________________________________________________________________________
 _____________________________________________________")
    print(color.BOLD)
    try:
        while True:
            zxc=pickle.load(t)
            pickle.dump(zxc,f)
            
print("\n{}\t\t\t{}\t\t\t\t\t{}\t\t\t\t{}".format(zxc[0],zxc[1],zxc[2],zxc[3]))
    except EOFError:
        pass
    f.close()
    t.close()
 def deleteroom():
    import pickle
    f=open("HOTEL.dat","rb")
    t=open("HOTELS.dat","wb")
    li=[]
    r=int(input("Enter the room no. whose details have to be deleted: "))
    found=0
    try:
        while True:
            li=pickle.load(f)
            if(li[0]!=r):
                pickle.dump(li,t)
            else:
                print(color.RED + color.BOLD + "\nDetails of this room has to be 
deleted: ")
                print(li)
                found=1
    except EOFError:
        if(found==0):
            print(color.BOLD + color.RED + "Provided room no. is not present in the 
record")
    f.close()
    t.close()
    print(color.BLUE + color.BOLD + "\nRoom details left after deletion are: ")
    f=open("HOTEL.dat","wb")
    t=open("HOTELS.dat","rb")
    a=[]
    print (color.BOLD + color.RED + "\n\n\t\t\t\t\t\tLIST OF ROOMS ")
    
print("_____________________________________________________________________________
 ____________________________________________________\n\n")
    print(color.BLUE+ color.BOLD+"{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}".format('ROOM 
NO.','ROOM TYPE','RATE','STATUS'))
    
print("_____________________________________________________________________________
 _____________________________________________________")
    print(color.BOLD)
    try:
        while True:
            a=pickle.load(t)
            pickle.dump(a,f)
            print("\n{}\t\t\t{}\t\t\t\t\t{}\t\t\t\t{}".format(a[0],a[1],a[2],a[3]))
    except EOFError:
        pass
    f.close()
    t.close()
 def displaycustomer():
    import pickle
    temp=open("abc.dat","rb+")
    emp=[]
    found=0
    print (color.BOLD + color.RED + "\n\n\t\t\t\t\t\tDETAILS OF CUSTOMERS ")
    
print("_____________________________________________________________________________
 ____________________________________________________________________________________
 ____\n\n")
    print(color.BLUE+ 
color.BOLD+"{}\t\t\t{}\t\t\t{}\t\t\t{}\t{}\t\t{}\t\t{}\t\t{}".format('NAME','EMAIL 
ID','PHONE','CHECK IN','CHECK OUT','ADULTS','CHILDREN','BILL NO.'))
    
print("_____________________________________________________________________________
 ____________________________________________________________________________________
 ____")
    print(color.BOLD)
    try:
        while True:
            emp=pickle.load(temp)
            
print("{}\t\t{}\t\t{}\t\t{}\t{}\t\t{}\t\t{}\t\t\{}".format(emp[0],emp[1],emp[2],emp[
 3],emp[4],emp[5],emp[6],emp[7]))
    except EOFError:
        pass
    temp.close()   
def employee():
    some=1
    while (some!=0):
        print(color.DARKCYAN + "\n\n\nWhat would you like to do?")
        print("\n1. Add new employee details")
        print("2. Display list of employees")
        print("3. Search for an employee")
        print("4. Modify details of an existing employee")
        print("5. Delete details of an existing employee")
        print("6. Exit")
        chac=int(input(Fore.GREEN + "\nEnter your choice: "))
        if(chac==1):
            insertemp()
        elif(chac==2):
            displayemp()
        elif(chac==3):
            searchemp()
        elif(chac==4):
            modifyemp()
        elif(chac==5):
            deleteemp()
        elif(chac==6):
            some=0
        else:
            print(Fore.RED + "\nWRONG CHOICE")
 def room():
    somes=1
    while (somes!=0):
        print(color.DARKCYAN + "\n\n\nWhat would you like to do?")
        print("\n1. Add new room details")
        print("2. Display list of rooms")
        print("3. Search for a room")
        print("4. Modify details of an existing room")
        print("5. Delete details of a room")
        print("6. Exit")
        char=int(input(Fore.GREEN + "\nEnter your choice: "))
        if(char==1):
            addroom()
        elif(char==2):
            displayroom()
        elif(char==3):
            searchroom()
        elif(char==4):
            modifyroom()
        elif(char==5):
            deleteroom()
        elif(char==6):
            somes=0
        else:
            print(Fore.RED + "\nWRONG CHOICE")
 def customers():
    ellipse=1
    while(ellipse!=0):
        print(color.DARKCYAN + "\n\nWhich section would you like to review: ")
        print(color.BOLD + "\n1. List of customers")
        print(color.BOLD + "2. Exit")
        chara=int(input(Fore.GREEN + color.BOLD + "\nEnter your choice: "))
        if (chara==1):
            displaycustomer()
        elif(chara==2):
            ellipse=0
        else:
            print(Fore.RED + "\nYOU HAVE ENTERED A WRONG CHOICE!! ")
 def admin():
    answer=1
    while(answer!=0):
        print(color.DARKCYAN + "\n\nWhich section would you like to review: ")
        print(color.BOLD + "\n1. Employees")
        print(color.BOLD + "2. Rooms ")
        print(color.BOLD + "3. Customers")
        print(color.BOLD + "4. Exit")
        cha=int(input(Fore.GREEN + color.BOLD + "\nEnter your choice: "))
        if (cha==1):
            employee()
        elif(cha==2):
            room()
        elif(cha==3):
            customers()
        elif(cha==4):
            main()
        else:
            print(Fore.RED + "\nYOU HAVE ENTERED A WRONG CHOICE!! ")           
def customer():
    abc=[]
    chi=[]
    f=0
    np=0
    import pickle
    f1=open("abc.dat","ab+")
    name=input("Enter your name:")
    abc.append(name)
    print("Hi",name,"!!!Please tell the following details for your stay in our 
hotel!")
    email=input("Enter your email:")
    abc.append(email)
    phoneno=int(input("Enter your number:"))
    abc.append(str(phoneno))
    checkin=input("Enter the check in date in format DD/MM/YYYY:")
    abc.append(str(checkin))
    checkout=input("Enter the check out date in format DD/MM/YYYY:")
    abc.append(str(checkout))
    adults=int(input("Enter the number of adults:"))
    abc.append(str(adults))
    child=int(input("Enter the number of children:"))
    abc.append(str(child))
    global room   
    for i in range(child):
        age=int(input("Enter the age of children:"))
        chi.append(age)
    for j in chi:
        if (j>10):
            np=np+1
    if ((adults+np)==1):
        room=1
    else:
        if ((adults+np)%2==0):
            room=(adults+np)//2
        else:
            room=(adults+np+1)//2
    print(color.DARKCYAN+ color.BOLD+"According to number of family members, you 
need to book {} rooms!!".format(room)+color.END)
    bl=[]
    trooms=[]
    def roominfo():
        pht=int(input("Select the room which you want to view:\n(1)STANDARD 
ROOM\n(2)DELUX ROOM\n(3)SUITE ROOM\nChoice:"))
        if (pht==1):
            root = Tk()
            root.geometry("1400x2500")
            photo = PhotoImage(file="STANDARD.png")
            varu= Label(image=photo)
            varu.pack()
            root.mainloop()
        elif (pht==2):
            root = Tk()
            root.geometry("1600x2500")
            photo = PhotoImage(file="DELUX.png")
            varu= Label(image=photo)
            varu.pack()
            root.mainloop()
        elif (pht==3):
            root = Tk()
            root.geometry("1300x1000")
            photo = PhotoImage(file="SUITE.png")
            varu = Label(image=photo)
            varu.pack()
            root.mainloop()
        else:
            print("\nPlease enter a valid choice!!\n")
            roominfo()
        ap=int(input("Do you want to view any other room?(1-yes/any key-no): "))
        if (ap==1):
            roominfo()
    answ=int(input("If you want to learn about the rooms, enter 1 , else enter any 
other number : "))    
    if (answ==1):
        roominfo()
    global found
    found=0
    def booking():
        global room
        found=0
        li=[]
        import pickle
        temp=open("HOTEL.dat","rb+")
        cho=int(input(color.BLACK+ color.BOLD+"Do you want\n (1)STANDARD ROOM - Rs 
2500/-\n (2)DELUX ROOM - Rs 3500/-\n(3)SUITE ROOM - Rs 5000/-\n"))
        if (cho==1):
            try:
                while True:
                    emp=pickle.load(temp)
                    if ((found==0) and (emp[1]=="STANDARD") and (emp[3]=='FREE')):
                        print(color.GREEN+ color.BOLD+"YOUR ROOM NO. IS",emp[0])
                        emp[3]='OCCUPIED'
                        found=1
                        li.append(emp)
                        trooms.append(emp)
                        print(color.PURPLE+ color.BOLD+"Your one room has been 
booked!")
                        bl.append(2500)
                    else:
                        li.append(emp)
                temp.close()
            except EOFError:
                pass
        elif (cho==2):
            try:
                while True:
                    emp=pickle.load(temp)
                    if ((found==0) and (emp[1]=="DELUX") and (emp[3]=="FREE")):
                        print(color.GREEN+ color.BOLD+"YOUR ROOM NO. IS",emp[0])
                        emp[3]='OCCUPIED'
                        li.append(emp)
                        trooms.append(emp)
                        found=1
                        print(color.PURPLE+ color.BOLD+"Your one room has been 
booked!")
                        bl.append(3500)
                    else:
                        li.append(emp)
                temp.close()
            except EOFError:
                pass
        elif (cho==3):
            try:
                while True:
                    emp=pickle.load(temp)
                    if ((found==0) and  (emp[1]=="SUITE") and (emp[3]=="FREE")):
                        print(color.GREEN+ color.BOLD+"YOUR ROOM NO. IS",emp[0])
                        emp[3]='OCCUPIED'
                        li.append(emp)
                        trooms.append(emp)
                        found=1
                        print(color.PURPLE+ color.BOLD+"Your one room has been 
booked!")
                        bl.append(5000)
                    else:
                        li.append(emp)
                temp.close()
            except EOFError:
                pass
        else:
            print("Please enter a valid choice!")
            booking()
        temp=open("HOTEL.dat","wb")
        for i in li:
            pickle.dump(i,temp)
        temp.close()
        if (found==0):
            global room
            answer=int(input("Sorry! The room you are trying to book is not 
available right now! Do you want to try booking other room?(1-yes/0-no)"))
            if (answer==0):
                print(color.RED+color.BOLD+"Sorry for the inconvenience! Please try 
booking again after rooms are available..")
                quit()
            elif (answer==1):
                rom=room-len(trooms)
                for i in range(rom):
                    booking()
            else:
                print(color.RED + color.BOLD +"Please enter a valid choice!"+ 
color.END)
                ans()
    def run(a):
        for i in range (a):
            if (len(trooms)==room):
                break
            else:
                booking()
    run(room-len(trooms))
    amount=sum(bl)
    print (color.BLACK+color.BOLD+"\n\n\t\t\t\t\tBILL GENERATION ")
    
print("*****************************************************************************
 ******************\n\n")
    print(color.RED+ color.BOLD+"{}\t\t{}\t\t\t{}\t\t\t{}".format('ROOM NO.','ROOM 
TYPE','PRICE','NUMBER OF ROOMS')+color.END)
    
print("_____________________________________________________________________________
_________________")
    print(color.BOLD)
    for i in trooms:
            print("\n{}\t\t\t{}\t\t\t\t{}\t\t\t{}".format(i[0],i[1],i[2],1))
    print("\n\n\n\t\t\tAmount payable = Rs.",amount,"/-\n")
    a=email.split('@')
    b=a[0].upper()
    import random
    r = random.randint(10000, 99999)
    n=b+str(r)
    print(color.BLACK+color.BOLD+"\t\t\tThe bill no. = ",n,"\n")
    abc.append(n)
    if (bl!=0):
        pickle.dump(abc,f1)
        f1.close()
    print(color.RED+color.BOLD+"\nTHANKING YOU FOR BOOKING FROM OUR HOTEL!!!\n\nWE 
HOPE THAT YOU HAVE AN ENJOYABLE STAY")      
    exit()
 from tkinter import *
 def review():
    class color:
            BLACK='\033[90m'
            PURPLE='\033[95m'
            CYAN='\033[96m'
            DARKCYAN='033[36m'
            BLUE='\033[94m'
            GREEN='\033[92m'
            YELLOW='\033[93m'
            RED='\033[91m'
            BOLD='\033[1m'
            UNDERLINE='\0u33[4m'
            END='\033[0m'    
    def display():
        import pickle
        f=open("review.dat",'rb+')
        rec=[]
        found=0
        try:
            while True:
                rec=pickle.load(f)
                print(rec[1],'\n',rec[2],'\n',rec[3])
                print("\n")    
        except EOFError:
            pass
        print(color.RED+ color.BOLD+ "HOPE IT WOULD HAVE BEEN HELPFUL FOR YOU. 
PLEASE DO VISIT IT IF YOU HAVEN'T..THANK YOU!!!!")
        f.close()   
    def add():
        class color:
            BLACK = '\033[90m'
            YELLOW = '\033[93m'
            BOLD = '\033[1m'
            RED='\033[91m'
        import pickle
        f=open("review.dat","ab+")
        t=open('abc.dat','rb')
        rec=[]
        found=0
        b=input("enter bill no.")
        rec.append(b)
        try:
            while True:
                n=pickle.load(t)
                if (n[7]==b):
                    rec.append(n[0])
                    found=1
        except EOFError:
            if (found==0):
                print("Invalid bill no.")
                ans=int(input("Do you want to try again?(yes-1/no-any key):"))
                if (ans==1):
                    add()
                else:
                    quit()
        r=int(input("how many ratings out of 5 do you want to add??"))
        if(r<=5):
            if(r==0):
                print(color.BLACK+color.BOLD+"*****")
                rec.append(color.BLACK+color.BOLD+"*****")
            if(r==1):
                print(color.YELLOW+color.BOLD+"*"+color.BLACK+color.BOLD+"****")
                
rec.append(color.YELLOW+color.BOLD+"*"+color.BLACK+color.BOLD+"****")          
            elif(r==2):
                print(color.YELLOW+color.BOLD+"**"+color.BLACK+color.BOLD+"***")
                
rec.append(color.YELLOW+color.BOLD+"**"+color.BLACK+color.BOLD+"***")
            elif(r==3):
                print(color.YELLOW+color.BOLD+"***"+color.BLACK+color.BOLD+"**")
                
rec.append(color.YELLOW+color.BOLD+"***"+color.BLACK+color.BOLD+"**")
            elif(r==4):
                print(color.YELLOW+color.BOLD+"****"+color.BLACK+color.BOLD+"*")
                
rec.append(color.YELLOW+color.BOLD+"****"+color.BLACK+color.BOLD+"*")
            else :
                print(color.YELLOW+color.BOLD+"*****")
                rec.append(color.YELLOW+color.BOLD+"*****") 
        else:
            print(color.RED+color.BOLD+"INVALID RATINGS")
        rev=input("Enter review:")
        rec.append(rev)
        pickle.dump(rec,f)
    def modify():
        import pickle
        f=open("review.dat",'rb')
        t=open("temp5.dat",'wb')
        b=input("enter bill number:")
        found=0
        try:
            while True:
                rec=pickle.load(f)
                if(rec[0]!=b):
                    pickle.dump(rec,t)
                else:
                    a=input("enter new review")
                    rec[3]=a
                    pickle.dump(rec,t)
                    found=1
        except EOFError:
            if(found==0):
                print("record not found")
        f.close()
        t.close()
        f=open("review.dat","wb")
        t=open("temp5.dat","rb")
        try:
            while True:
                rec=pickle.load(t)
                pickle.dump(rec,f)
        except EOFError:
            pass
        f.close()
        t.close()
    def modifyr():
        class color:
            BLACK = '\033[90m'
            YELLOW = '\033[93m'
            BOLD = '\033[1m'
            RED='\033[91m'
            END = '\033[0m'
        import pickle
        f=open("review.dat",'rb')
        t=open("temp5.dat",'wb')
        rec=[]
        b=input("enter your bill no.")
        found=0
        try:
            while True:
                rec=pickle.load(f)
                if(rec[0]!=b):
                    pickle.dump(rec,t)
                else:
                    r=int(input("enter new  ratings "))
                    if(r<=5):
                        if(r==0):
                            a=color.BLACK+color.BOLD+"*****"
                        if(r==1):
                            
a=color.YELLOW+color.BOLD+"*"+color.BLACK+color.BOLD+"****"
                        elif(r==2):
                            
a=color.YELLOW+color.BOLD+"**"+color.BLACK+color.BOLD+"***"
                        elif(r==3):
                            
a=color.YELLOW+color.BOLD+"***"+color.BLACK+color.BOLD+"**"
                        elif(r==4):
                           
a=color.YELLOW+color.BOLD+"****"+color.BLACK+color.BOLD+"*"
                        else:
                            a=color.YELLOW+color.BOLD+"*****"
                        rec[2]=a
                        print(rec[2])
                    else:
                        print(color.RED+color.BOLD+"INVALID RATINGS")
                    pickle.dump(rec,t)
                    found=1
        except EOFError:
            if(found==0):
                print("record not found")
        f.close()
        t.close()
        f=open("review.dat","wb")
        t=open("temp5.dat","rb")
        try:
            while True:
                rec=pickle.load(t)
                pickle.dump(rec,f)
        except EOFError:
            pass
        f.close()
        t.close()
    def deleter():
        class color:
            RED = '\033[91m'
        import pickle
        f=open("review.dat","rb")
        t=open("temp5.dat","wb")
        rec=[]
        b=input("enter your bill no:")
        found=0
        try:
            while True:
                rec=pickle.load(f)
                if(rec[0]!=b):
                    pickle.dump(rec,t)
                else:
                    print(color.RED+"Your review has been deleted sucessfully!")
        except EOFError:
            pass
        f.close()
        t.close()
        f=open("review.dat","wb")
        t=open("temp5.dat","rb")
        try:
            while True:
                rec=pickle.load(t)
                pickle.dump(rec,f)
        except EOFError:
            pass
        f.close()
        t.close()
            
    print (color.BLACK+color.BOLD+"\n1.Display Review \n2.Add your review  \n3. 
Modify review  \n4. Modify ratings\n5. Delete review and rating\n6. Exit\n ")
    ch=int(input("Enter your choice-"))
    if(ch==1):
        display()
    elif(ch==2):
        add()
    elif(ch==3):
        modify()
    elif(ch==4):
        modifyr()
    elif(ch==5):
        deleter()
    elif(ch==6):
        main()
    else:
        print(color.RED+'\nWRONG CHOICE\n')
 def main() :
    import pygame
    from pygame import mixer
    pygame.mixer.init()
    mixer.music.load("uni.mp3")
    mixer.music.set_volume(0.03)
    mixer.music.play(-1)
    print(color.BLUE + color.BOLD + "\n\t\t\t\tHOTEL AUGUSTUS WELCOMES 
YOU\t\t\t\t\t")
    print(color.DARKCYAN + 
"___________________________________________________________________________________
 __________")
    print()
    print()
    print(color.BOLD + "1. \t Administrator\n")
    print(color.BOLD + "2. \t Customer\n")
    print(color.BOLD + "3. \t Reviews\n")
    print(color.BOLD + "4. \t Exit\n\n")
    ch=int(input(color.BOLD + Fore.GREEN + "\nWhich section would you like to visit?
 "))
    keys=1
    while(keys!=0):
        if(ch==1):
            print(color.BOLD + Fore.MAGENTA + "\n\n\t\t\tWELCOME ADMININSTRATOR !")
            print(color.BOLD + Fore.MAGENTA + 
"______________________________________________________________________")
            admin()
        elif(ch==2):
            print(color.BOLD + Fore.MAGENTA + "\n\n\t\t\tWELCOME CUSTOMER !")
            print(color.BOLD + Fore.MAGENTA + 
"______________________________________________________________________")
            customer()
        elif(ch==3):
            print(color.BOLD + Fore.MAGENTA + "\n\n\t\t\tWELCOME TO REVIEWS SECTION 
!")
            print(color.BOLD + Fore.MAGENTA + 
"______________________________________________________________________")
            review()
        elif(ch==4):
            keys==0
        else:
            print(Fore.RED + "\nYOU HAVE ENTERED A WRONG CHOICE!")
 main()
       
