#CREATION OF Book class which is a parent class containing function such as add_book,Issue_book,display_book,display_staff,display_user and search_book title
import os # import os library to create a function clear_terminal to refresh terminal after each funtion used

#funtion clear_terminal 
def clear_terminal():
    #in-built function to clear screen
    os.system("cls")
#A funtion to verify date format for validation
def verify_date_format():
    #use a while loop until correct format is input
    while True:
        #enter date
        date=input("Enter date Format(yyyy-mm-dd) : ")
        #check if it match 
        if len(date)==10 and date[4]=="-" and date[7]=="-":
            return date
        else:
            #if not match
            clear_terminal()
            print("Wrong Format")
            continue
#a book dictionary to locate index more easily
book_map={
            "title":0,
            "author":1,
            "ISBN":2,
            "category":3,
            "publisher":4,
            "publication_year":5,
            "copies":6,
            "location":7,
            "status":8    
        }  
#Parent Class Book
class Book():
    #initialisation of book details
    def __init__(self,title,author,ISBN,category,publisher,publication_year,copies,location,status):
        self.title=title
        self.author=author
        self.ISBN=ISBN
        self.category=category
        self.publisher=publisher
        self.publication_year=publication_year
        self.copies=copies
        self.location=location
        self.status=status
    #funtion to add book into library and store it in a file named book.txt
    def add_book(self):
        #check if the file exists      
        if os.path.exists("book.txt"):
            print("File Exists")
        else:
            #if file does not exist we create the file with the following attribute to add
            book_file=open("book.txt","w")
            book_file.write("TITLE,AUTHOR,ISBN,CATEGORY,PUBLISHER,PUBLICATION YEAR,COPIES,LOCATION,STATUS\n")
            book_file.close()
        #we set update to false to check whether book isbn already found,set to true    
        update=False
        #open book file to read
        book_file=open("book.txt","r")
        # we populate a 2D list name book_list to ADD BOOK BY REMOVING THE \n and ,
        book_list=[]
        for i in book_file.readlines():
            book_list.append(i.strip().split(","))
  
        #we loop in the 2D List and check for ISBN IF IT MATCH THE ONE ENTERED
        for i in book_list:
            #IF ISBN MATCH WE UPDATE NUMBER OF COPIES ONLY
            if i[book_map["ISBN"]]==self.ISBN:
                i[book_map["copies"]]=str(int(i[book_map["copies"]])+self.copies)
                #SET UPDATE TO TRUE AS ISBN HAS BEEN FOUND
                update=True
                break
        book_file.close()
        #After changes has been made to THE 2D LIST WE WRITE IT INTO FILE book.txt 
        #WHERE OLD DATA OF THE FILE IS REMOVE AND UPDATED DATA IS ADDED
        book_file = open("book.txt", "w")
        for book in book_list:
            for i in range(len(book)):
                book_file.write(book[i])
                if i < len(book) - 1:
                    book_file.write(",")  # Add commas between elements
            book_file.write("\n")  # Move to the next line
        book_file.close()
        #AT THE END WE CHECK IF UPDATE HAS BEEN CHANGED TO TRUE:
        #IF IT REMAINED FALSE WE JUST APPEND NEW BOOK DETAILS ENTERED AS THE ISBN HAS NOT BEEN FOUND IN THE book.txt
        if update==False:
            book_file=open("book.txt","a")
            new_book=f"{self.title},{self.author},{self.ISBN},{self.category},{self.publisher},{self.publication_year},{self.copies},{self.location},{self.status}"
            book_file.write(new_book+"\n")
            book_file.close()
    #Function to Issue/Borrow book by User
    #We pass the username as parameter to be able to retrive matching record         
    def issue_book(username):
        #display books available at library
        check=Book.display_book()
        if check==True:
            return
        #Request user to enter ISBN to be issued
        ISBN=int(input("Enter book ISBN to issue : "))
        
        #open book.txt file to reduce the number of copies by 1
        book_file=open("book.txt","r")
        book_list=[]
        # loop in the file to remove \n and , and populate it in a 2D List
        for i in book_file.readlines():
            book_list.append(i.strip().split(","))
        #the process to remove 1 copies
        for i in range(1,len(book_list)):
            #we refer to a dictionary for easier search named book_map
            if int(book_list[i][book_map["ISBN"]])==ISBN:
                book_list[i][book_map["copies"]]=str(int(book_list[i][book_map["copies"]])-1)
                break
        book_file.close()
        #We Re-Write the content from 2D list to book.txt Filw With updated copies
        book_file = open("book.txt", "w")
        for book in book_list:
            for i in range(len(book)):
                book_file.write(book[i])
                if i < len(book) - 1:
                    book_file.write(",")  # Add commas between elements
            book_file.write("\n")  # Move to the next line
        book_file.close()
        
        #Open user.txt file to extract user information and append it in a 2D List by removing \n and ,
        user_file=open("user.txt","r")
        user_list=[]
        for i in user_file.readlines():
            user_list.append(i.strip().split(","))
        
        #loop in 2D List to fetch the email and username
        for i in user_list:
            if (i[8])==username:
                username=i[8]
                email=i[4]
        user_file.close() 
        #We check if transaction file exist or not 
        if os.path.exists("transactions.txt"):
            #if yes, we open it
            transactions_file=open("transactions.txt","r")
            #we read from last line
            transactions=transactions_file.readlines()[-1]
            #from that last line we extract the id and store it into variable id and immediately increment by 1 to record next line
            id=int(transactions.strip().split(",")[0])
            id+=1
        else:
            #if file not found,we create the file set the attribute and set id to 1 for first transaction
            book_file=open("transactions.txt","w")
            book_file.write("ID,USERNAME,ISBN,EMAIL,RETURN_DATE,STATUS\n")
            book_file.close()
            id=1
        
        #We request a return date
        return_date=verify_date_format()

        #open transaction.txt to write the book to issue
        transactions=open("transactions.txt","a")
        transactions.write(f"{id},{username},{ISBN},{email},{return_date},Borrowed\n")
        transactions.close()
    #Static function to display all books available if recorded
    @staticmethod
    def display_book():
        #check if file exist if not we print an output and exit
        if not os.path.exists("book.txt"):
            print("No books found in the library.")
            return True
        #else we open the file to read 
        book_file=open("book.txt","r")
        book_detail=book_file.readlines()
        #start to read from 2 line to the end
        #if nothing written print an output and exit
        if not book_detail[1:]:
            print("No books found in the library.")
            return True
        else:
            #print the books available in a format
            #clear the terminal
            clear_terminal()
            print(f"{"-"*80}BOOKS AVAILABLE IN LIBRARY{"-"*61}")
            print()
            for book in book_detail:
                book_attribute=book.strip().split(",")
                if book_attribute[0]=="TITLE":
                    print()
                    print(f"{book_attribute[0]:<25} {book_attribute[1]:<20} {book_attribute[2]:<20} {book_attribute[3]:<20} {book_attribute[4]:<25} {book_attribute[5]:<20} {book_attribute[6]:<10} {book_attribute[7]:<10} {book_attribute[8]:<10}")
                    print("-"*168)
                else:
                    print(f"{book_attribute[0]:<25} {book_attribute[1]:<20} {book_attribute[2]:<20} {book_attribute[3]:<20} {book_attribute[4]:<25} {book_attribute[5]:<20} {book_attribute[6]:<10} {book_attribute[7]:<10} {book_attribute[8]:<10}")
    #static method function to display all staff available
    @staticmethod
    def display_staff():
        #check if file exist if not we print an output and exit
        if not os.path.exists("staff.txt"):
           print("No staff found in the library.")
           return True
        #else we open the file to read 
        staff_file=open("staff.txt","r")
        staff_detail=staff_file.readlines()
        #start to read from 2 line to the end
        #if nothing written print an output and exit
        if not staff_detail[1:]:
            print("No staff found in the library.")
            return True
        else:
            #print the books available in a format
            #clear the terminal
            clear_terminal()
            print(f"{"-"*80}STAFF REGISTERED AT LIBRARY{"-"*56}")
            print()
            for staff in staff_detail:
                staff_attribute=staff.strip().split(",")
                if staff_attribute[0]=="ID":
                    print()
                    print(f"{staff_attribute[0]:<25} {staff_attribute[1]:<20} {staff_attribute[2]:<20} {staff_attribute[3]:<20} {staff_attribute[4]:<25} {staff_attribute[5]:<15} {staff_attribute[6]:<20} {staff_attribute[7]:<10}")
                    print("-"*163)
                else:
                    print(f"{staff_attribute[0]:<25} {staff_attribute[1]:<20} {staff_attribute[2]:<20} {staff_attribute[3]:<20} {staff_attribute[4]:<25} {staff_attribute[5]:<15} {staff_attribute[6]:<20} {staff_attribute[7]:<10}")
    #Static function to display all user registered    
    @staticmethod
    def display_user():
        #check if file exist if not we print an output and exit
        if not os.path.exists("user.txt"):
            print("No user found in the library.")
            return True
        #else we open the file to read
        user=open("user.txt","r")
        user_detail=user.readlines()
        #start to read from 2 line to the end
        #if nothing written print an output and exit
        if not user_detail[1:]:
            print("No user found in the library.")
            return True
        else:
            #print the books available in a format
            #clear the terminal
            clear_terminal()
            print()
            print(f"{"-"*80}USER REGISTERED AT LIBRARY{"-"*70}")
            for user in user_detail:
                user_attribute=user.strip().split(",")
                if user_attribute[0]=="ID":
                    print()
                    print(f"{user_attribute[0]:<5} {user_attribute[1]:<20} {user_attribute[2]:<20} {user_attribute[3]:<5} {user_attribute[4]:<30} {user_attribute[5]:<15} {user_attribute[6]:<20} {user_attribute[7]:<10}")
                    print("-"*170)
                else:
                    print(f"{user_attribute[0]:<5} {user_attribute[1]:<20} {user_attribute[2]:<20} {user_attribute[3]:<5} {user_attribute[4]:<30} {user_attribute[5]:<15} {user_attribute[6]:<20} {user_attribute[7]:<10}")
    #function to search book and its location/availability
    @staticmethod
    def search_book():
        clear_terminal()
        book=open("book.txt","r")
        book_details=book.readlines()
        book.close()
        if not book_details[1:]:
            print("No books found in the library.")
            return True
        else:
            count=0
            #Request Suggested Tilte to search
            search_name=str(input("Enter title to search :"))
            print()
            print(f"{"-"*15}BOOKS AVAILABLE WITH Suggested Title{"-"*15}")
            print(f"{"-"*66}")
            print()
            #loop into file to seach for the similar title
            for book in book_details[1:]:
                book_attribute=book.strip().split(",")
                #if title found we print the title and its location
                if search_name.lower() in book_attribute[0].lower():
                    # print(f"{book_attribute[0]:<25} {book_attribute[1]:<20} {book_attribute[2]:<20} {book_attribute[3]:<20} {book_attribute[4]:<25} {book_attribute[5]:<20} {book_attribute[6]:<10} {book_attribute[7]:<10} {book_attribute[8]:<10}")
                    print(f"{book_attribute[0]} Found @ Location {book_attribute[7]}")
                    count=1
            if count==0:
                    print("Not found")



                






        




        



    
