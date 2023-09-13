import json
import random 
class admin_file:
    def __init__(self):
        self.foods={}
    def add_item(self):
        key=random.randint(1,200)
        name=input("Enter food  name :")
        quantity=int(input("Enter quantity of food per plate :"))
        price=int(input("Enter food price per plate :"))
        discount=int(input("Enter discount of food per plate:"))
        stock=int(input("Enter food stock :"))
        food_data={"food name":name,
              "food quantity per plate":quantity,
              "food price per plate":price,
              "food discount per plate":discount,
              "food stock":stock
        }
        self.foods[key]=food_data
        with open("add_food.json","w")as f:
            json.dump(self.foods,f,indent=4)
        print(self.foods)
        return"**********************************************************************************************************************"
    def edit_food_item(self):
        for k,v in self.foods.items():
            print(f"ID : {k} data : {v}")
        food_code = int(input("enter food id which you want to edit :"))
        food_edit = input("enter which field you want to edit : ")
        food_updated_value = input("enter updated value : ")
        self.foods[food_code][food_edit]=food_updated_value
        with open("add_food.json","w") as f:
            json.dump(self.foods,f,indent=4)
        print(self.foods)
        return"**********************************************************************************************************************"
    def view_food_item(self):
        for k,v in self.foods.items():
            print(f"Id : {k}  data : {v}")
        return"**********************************************************************************************************************"
       
    
    def remove_item(self):
        for k,v in self.foods.items():
            print(f"ID : {k} data : {v}")
        food_del = int(input("enter food id which you want to delet : "))
        x = self.foods.pop(food_del)
        for k,v in self.foods.items():
            return(f"ID : {k} data : {v}")
        with open("add_food.json","w") as f:
            json.dump(self.foods,f,indent=4)
            return self.foods
        
        
