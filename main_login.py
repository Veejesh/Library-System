from login_func import * #import all function from login_func.py
import time #import time module
from book import clear_terminal #import clear_terminal function from book.py
#main login system to start
def main_login():
    #Welcoming output
    print("\nHello Sir/Madam ,Welcome to Library System")
    print("------------------------------------------")
    #validate user choice
    choice = "-1"
    while choice.upper() not in ("C", "A", "S"):
        #ask to enter choice 
        print("Sign in as (C)ustomer/ (A)dmin/ (S)taff\n")
        choice=input("Enter option :")
    #If choice is customer, we provide two option to signup if not yet registered ,sign in it already registered
    if choice.upper()=="C":
        print()
        print("1: Signup\n2: signin ")
        option=int(input("Enter option here :"))
        #if option is signup, we call funtion signup(1)
        if option==1:
            signup(1)
    #If choice is staff only two option available that is if admin has registered the staff details, then they can access the staff menu else they have no other option than to exit
    if choice.upper()=="S":
        print()
        print("If Admin has not yet registered , Login Acess denied")
        print("1: SignIn\n2: To Exit ")
        option=int(input("Enter option here :"))
        if option==2:
            return True,"",""
            
       
    #DICTIONARY KEY OF C,S and A with value Customer,Staff and Admin
    user={
        "C":"Customer",
        "A":"ADMIN",
        "S":"STAFF"
    }
    clear_terminal()
    #mention each one when requsting to enter username and password
    print()
    username = input(F"Please Enter your Username {user[choice.upper()]}:\n=> ")
    print()
    password = input("Please Enter your Password:\n=> ")
    print()
    #set trial to 0 to calulate attempt
    trial = 0
    #depending on choice entered do the case 
    match choice.upper():
        #if option is customer
        case "C":
            while trial != 2:
                #call funtion login with parameter choice as c ,username "" and password ""
                result = login(choice, username, password)
                #verify if result is -1,print the output as follow and return 
                if result == -1:
                    print("No customer has been registered yet")
                    return False, choice, username
                #verify if result is false and ask again to enter username and password
                if result == False:
                    clear_terminal()
                    print("Username or password invalid")
                    print()
                    username = input("Please enter your username:\n=> ")
                    print()
                    password = input("Please enter your password:\n=> ")
                    result = login(choice, username, password)
                    trial += 1
                if result==True:
                    #else username and password is correct
                    return True, choice, username
                    break
                
            if result == -1:
                pass
            if result==False:
                #timeout if too many attempt has been done
                print("Too many unsuccessful attempts! Please wait 30s before retry")
                time.sleep(15.0)
                return main_login()
                
        case "A":
            while trial !=2:
                #call funtion login with parameter choice as A ,username "" and password ""
                result = login(choice, username, password)
                #verify if result is -1,print the output as follow and return
                if result == -1:
                    print("No admin has been registered yet")
                    return False, choice, username
                #verify if result is false and ask again to enter username and password
                if result == False:
                    clear_terminal()
                    print()
                    print("Username or Password invalid")
                    print()
                    username = input("Please Enter your Username Again:\n=> ")
                    print()
                    password = input("Please Enter your Password Again:\n=> ")
                    result=login(choice, username, password)
                    trial += 1
                if result==True:
                    #else username and password is correct
                    return True, choice, username
                
            if  result==False :
                #timeout if too many attempt has been done
                print("Too many unsuccessful attempts! Please wait 30s before retry")
                print(trial)
                time.sleep(15.0)
                return main_login()
    
        
        case "S":
            while trial != 2:
                #call funtion login with parameter choice as S ,username "" and password ""
                result = login(choice, username, password)
                #verify if result is -1,print the output as follow and return
                if result == -1:
                    print("No staff has been registered yet")
                    return False, choice, username
                #verify if result is false and ask again to enter username and password   
                if result == False:
                    clear_terminal()
                    print()
                    print("Username or password invalid")
                    print()
                    username = input("Please enter your username:\n=> ")
                    print()
                    password = input("Please enter your password:\n=> ")
                    result = login(choice, username, password)
                    trial += 1
                if result==True:
                    #else username and password is correct
                    return True, choice, username
            if result == -1:
                pass
            if result==False:
                #timeout if too many attempt has been done
                print("Too many unsuccessful attempts! Please wait 30s before retry")
                time.sleep(15.0)
                return main_login()