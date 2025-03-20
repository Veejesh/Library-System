from book import Book,os,clear_terminal
class User(Book):
    #Funtion to borrow a book ,this is the same funtion as issue book
    def borrow_book(username):
        Book.issue_book(username)    
    #Funtion to ViewUserProfile passing a parameter username from login to know which account to access
    def view_user_profile(username):
        #open file user to extract data
        file_user = open("user.txt", "r")
        #check if transaction file exist 
        if os.path.exists("transactions.txt"):
            file_transaction = open("transactions.txt", "r")
        else:
            print("No transaction Made")
            return
        #read from user.txt and transaction.txt
        user=file_user.readlines()
        transaction=file_transaction.readlines()
        file_user.close()
        file_transaction.close()
        #set found to 0 to check if any transaction match the username profile, set to 1
        found=0
        print()
        clear_terminal()
        #printing format for the user details
        for content in user:
            data=content.strip().split(",")
            if username == data[8]:
                print(f"{"="*50}")
                print(f"User Name : {username}")
                print(f"{"="*50}")
                print(f"Name :{data[1]} {data[2]}")
                print(f"Age  :{data[3]}")
                print(f"Email: {data[4]} Phone :{data[5]}")
                print(f"Address :{data[6]}")
                print(f"DOB :{data[7]}")
                print(f"{"="*50}")
                print()
        #printing transaction made  by user
        print("Transaction History By User")
        for i in transaction:
            t=i.strip().split(",")
            if t[0]=="ID":
                print("="*75)
                print(f"{t[0]:<3} {t[1]:<10} {t[2]:<10} {t[3]:<25} {t[4]:<15} {t[5]:<15}")
                print("-"*75)
            elif username in t[1]:
                found=1
                print(f"{t[0]:<3} {t[1]:<10} {t[2]:<10} {t[3]:25} {t[4]:<15} {t[5]:<15}")
        if found==0:
            print("No transaction has been made")
        