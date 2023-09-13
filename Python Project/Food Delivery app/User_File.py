import json
class user_file:
    def __init__(self):
        self.user_details={}
    def Register(self):
        self.Full_name=input("Enter your Full name : ")
        self.Phone_number=int(input("Enter your Phone number : "))
        self.Address=input("eter your Address : ")
        self.Email_Id=input("Enter your Email ID : ")
        self.Password=input("Enter your Password : ")
        
        self.user_data={"user name":self.Full_name,"user Phone number":self.Phone_number,"user Address":self.Address,"user Email address":self.Email_Id,"user Password":self.Password}
        self.user_details[self.Email_Id]=self.user_data
        with open("user_details.json","w")as f:
            json.dump(self.user_details,f)
            print(self.user_details)
        return"**************************************************************************************************************************"
     
    def user_option(self):
        print("Press - 1 for user-Login")
        print("press - 2 for place_order")
        print("press - 3 for update_profile")
        
        user_option_input=int(input("Enter code for option : "))
        if user_option_input==1:
                    Email_Id=input("For Login Enter your email address  : ")
                    Password=input("For Login Enter your password  : ")
                    if Email_Id==self.Email_Id and Password==self.Password:
                        return "You Are Succefully Login"
                    else:
                        return"incorrect Email_Id or Password"
        elif user_option_input==2:
                order_list=[{"name":"Tandoori chiken","qunatity":"4 pices","price":240},
                   {"name":"Vegan Burger","qunatity":"1 pieces","price":320},
                   {"name":"Truffle Cake","qunatity":"500gm","price":900}]
                print("The menu is .......")
                print("Press-1 for - name:Tandoori chiken, qunatity:4 pices, price:240")
                print("Press-2 for - name:Vegan Burger, qunatity:1 pieces, price:320")
                print("Press-3 for - name:Truffle Cake , qunatity:500gm , price:900")
                user_input=int(input("Enter Code Of Item That You Want : "))
                if user_input==1:
                    print("name:Tandoori chiken, qunatity:4 pices, price:240")
                elif user_input==2:
                    print("name:Vegan Burger, qunatity:1 pieces, price:320")
                elif user_input==3:
                    print("name:Truffle Cake , qunatity:500gm , price:900")
                else:
                    print("Enter valid code")
                print(" Press 1 for order placed or fo order cancellation press any other key")
                order_list=int(input("Do you want place order : "))
                if order_list==1:
                    return"Order Placed successfully"
                else:
                    return"Order cancelled"
    
        elif user_option_input==3:
            for k,v in self.user_details.items():
                 print( f"Id : {k}  Data : {v}" )
                 Email_Id = input(" For profile update Enter your email id for  : ")
                 Password=input("For profile update Enter your Password  : ")
                 if Email_Id==self.Email_Id and Password==self.Password:
                      Personal = input("Enter which thing you want to edit : ")
                      updated_value = input("Enter Updated value : ")
                 else:
                      print("incorrect Email_Id or Password")
                      
                 self.user_details[Email_Id][Personal] = updated_value
                 with open("user_details.json","w") as f:
                      json.dump(self.user_details,f,indent=4)
                      print(self.user_details)
            return"**********************************************************************************************************************"
    
    def order_history(self):
        Email_Id = input("For Order Histort Enter your email id :")
        if Email_Id==self.Email_Id:
            print("Priveious Order Was : " , self.user_details)
        else:
             print("incorrect Email_Id or Password")
        return"********************************************************************************************************************************************************************"
            
    def final_order(self):
        Email_Id = input("For View Final Order Enter your email id :")
        if Email_Id==self.Email_Id:
            print("Final order is : " , self.user_details)
        else:
             print("incorrect Email_Id or Password")
        return"***********************************************************************************************************************************************"

