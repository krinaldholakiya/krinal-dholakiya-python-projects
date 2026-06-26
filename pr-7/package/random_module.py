import random

def random_num():
    print()
    start=int(input("Enter Minimum Number: "))
    end=int(input("Enter Maximum Number: "))
    random_num=random.randint(start,end)
    print(f"Random Number: {random_num}")
    print("===============================================")
    print() 

def random_list():
    length = int(input("\nEnter the total number of items in the list: "))
    start = int(input("Enter minimum value for items: "))
    end = int(input("Enter maximum value for items: "))
    random_list = []
    for i in range(length):
        num = random.randint(start, end)
        random_list.append(num)
    print(f"Generated Random List: {random_list}")
    print("===============================================")
    print() 

def random_password():
    length = int(input("\nEnter password length: "))
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$!%&*?"
    password = ""
    for i in range(length):
        password = password + random.choice(chars)
    print(f"Generated Password: {password}")
    print("===============================================")
    print()   

def random_OTP():
   print()
   length = int(input("\nEnter OTP length (e.g., 4 or 6): "))                                               
   digits = "0123456789"         
   otp = ""                       
   for i in range(length):
        otp = otp + random.choice(digits)
   print(f"Generated Random OTP: {otp}")
   print("===============================================")
   print()