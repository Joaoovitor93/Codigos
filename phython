
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
                    
