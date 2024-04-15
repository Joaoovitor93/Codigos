phython
import random
import time
print("\t\t\t**ONLINE AUCTION SYSTEM**\t\t\t")
i=int(input("enter the value 1 or 2 1:new user 2:exsisting user\n"))
file = open('gobi.txt','w') 
def create():
    name=str(input("Enter your name\n"))
    file.write(name)
    file.write("\n")
    contact()
    auction()
def contact():
        conno=str(input("enter your contact number\n"))
        mobno=len(conno)
        if int((mobno)==10):
            print("OTP IS SEND YOUR MOBILE NUMBER")
            contents = "1234567890"
            pw_length =1
            out= ""
            for i in range(pw_length):
                next_index = random.randrange(len(contents))
                out = out +contents[next_index]
                print(out)
                print("ENTER YOUR OTP")
                a=str(input(""))
                if a == out:
                    file.write(conno)
                    file.write("\n")
                    add=str(input("Enetr your address\n"))
                    file.write(add)
                    file.write("\n")
                    file.close()
                else:
                    print("password is wrong if you want re-enter press 1")
                    i=int(input(""))
                    if i==1:
                        contact()
                    else:
                        create()
                    
        else:
            contact()

def exsistinguser():
    name=str(input("Enter your name\n"))
    contacts()
def contacts():
    conno=str(input("enter your contact number\n"))
    mobno=len(conno)
    if int((mobno)==10):
        print("OTP IS SEND YOUR MOBILE NUMBER")
        contents = "1234567890"
        pw_length =1
        out= ""
        for i in range(pw_length):
            next_index = random.randrange(len(contents))
            out = out +contents[next_index]
            print(out)
            print("ENTER YOUR OTP")
            a=str(input(""))
            if a == out:
                auction()
            else:
                print("password is wrong if you want re-enter press 1")
                i=int(input(""))
                if i==1:
                    contacts()
            
    else:
        contacts()
def amount():
    print("online payment only")
    print("Enter your creadit card number")
    cn=str(input(""))
    cvv=str(input("enter cvv number\n"))
    lencn=len(cn)
    lencvv=len(cvv)
    if lencn==13 and lencvv==3:
        print("your payement success\n")
        print("**********************\n")
        print("The house detail are\n")
        print("**********************\n")
        print("Enter house number 1 or 2")
        count=int(input(""))
        if count==1:
            file = open('house.txt','r')
            house=file.read()
            print(house)
        else:
            file = open('house1.txt','r')
            house1=file.read()
            print(house1)
            
    else:
        amount()
def amountcar():
    print("online payment only")
    print("Enter your creadit card number")
    cn=str(input(""))
    cvv=str(input("enter cvv number\n"))
    lencn=len(cn)
    lencvv=len(cvv)
    if lencn==13 and lencvv==3:
        print("your payement success\n")
        print("**********************\n")
        print("The car details are")
        print("**********************\n")
        print("Enter car number 1 or 2")
        count=int(input(""))
        if count==1:
            file = open('car.txt','r')
            car=file.read()
            print(car)
        else:
            file = open('car1.txt','r')
            car1=file.read()
            print(car1)