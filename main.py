#The main program to be executed
from book import Book,clear_terminal,verify_date_format #import Book class,clear_terminal and verify_date_format function from book.py
from staff import Staff #import Staff class from staff.py
from admin import Admin #import Admin class from admin.py
from user import User #import User class from user.py
from main_login import * #import all function from main_login.py
from login_func import get_unique_username #import get_unique_username function from login_func.py


#Funtion to validate option using while loop and try except
def option_return():
        option=(input("Press 1 to return to Menu :"))
        while option!="1":
            print("Wrong Input! Press 1 Only")
            option=(input("Press 1 to return to Menu :"))
        return option
    



#main menu
def main():
    #initialise variable for later use
    result = False
    choice = ""
    username = ""
    #loop on result not true enter function main_logic()
    while result != True:
        #return three values from the function 
        result, choice, username = main_login()
        
    #match the choices of either customer C ,Admin A and Staff S
        match choice.upper():
            #if choice is customer
            case "C":
                option=0
                #loop through the option available
                while option!=6:
                    clear_terminal()
                    #display the menu for customer
                    print(f"{"-"*39}Customer Menu{"-"*39}")
                    print("1: View Book Available\n2: Search Book\n3: View_user_profile\n4: Borrow Book\n5: Return Book\n6: Exit")
                    print()
                    #validate option
                    option=int(input("Enter Your option :"))
                    while option<1 or option>6:
                            try:
                                print("Invalid option!, Option Range 1-5 Only")
                                option=int(input("Enter option again: "))
                            except:
                                print("Input should only be integer")
                                return
                    #match option and to do the specific function
                    match option:
                        case 1:
                            User.display_book()
                            print()
                            option=option_return()
                        case 2:
                            User.search_book()
                            print()
                            option=option_return()
                        case 3:
                            User.view_user_profile(username)
                            print()
                            option=option_return()
                        case 4:
                            User.borrow_book(username)
                            print()
                            option=option_return()
                        case 5:
                            Staff.return_book()
                            print()
                            option=option_return()
                        case 6:
                            print("-"*100)
                            print(F"Thank You Very Much To Use Our Platform MR/MRS {username} :)")
                            print("-"*100)
                            break
                    
        
                
            case "A":
                #Funtion to diplay admin menu when needed
                def admin_menu():
                    print(f"{"-"*39}Admin Menu{"-"*39}")
                    print()
                    print(f"{'1: Display Book':<20} {'5: Display Staff':<20} {' 9: Modify User':<20} {'13: Transaction History'}")
                    print(f"{'2: Add Book':<20} {'6: Add Staff':<20} {'10: View all Users':<20} {'14: Exit'}")
                    print(f"{'3: Delete Book':<20} {'7: Remove Staff':<20} {'11: Generate Report':<20}")
                    print(f"{'4: Search Book':<20} {'8: System Rules':<20} {'12: Delete User':<20}")


                    
                option = 0
                while option != 14:
                    clear_terminal()
                    admin_menu()
                    print()
                    #loop through the option available
                    try:
                        option = int(input("Enter option (1-14): "))
                        while option<1 or option>14:
                            try:
                                print("Invalid option!, Option Range 1-14 Only")
                                option=int(input("Enter option again: "))
                            except:
                                print("Input should only be integer")
                                return
                    except:
                            print("Input should only be integer")
                            return
                        
                    #match option and to do the specific function
                    match option:
                        case 1:
                            clear_terminal()
                            Admin.display_book()
                            print()
                            option=option_return()
                        case 2:
                            clear_terminal()
                            print("---------------Adding Book--------------------")
                            title = input("Enter title: ")
                            author = input("Enter author: ")
                            isbn = input("Enter ISBN: ")
                            category = input("Enter Category: ")
                            publisher = input("Enter publisher: ")
                            publication_year = input("Enter publication year: ")
                            copies = input("Enter copies: ")
                            location = input("Enter location: ")
                            status = input("Enter status: ") 
                            print()        
                            option=option_return()
                            book = Book(title, author, isbn, category, publisher, publication_year, copies, location, status)
                            book.add_book()
                        case 3:
                            clear_terminal()
                            Admin.remove_book()
                            print()
                            option=option_return()
                        case 4:
                            clear_terminal()
                            Admin.search_book()
                            print()
                            option=option_return()
                        case 5:
                            clear_terminal()
                            Admin.display_staff()
                            print()
                            option=option_return()
                        case 6:
                            print("---------------Adding Staff--------------------")
                            firstname=input("Enter First Name: ")
                            lastname=input("Enter LastName: ")
                            age=input("Enter age: ")
                            email=input("Enter Email: ")
                            phone=input("Enter phone: ")
                            address=input("Enter address: ")
                            dob=verify_date_format()
                            # username = input("Enter username: ")
                            username=get_unique_username("staff.txt")
                            password = input("Enter password: ")
                            new_staff = Admin(firstname, lastname, age, email, phone, address, dob,username,password)
                            new_staff.register_staff()
                            print()
                            option=option_return()
                        case 7:
                            clear_terminal()
                            Admin.delete_staff()
                            print()
                            option=option_return()
                        case 8:
                            clear_terminal()
                            Admin.system_rules()
                            print()
                            option=option_return()
                        case 9:
                            clear_terminal()
                            Admin.modify_user_details()
                            print()
                            option=option_return()
                        case 10:
                            clear_terminal()
                            Admin.view_user_details()
                            print()
                            option=option_return()
                        case 11: 
                            Admin.generate_report()
                            print()
                            option=option_return()
                        case 12:
                            Admin.delete_user()
                            print()
                            option=option_return()
                        case 13:
                            Admin.transaction_history()
                            print()
                            option=option_return()
                            #file not found
                        case 14:
                            print("-"*100)
                            print(f"Thank You For Your Service MR/MRS {username} ")
                            print("-"*100)
                            return
                
            case "S":
                #Funtion to diplay staff menu when needed
                def staff_menu():
                    print()
                    print(f"{"1: Add Book":<20} {" 6: Return Book":<20}")
                    print(f"{"2: Delete Book":<20} {" 7: Register Customer":<20}")
                    print(f"{"3: Display Book":<20} {" 8: Delete Customer":<20}")
                    print(f"{"4: Search Book":<20} {" 9: Modify Customer Details":<20}")
                    print(f"{"5: Issue Book":<20} {"10: Exit":<20}")
            
                option = 0
                #loop through the option available
                while option != 10:
                    clear_terminal()
                    staff_menu()            
                    print() 
                    option = int(input("Enter option: "))
                    while option<1 or option>10:
                            try:
                                print("Invalid option!, Option Range 1-10 Only")
                                option=int(input("Enter option again: "))
                            except:
                                print("Input should only be integer")
                                return
                    #match option and to do the specific function
                    match option:
                        #option 1 add book
                        case 1:
                            #required to enter book details assuming all details are correct!
                            title = input("Enter title: ")
                            author = input("Enter author: ")
                            isbn = input("Enter ISBN: ")
                            category = input("Enter Category: ")
                            publisher = input("Enter publisher: ")
                            publication_year = input("Enter publication year: ")
                            copies = input("Enter copies: ")
                            location = input("Enter location: ")
                            status = input("Enter status: ")
                            #create object book with the attribute               
                            book = Book(title, author, isbn, category, publisher, publication_year, copies, location, status)
                            book.add_book() # objrct to add book to the system
                            
                        case 2:
                            #option to remove book
                            clear_terminal()
                            #call object to remove book
                            Admin.remove_book()
                            print()
                            option=option_return()
                        case 3:
                            #option to diplay book
                            clear_terminal()
                            Staff.display_book()
                            print()
                            option=option_return()
                        case 4:
                            #option to seach book
                            clear_terminal()
                            Staff.search_book()
                            print()
                            option=option_return()
                        case 5:
                            #option to issue book bases on username provided by user
                            clear_terminal()
                            username=input("Enter username :")
                            Staff.issue_book(username)
                            print()
                            option=option_return()
                        case 6:
                            clear_terminal()
                            Staff.return_book()
                            print()
                            option=option_return()
                        case 7:
                            clear_terminal()
                            signup(1)
                            print()
                            option=option_return()
                        case 8:
                            clear_terminal()
                            Staff.delete_user()
                            print()
                            option=option_return()
                        case 9:
                            clear_terminal()    
                            Staff.modify_user_details()
                            print()
                            option=option_return()
                        case 10:
                            print("-"*100)
                            print(f"Thank You For Your Service MR/MRS {username} ")
                            print("-"*100)
                            break         
main()



