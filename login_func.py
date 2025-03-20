import os #import os module
from book import verify_date_format #import verify_date_format function from book.py
from staff import Staff
   
#function to check if username is taken 
def is_username_taken(file_path, username):
    """Check if the username already exists in the file."""
    try:
        with open(file_path, "r") as file:
            for line in file:
                data = line.strip().split(",")  # Split by comma
                if len(data) >= 9 and data[8] == username:  # Username is the 9th column (index 8)
                    return True
    except FileNotFoundError:
        return False  # If file doesn't exist, assume no usernames are taken
    return False
#function to get unique username
def get_unique_username(file_path):
    """Prompt user for a unique username."""
    while True:
        username = input("Enter a username: ").strip()
        if is_username_taken(file_path, username):
            print("Username already taken, please choose another.")
        else:
            return username
#funtion to verify username and password from file to choice entered by user
def login(choice, username, password):
    #match choice
    match choice.upper():
        #If Choice is C
        case "C":
            #open file for check
            try:
                f = open("user.txt", "r")
            except:
                #if file does not exist,print the output and return
                print("File not found")
                return -1
            
            #if file is created, we check if file is empty and return
            if (os.stat('user.txt').st_size == 0) == True:
                return -1
            #if both the file is created and it contains data
            else:
                #read in file
                for line in f:
                    #split the username and password
                    list = line.strip().split(",")
                    
                    
                    #compare username and password with input
                    #if both correct ,return true as result
                    if username == list[8]:
                        if password == list[9]:
                            f.close()
                            return True
                    
            f.close()  
            #else return false as result     
            return False
        #If Choice is A        
        case "A":
            if username=="admin" and password=="1234":
                return True
            else:
                return False
        #If Choice is S
        case "S":
            #open file for check
            try:
                  f = open("staff.txt", "r")
            except:
                #if file does not exist,print the output and return
                print("File not found")
                return -1
        
            #if file is created, we check if file is empty and return
            if (os.stat('staff.txt').st_size == 0) == True:
                return -1
            #if both the file is created and it contains data
            else:
                #read in file
                for line in f:
                    #split the username and password
                    list = line.strip().split(",")
                    
            
                    #compare username and password with input
                    #if both correct ,return true as result
                    if username == list[8]:
                        if password == list[9]:
                            f.close()
                            return True
                    
            f.close()     
            #else return false as result   
            return False
        
#function to signup
def signup(option):    
    #Requestion to enter details assuming data is normal data as of now
    firstname=input("Enter First Name: ")
    lastname=input("Enter Last Name: ")
    age=input("Enter age: ")
    email=input("Enter Email: ")
    phone=input("Enter phone: ")
    address=input("Enter address: ")
    dob=verify_date_format()
    print()
    username=get_unique_username("user.txt")            
    password = input("Enter password: ")
    #validate password
    #signin(1) this lead to register new customer into the system by entering the firstname,lastname,age,email,phone,address,dob,username,password
    if option==1:
        new_user=Staff(None,None,None,None,None,None,None,None,None,firstname,lastname,age,email,phone,address,dob,username,password)#create an object
        new_user.register_user() #object to register the user
        print("Customer Account SuccessFully Created")





    

