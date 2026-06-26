from datetime import datetime,timedelta
import time

def current_datetime():
    print()
    print("Current Date and Time:",datetime.now())
    print()

def date_diff():
    print()
    date1=input("Enter The First Date (DD-MM-YYYY):")
    date2=input("Enter The Second Date (DD-MM-YYYY):")
    d1=datetime.strptime(date1,"%d-%m-%Y")
    d2=datetime.strptime(date2,"%d-%m-%Y")
    dif=d2-d1
    print("Difference : ",dif)
    print() 
       
def date_style():
    print()
    try:
        print("Format Date Into Custom Format")
        print("===========================================")
        for_date=input("Enter Date (DD-MM-YYYY) : ")
        d = datetime.strptime(for_date, "%d-%m-%Y")
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
    print()

def stopwatch():
       print()
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
       print() 

def countdown_timer():
       print()
       print("\n============== Countdown Timer ===============")
       seconds=int(input("Enter The Time In Seconds: "))
       print("\nCountdown Started:")
       while seconds>0:
            print(f"Time Remaining: {seconds} seconds",end="\r")
            time.sleep(1)
            seconds -= 1
       print("Time remaining: 0 seconds")
       print("\nTime's up! 🚨")
       print("=============================")
       print()