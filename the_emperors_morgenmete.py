import time 
# for time related tasks like delays

import threading
from abc import ABC, abstractmethod

import sys 
# system specific functions

from collections import defaultdict 
# create dictionaries with default values

# If using API :
# '''
from fastapi import FastAPI, HTTPException 
# Create API and raise HTTP errors

from fastapi.middleware.cors import CORSMiddleware 
# used to handle cross origin resource sharing in FastApi apps

from pydantic import BaseModel 
# used to auto validate input for FastApi

import uvicorn 
# server used to run FastApi apps

from fastapi import Form 
# used to recieve form data in POST requests

import json 
# used to work with json data
# '''

# Decorator for applying discount if the total is > 500 :
def apply_discount(func):
    def wrapper(*args, **kwargs): # can take any arguments
        total = func(*args, **kwargs) # calls total_price function and stores result in total
        if total > 500:
            discount = total * 0.10
            print(f"🎉 You get a 10% discount! (-{discount:.2f} Rs)")
            return total - discount
        return total
    return wrapper # returns the wrapper function to replace the original

# Abstract Class : 
class MenuItem(ABC):

    item_count = 0 
    # class variable 
    # to track total items

    # Nested Class :
    class Additive:
        def __init__(self, name, price):
            self.name = name
            self.price = price
    # Shows a belongs-to relationship 

    # constructor of MenuItem
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price
        self.additives = [] # list to store toppings
        MenuItem.item_count += 1

    def add_additive(self, additive): # to add an additive
        self.additives.append(additive) 

    def total_price(self):
        return self.base_price + sum(a.price for a in self.additives) 
        # The latter is a generator function 

    def additive_list(self):
        return ', '.join(a.name for a in self.additives) if self.additives else "None"
        # Returns all additives seperated by commas if present else returns None

    @abstractmethod # abstract method : child class must override it 
    def cook(self):
        pass

    # magic method (u cant create new magic methods - always override existing) 
    # This one is invoked when print() is used 
    def __str__(self):  
        return f"{self.name} ({self.additive_list()}) : {self.total_price()} Rs."

# Egg :
# Inheritance :
class Egg(MenuItem):
    def __init__(self):
        super().__init__("Egg 🍳", 50)

    # Concrete Method :
    def cook(self):
        for i in range(3, 0, -1): # go from 3 to 1 (reverse order)
            print(f"⏳ Cooking Egg 🍳... {i} sec left")
            time.sleep(1)
        if self.additives:
            print(f"✅ Egg 🍳 is cooked with {self.additive_list()}!")
        else:
            print(f"✅ {getattr(self, 'display_name', self.name)} is cooked!")
            # getattr(object,"attribute name",default value) :
            # used to safely access an attribute of an object

# Paratha :
class Paratha(MenuItem):
    def __init__(self):
        super().__init__("Paratha 🥘", 80)

    # Concrete Method :
    def cook(self):
        for i in range(10, 0, -1):
            print(f"⏳ Cooking Paratha 🥘... {i} sec left")
            time.sleep(1)
        if self.additives:
            print(f"✅ Paratha 🥘 is cooked with {self.additive_list()}!")
        else:
            print(f"✅ {getattr(self, 'display_name', self.name)} is cooked!")
            # getattr(object,"attribute name",default value) :
            # used to safely access an attribute of an object

# Tea :
class Tea(MenuItem):
    def __init__(self):
        super().__init__("Tea ☕", 60)

    # Concrete Method :
    def cook(self):
        for i in range(5, 0, -1):
            print(f"⏳ Brewing Tea ☕... {i} sec left")
            time.sleep(1)
        if self.additives:
            print(f"✅ Tea ☕ is brewed with {self.additive_list()}!")
        else:
            print(f"✅ {getattr(self, 'display_name', self.name)} is cooked!")
            # getattr(object,"attribute name",default value) :
            # used to safely access an attribute of an object


