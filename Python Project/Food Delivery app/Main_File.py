from Admin_File import *
from User_File import *
import sys
admin= admin_file()
user= user_file()
while True:
    print("Press-1 For Enter Admin Login")
    print("Press-2 For Enter User Login")
    print("Press-3 For Exit")
    print("*"*120)
    option = int(input("enter number : "))
    if option ==1:
        print("*********************************************WELCOME IN ADMIN PANEL*********************************************************")
        print("press-1 For add items : ") 
        print("press-2 For edit_food_item : ") 
        print("press-3 For view_food_item: ") 
        print("press-4 For remove_item : ")
        print("press-5 For Exit: ")  
        option = int(input("enter number : "))
        if option==1:
            print(admin.add_item())
            print("*"*120)
        elif option==2:
            print(admin.edit_food_item())
            print("*"*120)
            continue
        elif option == 3:
            print(admin.view_food_item())
            print("*"*120)
            continue
        elif option == 4:
            print(admin.remove_item())
            print("*"*120)
            continue
        elif option == 5:
            print("Thank You for Using Our Application.....")
            print("*"*120)
            continue
        else:
            print("Entr Valid code")
            print("*"*120)
    if option == 2:
        print("*********************************************WELCOME IN USER PANEL*********************************************************")
        print("press-1 For Register : ") 
        print("press-2 For user_option : ") 
        print("press-3 For order_histor : ")  
        print("press-4 For final_order : ") 
        option = int(input("enter number : "))
        print("*"*120)
        if option==1:
            print(user.Register())
            print("Module Added successfully")
            print("*"*120)
        elif option==2:
           print(user.user_option())
           print("*"*120)
        elif option == 3:
            print(user.order_history())
            print("*"*120)
        elif option == 4:
            print(user.final_order())
            print("*"*120)
        else:
            print("Entr Valid code")
            print("*"*120)
    elif option == 3:
        print("Thank You for Using Our Application.....")
        print("*"*120)
        sys.exit()

