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
             print("id:",self.emp_id)
             print("salary:",self.salary)
             

class Manager(Employee):
        def __init__(self, name, age, man_id, salary, department):
            super().__init__(name,age,man_id,salary)
            self.department = department

        def display(self):
             super().display()
             print("department:",self.department)

person_details=[]
employee_details=[]
manager_details=[]

while True:
    print("\nChoose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")
    choice = int(input("\nEnter your choice: "))
        
    match choice:
        case 1:
            name = input("Enter Name: ")
            age = input("Enter Age: ")
                                        
            person = Person(name, age)

                                        
            print(f"\nPerson created with name: {name} and age: {age}.")

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
            man_id = input("enter id:")
            salary = input("enter employee salary:") 
            department = input("enter department")

            Man = Manager(name, age ,man_id ,salary ,department)  

            print(f"manager created with name :{name} , age :{age} , id :{man_id} ,salary :{salary} , department :{department}")    
            manager_details.append(Man)

        case 4:
            print("choose details to show:")
            print("1.person")
            print("2.employee")
            print("3.manager")
            show=int(input("enter your choice:"))
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
              print("---------exiting the system. all resourse have been freed.---------")
              break