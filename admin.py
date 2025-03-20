#CREATE Admin Class Inherit from Staff Class and Book Class
#Funtion of Admin Class : remove_book,view_user_details=> for all users,generate_report,system_rules,transaction_history => for all users,register_staff,delete_staff
from staff import Staff,os #import Staff class and os from staff.py
from book import clear_terminal #import Book Class and clear_terminal function from book.py

#Admin Class
class Admin(Staff):
    #initialise init
    def __init__(self,firstname,lastname,age,email,phone,address,dob,username,password):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
        self.email=email
        self.phone=phone
        self.address=address
        self.dob=dob   
        self.username=username
        self.password=password
    #function to remove book    
    def remove_book():
       
        #call funtion display book as well as assign the return value to check
        check=Staff.display_book()
        print()
        #boolean value check return true,no book found ,we exit the function
        if check==True:
            return
        #else we request the details
        ISBN=input("Enter Book ISBN to be removed :")
         
        #OPEN book.txt to extract data and put it into 2D List while removing the \n and split it by ,
        book_file=open("book.txt","r")
        book_list = []
        for line in book_file.readlines():
            book_list.append(line.strip().split(","))
        
        #loop into book_list where ISBN is found we remove all its data
        for i in range(1, len(book_list)):
            if book_list[i][2] == ISBN:
                book_list.pop(i)
                break
            else:
                print("Not Found")
        book_file.close()
        #Re-write into book.txt file with the updated 2D List
        #Reference Chatgpt to we-write it.
        book_file = open("book.txt", "w")
        for book in book_list:
            for i in range(len(book)):
                book_file.write(book[i])
                if i < len(book) - 1:
                    book_file.write(",")  # Add commas between elements
            book_file.write("\n")  # Move to the next line
        book_file.close()
    #Function to view all users with each one having there own transaction history    
    def view_user_details():
        #open both file user.txt and transaction.txt
        file_user = open("user.txt", "r")
        file_transaction = open("transactions.txt", "r")
        #Read into user.txt and put it into content variable
        user_detail=file_user.readlines()
        #From user_detail, we read starting 2 line check it data exist or not
        if not user_detail[1:]:
            #if not print output and exit the function
            print("No user found in the library.")
            file_user.close()
            file_transaction.close()
            return
            
        #if exist populate data from file to a 2D List by removing \n and ,
        user_list = []
        for i in user_detail:
            user_list.append(i.strip().split(","))
            
        #loop into user list and for each user ,we go to its transaction
        for i in range(1, len(user_list)):
            #each user details
            print(f"User {i} {user_list[i][8]}")
            print(f"{"-"*50}")
            print(f"Name :{user_list[i][1]} {user_list[i][2]}")
            print(f"Age  :{user_list[i][3]}")
            print(f"Email: {user_list[i][4]} | Phone :{user_list[i][5]}")
            print(f"Address :{user_list[i][6]}")
            print(f"DOB :{user_list[i][7]}")
            print()
            #inner loop user tranction
            found=False
            file_transaction=open("transactions.txt","r")
            print("---------------Transactions History------------------")
            print(f"{"BOOK ISBN":<15} {"DATE Borrowed/Returned":<25} {"STATUS":<10}")
            for j in file_transaction.readlines():
                user_attribute=j.strip().split(",")
                #if transaction recorded,print it 
                if user_list[i][8] == user_attribute[1]:
                    #format needed here
                    print(f"{user_attribute[2]:<15} {user_attribute[4]:<25} {user_attribute[5]:<10}")
                    found=True
            if found==False:
                    #if not continue to next user_attribute
                    print("No Transaction Occured")
                    print()
            print()
            file_transaction.close()
        file_user.close()
        
    #Funtion to generate report by printing number of users,book,staff and transaction  
    def generate_report():
        #open all file user.txt,transaction.txt,staff.txt,book.txt to read
        file_user = open("user.txt", "r")
        file_transaction = open("transactions.txt", "r")
        file_staff = open("staff.txt", "r")
        file_book = open("book.txt", "r")
        #before looping into each file,set number of line to 0 to count each file line
        number_of_lines=0
        #loop in user file
        for i in file_user:
            number_of_lines += 1
        print(f"Number of User registered: {number_of_lines-1}")
        
        number_of_lines=0
        #loop in transaction file
        for i in file_transaction:
            number_of_lines += 1
        print(f"Number of Transactions made: {number_of_lines-1}")
        
        number_of_lines=0
        #loop into staff file
        for i in file_staff:
            number_of_lines += 1
        print(f"Number of Staff registered: {number_of_lines-1}")
        number_of_lines=0
        #loop into book file
        for i in file_book:
            number_of_lines += 1
        print(f"Number of Books in library: {number_of_lines-1}")
        file_user.close()
        file_book.close()
        file_transaction.close()
        file_staff.close()   
    #Funtion to add or view system Rules set by the admin    
    def system_rules():
        #Open system_rules.txt file to read and write
        if os.path.exists("system_rules.txt"):
            file_rules = open("system_rules.txt", "r+")
        else:
            file_rules = open("system_rules.txt", "w")
        #Provide two option either to view or to add rules
        print("1 :To View System Rules\n2 :To add Rules")
        option=int(input("Enter option: "))#Enter option here
        clear_terminal()#clear terminal screen
        #If option is 1 ,We print the rules available
        if option==1:
            #we verify if file contain information ,if not we exit
            if (os.stat('system_rules.txt').st_size == 0) == True:
                print("No Rules set as of now ,Thank You")
                return
            else:
                print("----------------RULES SET IN LIBRARY----------------------")
                print(F"{"-"*50}")
                #Loop into file_rules by reading each line
                for i in file_rules.readlines():
                    #We remove \n 
                    rule=i.strip()
                    #Print the rule 
                    print(rule)
        #IF option is 2, We request number of rules to add
        elif option==2:
            #Request the number of rule
            number_lines = input("Enter number of rules to be added:")
            #Loop through the number of rules
            for i in range(int(number_lines)):
                #for Line ,We enter the rule
                line = input("Enter rule:")
                file_rules.write(line + "\n")
        file_rules.close()    
    #Function to see all transaction made in the library regarding borrowing and returning of book
    def transaction_history():
        clear_terminal()#Clear the screen
        #open transactions.txt to read date from
        file_transaction = open("transactions.txt", "r")
        print()
        #Format printing 
        print(f"{"-"*40}Transaction History{"-"*40}")
        #Loop through the transaction file line by line
        for i in file_transaction.readlines():
            #Remove the \n and split each data by ,
            transaction_attribute=i.strip().split(",")
            #if in the first position of the line has id , the format is different compared to other id
            if transaction_attribute[0]=="id":
                print()
                print(f"{transaction_attribute[0]:<5} {transaction_attribute[1]:<20} {transaction_attribute[2]:<20} {transaction_attribute[3]:<25} {transaction_attribute[4]:<15} {transaction_attribute[5]:<10}")
                print("-"*100)
            else:
                print(f"{transaction_attribute[0]:<5} {transaction_attribute[1]:<20} {transaction_attribute[2]:<20} {transaction_attribute[3]:<25} {transaction_attribute[4]:<15} {transaction_attribute[5]:<10}")
    #Funtion to Register staff into the system where without the registration by an admin ,the menu Staff cannot be accessed as username and password are set by admin           
    def register_staff(self):
        #Verify if the file exist or not?
        if os.path.exists("staff.txt"):
            #If file exist, open the file, read the last line entered and from that line, we take the id that is at position 0
            staff_file=open("staff.txt","r")
            last_line=staff_file.readlines()[-1]
            #Extraction is done by removing the \n and ,
            number_id=last_line.strip().split(",")
            #If the id from last line is ID ,we assume that not staff has not been registered and we set id to 0
            if number_id[0]=="ID":
                id=0
            else:
            #if ID is a digit ,We take that digit
                id=int(number_id[0])          
        else:
            #If file does not exist we create it and add first line as follows
            staff_file=open("staff.txt","w")
            staff_file.write("ID,FIRSTNAME,LASTNAME,AGE,EMAIL,PHONE,ADDRESS,DOB,USERNAME,PASSWORD\n")
            #We set id to 0
            id=0
            staff_file.close()
        #as the file exist or just created, we verify if the firstname match record ,if yes staff exist and staff_exist is set to true
        staff_exist=False
        staff_file=open("staff.txt","r")
        staff_list=[]
        #loop into file and append into a 2D List
        for i in staff_file.readlines():
            staff_list.append(i.strip().split(","))
        staff_file.close()
        #Verify the firstname
        for i in staff_list: 
            if str(self.firstname) == i[1]:
                print("staff already exist")
                staff_exist=True    
        #If staff does not exist,we add it to the system and id +1       
        if staff_exist==False:
                    staff_file=open("staff.txt","a")
                    staff_file.write(f"{id+1},{self.firstname},{self.lastname},{self.age},{self.email},{self.phone},{self.address},{self.dob},{self.username},{self.password}\n")
                    print("Entered Successfull")
                    staff_file.close()
    #Funtion to delete staff on the system
    def delete_staff():
        #call funtion display book
        #Return true if not staff found
        check=Staff.display_staff()
        print()
        #If check is true , we exit the funtion
        if check==True:
            return
        
        #selection of id from list
        id=input("Enter staff ID to be removed :")
        #process to delete book by id
        file_staff = open("staff.txt", "r")
        #Read into staff file and populate it into a 2D List
        staff_list = []
        for line in file_staff.readlines():
            staff_list.append(line.strip().split(","))
            
        #Based on id entered we remove all its data
        for i in range(1, len(staff_list)):
            if staff_list[i][0] == id:
                staff_list.pop(i)
                print("Removed successful")
                break        
        file_staff.close()
        #Re-write new data into the file
        file_staff = open("staff.txt", "w")
        for staff in staff_list:
            for i in range(len(staff)):
                file_staff.write(staff[i])
                if i < len(staff) - 1:
                    file_staff.write(",")  # Add commas between elements
            file_staff.write("\n")  # Move to the next line
        file_staff.close()
 