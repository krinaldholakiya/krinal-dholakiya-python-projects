print("Welcome to the pattern generater and number analyzer!")
while True:
    print("\nSelect an option:")

    print("Press 1 for generate a pattern")
    print("Press 2 for analyze a range of number")
    print("Press 3 for exit")
    choice=int(input("Enter your choice:"))

    match choice:
        case 1:
            row=int(input("\nEnter the number of rows for the pattern:"))
            for i in range (1,row+1,+1):
                for j in range (1,i+1,+1):
                    print("*",end="")
                print("")
        case 2:
            start=int(input("\nEnter the start of the range:"))
            end=int(input("Enter the end of the range:"))
            sum=0
            for i in range (start,end+1,+1):
                    if i%2==0:
                        print("Number",i,"is even")
                    else :
                        print("Number",i," is odd")
                    
                    sum=sum+i
            print("Sum of all number from",start,"to",end,"is:",sum)
        case 3:
            print("\nExiting the programe.Goodbye!")
            break
