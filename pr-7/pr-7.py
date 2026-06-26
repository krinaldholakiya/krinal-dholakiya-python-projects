import math
import uuid
from package.datetime_module import *
from package.math_operation_module import *
from package.random_module import *
from package.file_operations import *


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
                                 current_datetime()
                            case 2:
                                 date_diff()
                            case 3:
                                 date_style()
                            case 4:
                                 stopwatch()
                            case 5:
                                 countdown_timer()
                            case 6:
                                 print("Back To Main Menu......")
                                 print()
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
                                factorial_number()
                            case 2:
                                compound_interest()
                            case 3:
                                trigonometry()
                            case 4:
                                 print("\n--- Area of Geometric Shapes ---")
                                
                       
                                 while True:
                                        print("1. Rectangle")
                                        print("2. Square")
                                        print("3. Triangle")
                                        print("4. Circle")
                                        print("5. Exit")
                                        print()

                                        choice = int(input("Enter your choice: "))
                                        print()

                                        match choice:
                                            
                                            case 1:
                                                area_Rectangle()
                                            case 2:
                                                area_Square()
                                            case 3:
                                                area_triangle()
                                            case 4:
                                                area_circle()
                                            case 5 :
                                                print("Exiting......")
                                                break                                                 
                                            case _:
                                                print("Invalid Choice")
                                                print()
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
                                 random_num()
                             case 2:
                                random_list()
                             case 3:
                                random_password()
                             case 4:
                                 random_OTP()
                             case 5:
                                   print()
                                   print("Back To Main Menu.....")
                                   print()
                                   break
                             case _:
                                 print()
                                 print("Invalid Choice")
                                 print()
 
                case 4:
                        print("\n=== Generate Unique Identifiers (UUID) ===")
                        unique_id = uuid.uuid4()          
                        print(f"Generated UUID: {unique_id}")
                        print("==========================================")  
                        print()
         
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
                                file_create()
                            case 2:                                                                                    
                                 file_write()
                            case 3:                                                   
                               
                                  file_read()
                            case 4:                               
                                  file_append()
                            case 5:
                                  print()
                                  print("Back To Main Menu")
                                  print()
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
                   
                    print()
                case 7:
                    print("===============================================") 
                    print("Thank You For Using The Multi-Utility Toolkit!")
                    print("===============================================") 
                    break
                case _:
                       print("Invalid Choice")
                       print()        