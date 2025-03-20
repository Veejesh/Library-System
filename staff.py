#CREATE A CLASS STAFF THAT INHERITS FROM BOOK 
from book import Book,os,clear_terminal,verify_date_format #import Book class from book.py
#Import os,clear_terminal,verify_date_format from book.py
from user import User #import User class from user.py
import datetime #import datetime from library
#Create a Class Staff
class Staff(Book):
    #Initialise the attributes of the class
    def __init__(self,title, author, ISBN, category, publisher, publication_year, copies, location, status,
                 firstname,lastname,age,email,phone,address,dob,username,password):
        super().__init__(title, author, ISBN, category, publisher, publication_year, copies, location, status)
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
        self.email=email
        self.phone=phone
        self.address=address
        self.dob=dob
        self.username=username
        self.password=password
    #Static method to return book based on isbn and username
    @staticmethod
    def return_book():
        #add book back to table transaction
        # update transaction table attribute return ok
        #check returning date
        
        #enter details to retrieve record
        username = input("Enter username of user : ")
        #call funtion view_user_profile from User class to display user profile
        User.view_user_profile(username)
        print()
        ISBN=input("Enter ISBN of book to be returned :")
        
      
        #open book.txt to extract data and populate it into a 2D list by removing \n and ,
        book_file=open("book.txt","r")
        book_list=[]
        #process of extracting data to list
        for i in book_file.readlines():
            book_list.append(i.strip().split(","))
        #loop into list to find match ISBN and update the number of copies by 1 as book has been returned
        for i in range(1,len(book_list)):
            if (book_list[i][2])==ISBN:
                book_list[i][6]=str(int(book_list[i][6])+1)
                break
        book_file.close()
        
        #Re-write into book.txt with updated copies    
        book_file = open("book.txt", "w")
        for book in book_list:
            for i in range(len(book)):
                book_file.write(book[i])
                if i < len(book) - 1:
                    book_file.write(",")  # Add commas between elements
            book_file.write("\n")  # Move to the next line
        book_file.close()
        
        
        #open transactions.txt to find the same ISBN and username ,then we set the status from borrowed to returned
        transactions_file=open("transactions.txt", "r")
        transactions_list=[]
        for i in transactions_file.readlines():
           transactions_list.append(i.strip().split(","))
           
        transactions_file.close()
        #intialse date as we need to verify if date returned is before deadline or not
        date=""
        for i in transactions_list:
            if i[2]==str(ISBN) and i[1]==str(username) and i[5]=="Borrowed":
                i[5]="Returned"
                break
            else:
                print()
                print("Book already Returned")
                return
        #from transaction file,we extract data and search for the data set to be returned and set it to variable date
        for j in transactions_list:
            if j[1]==str(username):
                date=j[4]
                break
        #Re-Write transaction data from list to transactions.txt with updated record
        transactions_file=open("transactions.txt","w")
        for transactions in transactions_list:
            for i in range(len(transactions)):
                transactions_file.write(transactions[i])
                if i < len(transactions) - 1:
                    transactions_file.write(",")  # Add commas between elements
            transactions_file.write("\n")  # Move to the next line
        transactions_file.close()
        
        #from date variable, we remove space
        date=date.replace(" ","")    
        j=""      
        #loop into date to concatenate it into new variable j
        for i in date:
            j=j+i
        #another variable time is set to integer where the last two number are taken which is date yyyy-mm-dd
        time=int(j[-2:]) 
        #from a library call datetime, we import date for actual date
        today = str(datetime.date.today())
        #split it into list by "-"
        list = today.split('-')
        #we take only the date
        day = list[2]
        #convert it into integer
        day = int(day)
        #we check for > or < 
        if day>time:
            print("Additional charge of Rs100 for late return")
        else:
            print("Book returned on time")
    #functin to add user to the system
    def register_user(self):
        #verify if the file user.txt exist
        if os.path.exists("user.txt"):
            #if yes, we open to read the data
            user_file=open("user.txt","r")
            # we extract the last line to find the id
            last_line=user_file.readlines()[-1]
            number=last_line.strip().split(",")
            #if no data entered ,id is set to 0 which will be used as id+1 when registering new user
            if number[0]=="ID":
                id=0
            else:
                #if file exist we take the id and still use id+1  when registering new use
                id=int(number[0])
            user_file.close()
        else:
            #if file does not exist, we create it with the attribute and set id by 0
            user_file=open("user.txt","w")
            user_file.write("ID,FIRSTNAME,LASTNAME,AGE,EMAIL,PHONE,ADDRESS,DOB,USERNAME,PASSWORD\n")
            id=0
            user_file.close()
        #init user_exist as false to verify if user exist,set to true
        user_exist=False
        #open user.txt file to read all data by removing \n and ,
        user_file=open("user.txt","r")
        user_list=[]
        for i in user_file.readlines():
            user_list.append(i.strip().split(","))
        user_file.close()
        
        #loop into appended 2D List to find if user already exist,set user_exist to true or not 
        for i in user_list: 
            if str(self.username) == i[8]:
                print("User already exist")
                user_exist=True
                break   
        #if false # we append if into user.txt file with the attribute required    
        if user_exist==False:
                    user_file=open("user.txt","a")
                    user_file.write(f"{id+1},{self.firstname},{self.lastname},{self.age},{self.email},{self.phone},{self.address},{self.dob},{self.username},{self.password}\n")
                    print("Entered Successfull")
                    user_file.close()
    #function to delete a user from the the system
    def delete_user():
        #call funtion display user available at library 
        check=Book.display_user()
        if check==True:
            return
        print()
        #selection of id from list
        id=input("Enter user ID to be removed :")
        #process to delete book by id
        file_user = open("user.txt", "r")
        #append data from user.txt to 2D List user_list
        user_list = []
        for line in file_user.readlines():
            user_list.append(line.strip().split(","))
        
        #loop into user_list where id is found we remove all its data
        for i in range(1, len(user_list)):
            if user_list[i][0] == id:
                user_list.pop(i)
                print("Removed successful")
                break        
        file_user.close()
        
        #Re-write into user.txt file with the updated 2D List
        file_user = open("user.txt", "w")
        for user in user_list:
            for i in range(len(user)):
                file_user.write(user[i])
                if i < len(user) - 1:
                    file_user.write(",")  # Add commas between elements
            file_user.write("\n")  # Move to the next line
        file_user.close()
    #Function to make changes to user details whose data has already been registered
    def modify_user_details():
        #-----------------------------------#
        #we display user as well as return a boolean value if no user availble
        check=Book.display_user()
        clear_terminal()
        print()
        #boolean value check return true,no user found ,we exit the function
        if check==True:
            return
        #else we request the details
        
        #OPEN user.txt to extract data and put it into 2D List
        file_user = open("user.txt", "r")
        user_list = []
        for line in file_user:
            user_list.append(line.strip().split(","))
        file_user.close()
        
        #Use a while loop to allow multiple time to modify user details
        field="-1" 
        while field!="8":
            #display users
            Book.display_user()
            print()
            #A funtion to validate only available id to be selected
            def get_existing_id():
                print("SELECT USER'S ID FIRST ")
                while True:
                    id = input("Enter user ID to be updated: ")
                    for i in range(1,len(user_list)):
                        if id in user_list[i][0]:
                            found=True
                            return id
                        else:
                            found=False
                    if found==False:
                        print("ID not found. Please enter a valid ID.")
                        
            #return the correct id and set to variable id               
            id=get_existing_id()
            clear_terminal()
        
            #OPTION AVAILABLE TO MODIFY
            print("Field Option Available")
            print(F"{"1: FIRSTNAME":<30} {"5: PHONE"}")
            print(F"{"2: LASTNAME":<30} 6: ADDRESS")
            print(F"{"3: AGE":<30} 7: DOB")
            print(F"{"4: EMAIL":<30} 8: USERNAME")
            print(F"9: To Exit")
            print()
            #SELECT OPTION
            field = input("Enter field to be updated: ")
            
            
            
            #Case statement to match id and field choice and do the necessary changes
            match field.lower(): 
                #if field is 1, we update the first name          
                case "1":
                    for i in range(len(user_list)):
                        if user_list[i][0] == id:
                            user_list[i][1] = input("Enter new First Name: ")
                #if field is 2, we update the last name
                case "2":
                    for i in range(len(user_list)):
                        if user_list[i][0] == id:
                            user_list[i][2] = input("Enter new Last Name: ")
                #if field is 3, we update the age
                case "3":
                    for i in range(len(user_list)):
                        if user_list[i][0] == id:
                            user_list[i][3] = input("Enter new Age: ")
                #if field is 4, we update the email
                case "4":
                    for i in range(len(user_list)):
                        if user_list[i][0] == id:
                            user_list[i][4] = input("Enter new Email: ")
                #if field is 5, we update the phone           
                case "5":
                    for i in range(len(user_list)):
                        if user_list[i][0] == id:
                            user_list[i][5] = input("Enter new Phone: ")
                #if field is 6, we update the address           
                case "6":
                    for i in range(len(user_list)):
                        if user_list[i][0] == id:
                            user_list[i][6] = input("Enter new Address: ")
                #if field is 7, we update the date of birth
                case "7":
                    for i in range(len(user_list)):
                        if user_list[i][0] == id:
                            #call funtion verify_date_format to validate date
                            user_list[i][7] = verify_date_format()
                #if field is 8, we update the username            
                case "8":
                    for i in range(len(user_list)):
                        if user_list[i][0] == id:
                            user_list[i][8] = input("Enter new  Username: ")
                #if field is 9, we exit the function
                case "9":
                    return
            #once modify done , Re-Write it back to the user.txt file with changes made
            file_user = open("user.txt", "w")
            #process to write into file   
            for i in user_list:
                record = ""
                #loop into list to append data
                for j in range(len(i)):
                    record = record + "," + i[j]
                record = record.strip(",")
                file_user.write(record + "\n")    
            file_user.close()
            clear_terminal()
            #Ask if user want to continue to modify more
            print("Do you want to continue to modify more ?")
            print("Press 1 For YES\nPress 2 To  Exit")
            option=input("Enter option Here => ")
            if option=="2":
                return
            
       