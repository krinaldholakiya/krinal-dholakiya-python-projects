<div align="center">

# \-- ! OOP Person, Employee \& Manager System ! --

### *Interactive Console-Based Object-Oriented Programming in Python*

[!\[Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[!\[OOP](https://img.shields.io/badge/OOP-Inheritance%20%26%20Classes-FF6F00?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[!\[Console](https://img.shields.io/badge/Console-Interactive%20CLI-4CAF50?style=for-the-badge\&logo=windowsterminal\&logoColor=white)](https://www.python.org/)
[!\[Encapsulation](https://img.shields.io/badge/Concepts-Encapsulation%20%26%20Polymorphism-9C27B0?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)

<br/>

> \*"Object-Oriented Programming is not just a paradigm — it's how the real world thinks in code."\*

</div>

\---

## 📋 Table of Contents

* [📌 Overview](#-overview)
* [🎯 Problem Statement](#-problem-statement)
* [✨ Key Features](#-key-features)
* [🏗️ Project Structure](#️-project-structure)
* [🔄 Project Workflow](#-project-workflow)
* [👤 Class Design](#-class-design)
* [🖥️ Program Output](#️-program-output)
* [🛠️ Tech Stack](#️-tech-stack)
* [📈 Results \& Insights](#-results--insights)
* [🏆 Advantages](#-advantages)
* [📄 License](#-license)
* [👤 Author](#-author)
* [🙏 Acknowledgements](#-acknowledgements)

\---

## 📌 Overview

The **OOP Person, Employee \& Manager System** is a beginner-friendly, interactive Python console application that demonstrates core **Object-Oriented Programming (OOP)** concepts such as **class creation**, **inheritance**, **encapsulation**, and **method overriding**. The program presents a menu-driven interface that runs continuously until the user chooses to exit.

This project is designed to:

* Strengthen understanding of Python **classes and objects**
* Demonstrate **single and multilevel inheritance** between `Person`, `Employee`, and `Manager`
* Practice **constructor design** using `\_\_init\_\_` and `super()`
* Apply **user input handling** and **menu-driven program design**
* Produce clean, readable **console output** for real-world-style data

\---

## 🎯 Problem Statement

> \*\*Objective:\*\* Build a console-based interactive tool to create and display Person, Employee, and Manager objects using OOP principles.

You are building a simple employee management utility for students learning Python OOP. The program must accept user choices from a menu and execute the corresponding task — either creating an object of the selected class type or displaying its stored details.

|📂 Class|📄 Type|🔍 Description|
|-|-|-|
|`Person`|Base Class|Stores name and age|
|`Employee`|Derived from Person|Adds employee ID and salary|
|`Manager`|Derived from Employee|Adds department information|
|Menu System|Console I/O|Create objects and show their details|

The goal is to demonstrate **OOP hierarchy and real-world modeling** through a clean, menu-driven interactive program.

\---

## ✨ Key Features

|Feature|Description|
|-|-|
|🔁 **Infinite Menu Loop**|Program runs continuously until user selects Exit|
|👤 **3 Class Types**|Person, Employee, and Manager using class inheritance|
|🏗️ **OOP Hierarchy**|Manager → Employee → Person (multilevel inheritance)|
|📋 **Show Details**|Displays full object data via a sub-menu|
|🖥️ **CLI Interface**|Simple, clean text-based menu for user interaction|
|✅ **Input-Driven Flow**|Fully driven by user input with branching via `if-elif-else`|
|⚠️ **Exit Handling**|Graceful exit with "all resources have been freed" message|
|🧬 **Constructor Chaining**|Uses `super()` to pass attributes up the inheritance chain|

\---

## 🏗️ Project Structure

```
📦 oop-person-employee-manager/
│
├── 📄 project.py          ← Main Python script (entry point)
│
└── 📄 README.md           ← Project documentation
```

\---

## 🔄 Project Workflow

```
Program Start
      │
      ▼
┌─────────────────────────────┐
│   Display Main Menu         │  ← Options: Create / Show Details / Exit
└────────────┬────────────────┘
             │
     ┌───────┼────────────┐
     ▼       ▼            ▼
┌─────────┐ ┌──────────┐ ┌──────────┐
│Choice: 1│ │Choice: 2 │ │Choice: 3 │
│ Person  │ │ Employee │ │ Manager  │
└────┬────┘ └────┬─────┘ └────┬─────┘
     │           │             │
     ▼           ▼             ▼
┌─────────────────────────────────────┐
│  Input name, age (+id, salary,      │
│  department as needed)              │
└────────────────┬────────────────────┘
                 │
                 ▼
┌─────────────────────────────┐
│   Object Created \& Stored   │
└────────────┬────────────────┘
             │
             ▼
     Loop Back to Menu
             │
         ┌───┴──────────────┐
         ▼                  ▼
   Choice: 4             Choice: 5
  (Show Details)           Exit ✅
         │
   Sub-menu: person /
   employee / manager
```

\---

## 👤 Class Design

### 🧱 1. Person (Base Class)

> Stores the most basic human attributes: name and age.

**Logic:**

```python
class Person:
    def \_\_init\_\_(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
```

\---

### 💼 2. Employee (Inherits from Person)

> Extends Person with an employee ID and salary.

**Logic:**

```python
class Employee(Person):
    def \_\_init\_\_(self, name, age, emp\_id, salary):
        super().\_\_init\_\_(name, age)
        self.emp\_id = emp\_id
        self.salary = salary

    def show(self):
        super().show()
        print(f"id: {self.emp\_id}")
        print(f"salary: {self.salary}")
```

\---

### 🏢 3. Manager (Inherits from Employee)

> Extends Employee with a department field, forming a 3-level inheritance chain.

**Logic:**

```python
class Manager(Employee):
    def \_\_init\_\_(self, name, age, emp\_id, salary, department):
        super().\_\_init\_\_(name, age, emp\_id, salary)
        self.department = department

    def show(self):
        super().show()
        print(f"department: {self.department}")
```

\---

### 📐 4. Key OOP Concepts Used

|Concept|Detail|
|-|-|
|🧬 **Inheritance**|`Employee` extends `Person`; `Manager` extends `Employee`|
|🔧 **`\_\_init\_\_` Constructor**|Each class initializes its own attributes|
|🔗 **`super()`**|Child classes call parent constructors to chain initialization|
|🔁 **Method Overriding**|`show()` is overridden in each class, calling `super().show()`|
|🔒 **Encapsulation**|Each class manages its own data fields|

\---

## 🖥️ Program Output

### ▶️ Output 1 — Create a Person

> User selects option `1`, enters name and age to create a `Person` object.

!\[Create a Person](Screenshot\_2026-06-11\_120756.png)

\---

### ▶️ Output 2 — Create an Employee

> User selects option `2`, enters name, age, employee ID, and salary.

!\[Create an Employee](Screenshot\_2026-06-11\_120808.png)

\---

### ▶️ Output 3 — Create a Manager

> User selects option `3`, enters name, age, ID, salary, and department name.

!\[Create a Manager](Screenshot\_2026-06-11\_120817.png)

\---

### ▶️ Output 4 — Show Person Details

> User selects option `4 → 1` to display stored Person details.

!\[Show Person Details](Screenshot\_2026-06-11\_120832.png)

\---

### ▶️ Output 5 — Show Employee Details

> User selects option `4 → 2` to display stored Employee details.

!\[Show Employee Details](Screenshot\_2026-06-11\_120842.png)

\---

### ▶️ Output 6 — Show Manager Details

> User selects option `4 → 3` to display full Manager details including department.

!\[Show Manager Details](Screenshot\_2026-06-11\_120853.png)

\---

### ▶️ Output 7 — Exit the Program

> User selects option `5` to gracefully exit. System confirms all resources are freed.

!\[Exit Program](Screenshot\_2026-06-11\_120912.png)

\---

## 🛠️ Tech Stack

|Tool|Version|Purpose|
|-|-|-|
|🐍 **Python**|3.8+|Core programming language|
|🏗️ **Classes**|Built-in|Define Person, Employee, Manager objects|
|🧬 **Inheritance**|OOP Concept|Share and extend class attributes|
|🔗 **super()**|Built-in|Chain constructors and methods|
|🔁 **While Loop**|Built-in|Infinite menu loop control|
|🖨️ **print() / input()**|Built-in|Console I/O and user interaction|
|📐 **f-strings**|Python 3.6+|Formatted string output|

\---

## 📈 Results \& Insights

After running the program, the following outputs are produced:

* ✅ **3 Class Objects Created** — Person, Employee, and Manager with full attribute sets
* 🧬 **Inheritance Chain Works** — Manager inherits from Employee which inherits from Person
* 📋 **Show Details** — All stored object attributes are displayed cleanly via sub-menu
* 🔁 **Persistent Menu** — Program loops back after every task until manually exited
* 🚪 **Graceful Exit** — Option 5 displays a proper exit message confirming resource cleanup

\---

## 🏆 Advantages

|Advantage|Detail|
|-|-|
|🎓 **Beginner Friendly**|Core OOP concepts: classes, inheritance, and constructors in one project|
|🔄 **Reusability**|Classes can be reused and extended for larger systems|
|📚 **Educational**|Each class reinforces understanding of `\_\_init\_\_`, `super()`, and `show()`|
|🖥️ **No Dependencies**|Runs with pure Python — no external libraries needed|
|⚡ **Lightweight**|Single-file script, instantly runnable from any terminal|
|🧪 **Extensible**|Easy to add new classes like `Director`, `Intern`, etc.|
|📖 **Readable Code**|Clear class hierarchy makes logic easy to follow|
|🛡️ **Modular Design**|Each class is self-contained and independently testable|

\---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for full details.

```
MIT License — Free to use, modify, and distribute with attribution.
```

\---

## 👤 Author

<div align="center">

### KRINAL DHOLAKIYA

[!\[GitHub](https://img.shields.io/badge/GitHub-krinaldholakiya-181717?style=for-the-badge\&logo=github\&logoColor=white)](https://github.com/isamaliya16)
> \*"Every class is a blueprint — every object is a story waiting to be told."\*

**🎓 Role:** Junior Python Developer | OOP Enthusiast   
**📍 Location:** India  
**🛠️ Skills:** Python · OOP · CLI Applications · Inheritance · Class Design

</div>

\---

## 🙏 Acknowledgements

Special thanks to the following resources and communities that made this project possible:

* 📚 [Python Official Docs](https://docs.python.org/3/) — Official Python language reference
* 🧬 [Real Python — OOP](https://realpython.com/python3-object-oriented-programming/) — In-depth OOP tutorials
* 📐 [GeeksForGeeks — Classes](https://www.geeksforgeeks.org/python-classes-and-objects/) — Class and inheritance examples
* 🖥️ [W3Schools Python](https://www.w3schools.com/python/) — Beginner Python reference
* 🔗 [Python super() Guide](https://realpython.com/python-super/) — Constructor chaining with super()
* 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support
* 📖 [Kaggle Learn](https://www.kaggle.com/learn) — Python and programming courses

\---

<div align="center">

\---

*Made with ❤️  — Last updated: 11 June, 2026*

</div>

