def file_create():
    print()
    filename = input("\nEnter file name: ")                                                  
    try:
        with open(filename, "x") as file:
            pass  
        print("File created successfully!")
    except FileExistsError:
            print("Error: File already exists!")
                                    
    print("===============================================")
    print()

def file_write():
    print()
    filename = input("\nEnter file name: ")
    data = input("Enter data to write: ")                                                              
    with open(filename, "w") as file:
        file.write(data)                                    
    print("Data written successfully!")
    print("===============================================")
    print()

def file_read():
    print()
    filename = input("\nEnter file name: ") 
    try:                                                             
        with open(filename, "r") as file:
            data = file.read()                                        
        print("File Data:")
        print(data)
    except FileNotFoundError:
            print("Error: File not found!")
                                    
    print("===============================================")

def file_append():
    print()
    filename = input("\nEnter file name: ")
    data = input("Enter data to append: ")
    with open(filename, "a") as file:
        file.write("\n" + data) 
    print("Data appended successfully!")
    print("===============================================") 
    print()