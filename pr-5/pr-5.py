class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def display(self):
            print("Name:", self.name)
            print("Age:", self.age)

class Employee(Person):
        def __init__(self, name, age, emp_id, salary):
            super().__init__(name,age)
            self.emp_id = emp_id
            self.salary = salary

        def display(self):
             super().display()
             print("Id:",self.emp_id)
             print("Salary:",self.salary)
             

class Manager(Employee):
        def __init__(self, name, age, man_id, salary, department):
            super().__init__(name,age,man_id,salary)
            self.department = department

        def display(self):
             super().display()
             print("Department:",self.department)

person_details=[]
employee_details=[]
manager_details=[]

while True:
    print("\nChoose an Operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")
    choice = int(input("\nEnter Your choice: "))
        
    match choice:
        case 1:
            name = input("Enter Name: ")
            age = input("Enter Age: ")
                                        
            person = Person(name, age)

                                        
            print(f"\nPerson Created With Name: {name} and Age: {age}.")

            person_details.append(person)
        

        case 2:
            name = input("Enter Name: ")
            age = input("Enter Age: ")  
            emp_id = input("enter id:")
            salary = input("enter salary:")    

            emp = Employee(name, age,emp_id,salary)      

            print(f"employee created with name :{name} , age :{age} , id :{emp_id} ,salary :{salary} ") 
            employee_details.append(emp)

        case 3:
            name = input("Enter Name: ")
            age = input("Enter Age: ")  
            man_id = input("Enter Id:")
            salary = input("Enter Employee Salary:") 
            department = input("Enter Department")

            Man = Manager(name, age ,man_id ,salary ,department)  

            print(f"Manager Created With Name :{name} , Age :{age} , Id :{man_id} ,Salary :{salary} , Department :{department}")    
            manager_details.append(Man)

        case 4:
            print("Choose Details To Show:")
            print("1.Person")
            print("2.Employee")
            print("3.Manager")
            show=int(input("Enter Your Choice:"))
            match show:
                 case 1:
                     print("\n--- Person Details ---")
                     for i in person_details:
                        i.display()

                 case 2:
                      print("\n--- Employee Details ---")
                      for i in employee_details:
                        i.display()

                 case 3:
                    print("\n--- Manager Details ---")
                    for i in manager_details:
                        i.display()
     
        case 5:
              print("---------Exiting The System. All Resourse Have Been Freed.---------")
              break
