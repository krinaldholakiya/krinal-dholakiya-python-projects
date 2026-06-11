# 🎨 Pattern Generator \& Number Analyzer

!\[Project Screenshot](22f62219-3621-4a05-817d-6d74f0d057b2.png)

## ✨ Features

* 🌟 Generate beautiful star (`\\\*`) patterns
* 🔢 Analyze numbers in a given range
* ⚡ Detect **Odd** and **Even** numbers
* ➕ Calculate the sum of numbers in the selected range
* 🖥️ Simple menu-driven Python program

\---

## 📸 Program Preview

The screenshot below shows the working output of the program:

!\[Output Preview](22f62219-3621-4a05-817d-6d74f0d057b2.png)

\---

## 🧾 Python Code

```python
print("Welcome to the pattern generater and number analyzer!")

while True:
    print("\\\\nSelect an option:")
    print("Press 1 for generate a pattern")
    print("Press 2 for analyze a range of number")
    print("Press 3 for exit")

    choice = int(input("Enter your choice:"))

    match choice:
        case 1:
            row = int(input("\\\\nEnter the number of rows for the pattern:"))
            for i in range(1, row + 1):
                for j in range(1, i + 1):
                    print("\\\*", end="")
                print("")

        case 2:
            start = int(input("\\\\nEnter the start of the range:"))
            end = int(input("Enter the end of the range:"))

            sum = 0

            for i in range(start, end + 1):
                if i % 2 == 0:
                    print("Number", i, "is even")
                else:
                    print("Number", i, "is odd")

                sum = sum + i

            print("Sum of all number from", start, "to", end, "is:", sum)

        case 3:
            print("\\\\nExiting the programe.Goodbye!")
            break
```

\---

## 🚀 How to Run

1. Install Python on your system
2. Save the code in a file named `main.py`
3. Run the program using:

```bash
python main.py
```

\---

## 📂 Project Structure

```text
📁 Project Folder
 ┣ 📄 main.py
 ┣ 📄 README.md
 ┗ 🖼️ screenshot.png
```

\---

## 💡 Future Improvements

* Add colorful terminal output
* Add more pattern styles
* Improve input validation
* Add GUI version using Tkinter

\---

## 👨‍💻 Author

Made with ❤️ using Python

