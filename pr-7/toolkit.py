import datetime
from datetime import timedelta
import time
import math
import random
import uuid

print("=================================")
print("Welcome To Multi-Utility Toolkit")
print("=================================")

while True:
    print("================================")
    print("Choose an Option:")
    print("1.Datetime and Time Operations")
    print("2.Mathematical Operations")
    print("3.Random Data Generation")
    print("4.Generate Unique Identifiers")
    print("5.File Operations")
    print("6.Explore Module Attributes")
    print("7.Exit")
    print("================================")

    try:
         choice=int(input("Enter Your Choice:"))
    except ValueError:
        print("Invalid input! Please enter a valid number between 1 and 7.")
        continue

    match choice:
      
                case 1:
                    while True:
                        print("================================================")
                        print("1.Datetime and Time Operations:")
                        print("2.Calculate Difference Between Two Dates/Times")
                        print("3.Formate Date Into Custom Format")
                        print("4.Stopwatch")
                        print("5.Countdown Timer")
                        print("6.Back To Main Menu")
                        print("===============================================")
                        choice2=int(input("Enter Your Choice:"))

                        match choice2:
                            case 1:
                                print((f"Current Date and Time: {datetime.datetime.now()}"))
                            case 2:
                                date1=input("Enter The First Date (DD-MM-YYYY):")
                                date2=input("Enter The Second Date (DD-MM-YYYY):")
                                d1=datetime.datetime.strptime(date1,"%d-%m-%Y")
                                d2=datetime.datetime.strptime(date2,"%d-%m-%Y")
                                dif=d2-d1
                                print("Difference : ",dif)
                            case 3:
                                try:
                                    print("Format Date Into Custom Format")
                                    print("===========================================")
                                    for_date=input("Enter Date (DD-MM-YYYY) : ")
                                    d = datetime.datetime.strptime(for_date, "%d-%m-%Y")
                                    print("Choose Format:")
                                    print("----------------------")
                                    print("A. YYYY/MM/DD")
                                    print("B. Month Day, Year")
                                    print("C. Day Of The Week")
                                    print("----------------------")

                                    for_choice=input("Enter Format Choice (A/B/C) : ")

                                    if for_choice=="A" or for_choice=="a":
                                            print(f"Formatted Date : {d.strftime('%Y-%m-%d')}")
                                    elif for_choice=="B" or for_choice=="b":
                                            print(f"Formatted Date : {d.strftime('%B %d, %Y')}")
                                    elif for_choice=="C" or for_choice=="c":
                                            print(f"Formatted Date : {d.strftime('%A')}")
                                    else :
                                        print("Invalid Choice!.....")
                                except ValueError:
                                    print("Error: Invalid date input.")
                            case 4:
                                print("=========== Stopwatch =========")
                                input("Press ENTER To Start...")
                                start_time=time.time()
                                print("Stopwatch is Running...")
                                input("Press ENTER Again To Stop...")
                                end_time=time.time()
                                elapsed=end_time-start_time
                                elapsed_time=timedelta(seconds=int(elapsed))
                                print(f"\nTime Elapsed: {elapsed_time}")
                                print("===============================")
                            case 5:
                                print("\n============== Countdown Timer ===============")
                                seconds=int(input("Enter The Time In Seconds: "))
                                print("\nCountdown Started:")
                                while seconds>0:
                                    print(f"Time Remaining: {seconds} seconds",end="\r")
                                    time.sleep(1)
                                    seconds -= 1
                                print("Time remaining: 0 seconds")
                                print("\nTime's up! \U0001f6a8")
                                print("=============================")
                            case 6:
                                break
            
                case 2:
                    while True:
                        print("---------- Mathematical Operations ----------")
                        print("1.Calculate Factorial")
                        print("2.Solve Compound Intrest")
                        print("3.Trigonometric Calculations")
                        print("4.Area Of Geometric Shapes")
                        print("5.Back To Main Menu")
                        math_choice=int(input("Enter Your Choice: "))

                        match math_choice:
                            case 1:
                                n=int(input("Enter Any Number: "))
                                if n<0:
                                    print("Factorials are mathematically undefined for negative numbers.")
                                else:
                                    fact=math.factorial(n)
                                    print(f"The Factorial of {n} is {fact}.")
                            case 2:
                                   print("===============================================")
                                   p = float(input("\nEnter principal amount: "))
                                   r = float(input("Enter rate of interest (in %): "))
                                   t = float(input("Enter time (in years): ")) 
                                   amount = p * ((1 + r / 100) **t)
                                   print(f"Compound Interest: {amount:.2f}")
                                   print("===============================================")
                            case 3:
                                  angle = float(input("\nEnter angle in degrees: "))
                                  rad = math.radians(angle)
                                  print(f"sin({angle}) = {math.sin(rad):.4f}")
                                  print(f"cos({angle}) = {math.cos(rad):.4f}")
                                  if angle % 180 == 90:
                                    print(f"tan({angle}) = Undefined")
                                  else:
                                    print(f"tan({angle}) = {math.tan(rad):.4f}")
                                  print("===============================================")
                            case 4:
                                print("\n--- Area of Geometric Shapes ---")
                                print("A. Circle")
                                print("B. Rectangle")
                                print("C. Square")
                                shape = input("Choose Shape (A/B/C): ")
                                if shape=="A" or shape=="a":
                                    r = float(input("Enter radius: "))
                                    area=math.pi*r*r
                                    print(f"Area Of Circle: {area:.2f}")
                                elif shape=="B" or shape=="b":
                                    l = float(input("Enter length: "))
                                    w = float(input("Enter width: "))
                                    area = l * w
                                    print(f"Area of Rectangle: {area:.2f}")
                                elif shape == "C" or shape == "c":
                                    s = float(input("Enter side length: "))
                                    area = s * s
                                    print(f"Area of Square: {area:.2f}")   
                                else:
                                    print("Invalid Choice!")
                            case 5:
                                  break
                case 3:
                    while True:
                        print("================================================")
                        print("Random Data Generation:")
                        print("1. Generate Random Number")
                        print("2. Generate Random List")
                        print("3. Create Random Password")
                        print("4. Generate Random OTP")
                        print("5. Back to Main Menu")
                        print("===============================================")
                        ran_choice= int(input("Enter your choice: "))

                        match ran_choice:
                             case 1:
                                  start=int(input("Enter Minimum Number: "))
                                  end=int(input("Enter Maximum Number: "))
                                  random_num=random.randint(start,end)
                                  print(f"Random Number: {random_num}")
                                  print("===============================================")
                             case 2:
                                  length = int(input("\nEnter the total number of items in the list: "))
                                  start = int(input("Enter minimum value for items: "))
                                  end = int(input("Enter maximum value for items: "))
                                  random_list = []
                                  for i in range(length):
                                    num = random.randint(start, end)
                                    random_list.append(num)
                                  print(f"Generated Random List: {random_list}")
                                  print("===============================================")
                             case 3:
                                length = int(input("\nEnter password length: "))
                                chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$!%&*?"
                                password = ""
                                for i in range(length):
                                    password = password + random.choice(chars)
                                print(f"Generated Password: {password}")
                                print("===============================================")
                             case 4:
                                length = int(input("\nEnter OTP length (e.g., 4 or 6): "))                                               
                                digits = "0123456789"         
                                otp = ""                       
                                for i in range(length):
                                     otp = otp + random.choice(digits)
                                print(f"Generated Random OTP: {otp}")
                                print("===============================================")
                             case 5:
                                  break
                case 4:
                        print("\n=== Generate Unique Identifiers (UUID) ===")
                        unique_id = uuid.uuid4()          
                        print(f"Generated UUID: {unique_id}")
                        print("==========================================")            
                case 5:
                    while True:
                        print("================================================")
                        print("File Operations:")
                        print("1. Create a new file")
                        print("2. Write to a file")
                        print("3. Read from a file")
                        print("4. Append to a file")
                        print("5. Back to Main Menu")
                        print("===============================================")
                        choice2 = int(input("Enter your choice: "))

                        match choice2:
                            case 1:
                                filename = input("\nEnter file name: ")                                                  
                                try:
                                    with open(filename, "x") as file:
                                        pass  
                                    print("File created successfully!")
                                except FileExistsError:
                                    print("Error: File already exists!")
                                    
                                print("===============================================")
                            case 2:                                                     
                                filename = input("\nEnter file name: ")
                                data = input("Enter data to write: ")                                                              
                                with open(filename, "w") as file:
                                    file.write(data)                                    
                                print("Data written successfully!")
                                print("===============================================")
                            case 3:                                                   
                                filename = input("\nEnter file name: ") 
                                try:                                                             
                                    with open(filename, "r") as file:
                                         data = file.read()                                        
                                    print("File Data:")
                                    print(data)
                                except FileNotFoundError:
                                    print("Error: File not found!")
                                    
                                print("===============================================")
                            case 4:
                                  filename = input("\nEnter file name: ")
                                  data = input("Enter data to append: ")
                                  with open(filename, "a") as file:
                                        file.write("\n" + data) 
                                  print("Data appended successfully!")
                                  print("===============================================") 
                            case 5:
                                  break
                case 6:                          
                    print("\n====== Explore Module Attributes =======")
                    print("Choose a module to explore:")
                    print("1. math")
                    print("2. time")
                    print("3. random")
                    print("4. datetime")
                    print("5. uuid")
                    print("=========================================")
                    dir_choice = int(input("Enter your choice: "))
                    if dir_choice == 1:
                        print(f"\nAttributes of 'math' module:\n{dir(math)}")
                    elif dir_choice == 2:
                        print(f"\nAttributes of 'time' module:\n{dir(time)}")
                    elif dir_choice == 3:
                        print(f"\nAttributes of 'random' module:\n{dir(random)}")
                    elif dir_choice == 4:
                        print(f"\nAttributes of 'datetime' module:\n{dir(datetime)}")
                    elif dir_choice == 5:
                        print(f"\nAttributes of 'uuid' module:\n{dir(uuid)}")
                    else:
                        print("Invalid Choice!")
                    print("=========================================")
                case 7:
                    print("===============================================") 
                    print("Thank You For Using The Multi-Utility Toolkit!")
                    print("===============================================") 
                    break