# Order Handling :
class Order:
    # class variable :
    all_orders = [] # To track order instances  

    def __init__(self):
        self.items = []
        Order.all_orders.append(self)
        # Can add multiple orders : however that functionality isnt implemented in this code yet (4th/07/2025)

    def add_item(self, item):
        self.items.append(item)
        # Adds item to the list (egg,paratha,tea)
        print(f"{item.name} added successfully!\n")

    def view_order(self):
        if not self.items:
            print("Your order is empty like your brain.")
            return
            # used to exit early if the order is empty

        print("\n--- Your Order ---")
        for idx, item in enumerate(self.items, 1):
            print(f"{idx}. {item}")
        # Enumeration : geting index + value from a list in a loop
        # for index,value in enumerate(iterable,start=0):
        print(f"Total: {self.total_price()} Rs\n")


    # Decorator applied :
    @apply_discount
    def total_price(self):
        return sum(item.total_price() for item in self.items)

    @staticmethod
    def choose_additives(available): # Can be called without creating an Order 
        selected = []
        print("\nAvailable Additives :")
        for i in range(len(available)):
            print(f"{i+1}. {available[i].name} : {available[i].price} Rs.")
        print("0. Done")

        while True:
            choice = input("Pick additive number (0 to stop): ").strip()
            if choice == "0":
                break
            elif choice.isdigit() and 1 <= int(choice) <= len(available):
                # check if number is in range : min <= value <= max 

                selected.append(available[int(choice)-1]) # remember indexes start from 0 .....
            else:
                print("Invalid input.")

        selected.sort(key=lambda a: a.price)  
        # Sort additives by price before returning : pass (a) , return a.price

        return selected


    @classmethod # Access class data
    def total_orders(cls):
        return len(cls.all_orders)

    # Generators : functions that give one value at a time and save memory
    def numbered_names(self):
        counts = defaultdict(int) 
        # defaultdict : auto sets defult values 

        for item in self.items:
            counts[item.name] += 1
            yield f"{item.name} #{counts[item.name]}"

    def checkout(self):
        if not self.items:
            print("Your cart and your head — both are empty.")
            return

        self.view_order()
        confirm = input("Proceed to checkout? (yes/no): ").strip().lower()

        if confirm != "yes":
            print("Checkout cancelled, you indecisive noob.")
            return

        print(f"\nTotal bill 🧾 : {self.total_price()} Rs")
        payment_method = input("Choose payment method (Cash/Card/Easypaisa): ").strip().capitalize()

        valid_methods = ["Cash", "Card", "Easypaisa"]
        while payment_method not in valid_methods:
            payment_method = input("Invalid method. Choose (Cash/Card/Easypaisa): ").strip().capitalize()

        print(f"Processing {payment_method} payment...")
        time.sleep(2)
        print("Payment successful! 😋\n")

        print("\nCooking has begun...\n")

        name_generator = self.numbered_names() 
        # Calls the numbered_names() generator

        threads = []

        for item in self.items:
            item.display_name = next(name_generator)
            # Calls the numbered_names() generator

            t = threading.Thread(target=item.cook)
            # pass cook function to the thread

            threads.append(t)
            # save thethread in threads list

            t.start()
            # start the thread : cooking begins.....

        # loop through each thread : 
        for t in threads:
            t.join()

        print("\n🥣 All items cooked!")
        print("Here is your order 👉🛒 Have a splendid day!\n")
        sys.exit()

# '''
app = FastAPI(title="The Emperor's Morgenmete API") # start the Api Application

# Enable CORS
app.add_middleware( 
    # Add a middleware for handling cors 
    # Middleware : a function that runs before and after every request to process or modify it
    # CORS : A rule that decides which websites can talk to your API

    CORSMiddleware, # da Middleware :)
    allow_origins=["*"],  # Allows any website to access the api
    allow_credentials=True, # Allows sending cookies or auth data in requests
    allow_methods=["*"], # Allow all HTTP methods
    allow_headers=["*"], # Allow all request headers
)

api_order = Order()  
# creates instance for API

class AdditiveModel(BaseModel):
    name: str # name of additive 
    price: float # price of additive
# Inherits from BaseModel class from Pydantic to validate and structure additive data
# BaseModel : helps define data structure 
# Pydantic : A library for validating and parsing data
# Additive Data : things added to items like sugar etc.

class ItemRequest(BaseModel):
    item_type: str  # "egg", "paratha", "tea"
    additives: list[AdditiveModel] = []


@app.post("/add-item")
def add_item(item_type: str = Form(...), additives: list[str] = Form(...)):
    item_map = {"egg": Egg, "paratha": Paratha, "tea": Tea}
    if item_type.lower() not in item_map:
        raise HTTPException(status_code=400, detail="Invalid item type.")
    item = item_map[item_type.lower()]()
    for a_json in additives:
        a = json.loads(a_json)
        item.add_additive(MenuItem.Additive(a["name"], a["price"]))
    api_order.add_item(item)
    return {"message": f"{item.name} added", "price": item.total_price()}


@app.get("/view-order")
def view_order():
    return {
        "items": [str(item) for item in api_order.items],
        "total": api_order.total_price()
    }

@app.post("/checkout")
def checkout(payment_method: str):
    if payment_method not in ["Cash", "Card", "Easypaisa"]:
        raise HTTPException(status_code=400, detail="Invalid method.")
    name_gen = api_order.numbered_names()
    threads = []
    for item in api_order.items:
        item.display_name = next(name_gen)
        t = threading.Thread(target=item.cook)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    return {"message": "Cooking complete!", "total": api_order.total_price()}
# '''


def main():
    egg_additives = [
        MenuItem.Additive("Black Pepper", 7),
        MenuItem.Additive("Red Pepper", 7),
        MenuItem.Additive("Puck Cream", 25)
    ]

    tea_additives = [
        MenuItem.Additive("Honey", 20),
        MenuItem.Additive("Ginger", 10),
        MenuItem.Additive("Sugar", 15),
        MenuItem.Additive("Lemon", 10)
    ]

    paratha_additives = [
        MenuItem.Additive("Butter", 20),
        MenuItem.Additive("Jam", 20)
    ]

    options = {
        "1": Egg,
        "2": Paratha,
        "3": Tea
    }

    additives_map = {
        "1": egg_additives,
        "2": paratha_additives,
        "3": tea_additives
    }

    order = Order()

    print("\nWelcome to The Emperor's Morgenmete 🐧!")

    while True:
        print("\n------  Menu  ------")
        print("1. Egg 🍳")
        print("2. Paratha 🥘")
        print("3. Tea ☕")
        print("4. View Order")
        print("5. Checkout")
        print("6. Exit")

        choice = input("Choose an option: ").strip()
                        # removes any spaces before or after the input 

        if choice in ["1", "2", "3"]:
            item = options[choice]()  
            # create an item based on user's choice , e.g. Egg()

            additives = Order.choose_additives(additives_map[choice])
            for a in additives:
                item.add_additive(a)
            order.add_item(item)

        elif choice == "4":
            order.view_order()

        elif choice == "5":
            order.checkout()

        elif choice == "6":
            print("Goodbye 😒")
            break

        else:
            print("Invalid input Peasant.")

if __name__ == "__main__":
    main()