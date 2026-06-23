<div align="center">

# -- ! Multi-Utility Toolkit ! --
### *An All-in-One Interactive Console-Based Python Utility Suite*

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Match-Case](https://img.shields.io/badge/Control%20Flow-Match%20Case-FF6F00?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Console](https://img.shields.io/badge/Console-Interactive%20CLI-4CAF50?style=for-the-badge&logo=windowsterminal&logoColor=white)](https://www.python.org/)
[![Modules](https://img.shields.io/badge/Modules-datetime%20%7C%20time%20%7C%20math%20%7C%20random%20%7C%20uuid-9C27B0?style=for-the-badge&logo=python&logoColor=white)](https://docs.python.org/3/)

<br/>

> *"One toolkit, six powers — time, math, randomness, identity, files, and introspection, all in a single loop."*

<br/>

![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&duration=2800&pause=900&color=58A6FF&center=true&vCenter=true&width=750&lines=Welcome+To+Multi-Utility+Toolkit;Datetime+%E2%80%A2+Math+%E2%80%A2+Random+%E2%80%A2+UUID;File+Ops+%E2%80%A2+Module+Explorer;Choose+an+Option%3A+1+to+7...)

</div>

---

## 📋 Table of Contents

- [🎥 Live Demo](#-live-demo)
- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🕒 Part A — Datetime & Time Operations](#-part-a--datetime--time-operations)
- [➗ Part B — Mathematical Operations](#-part-b--mathematical-operations)
- [🎲 Part C — Random Data Generation](#-part-c--random-data-generation)
- [🆔 Part D — Unique Identifier Generation](#-part-d--unique-identifier-generation)
- [📁 Part E — File Operations](#-part-e--file-operations)
- [🧭 Part F — Module Attribute Explorer](#-part-f--module-attribute-explorer)
- [🎬 Animation & Visual Effects (Future Scope)](#-animation--visual-effects-future-scope)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 🎥 Live Demo

> An animated walkthrough of all 16 console screens, stitched into a looping GIF — the menu opens, every module runs in order, and the program exits.

<div align="center">

![Live Demo](screenshots/demo.gif)

*Full program walkthrough — Datetime → Math → Random → UUID → File Ops → Module Explorer → Exit*

</div>

> ℹ️ **Note:** `demo.gif` is a local file — it plays everywhere (GitHub, VS Code, offline) once the `screenshots/` folder sits next to this README. The typing banner near the top is a live SVG served by an external API, so it animates only when this README is viewed online (e.g., on GitHub) with an internet connection.

---

## 📌 Overview

The **Multi-Utility Toolkit** is a menu-driven, interactive Python console application that bundles **six independent utility modules** into one continuous program loop. It is built entirely on Python's standard library — no external dependencies — and is a practical showcase of **nested `while`/`match-case` control flow**, **exception handling**, **module exploration**, and **file I/O**.

This project is designed to:
- Demonstrate real-world use of Python's `match-case` statement (Python 3.10+) as a cleaner alternative to long `if-elif` chains
- Combine multiple standard-library modules (`datetime`, `time`, `math`, `random`, `uuid`) into one cohesive tool
- Practice robust input validation using `try/except`
- Provide a reusable CLI scaffold that can be extended with more utilities

---

## 🎯 Problem Statement

> **Objective:** Build a single console-based application that consolidates everyday small utilities — date/time handling, math operations, random data generation, unique ID creation, file handling, and module introspection — behind one unified, looping menu.

Instead of writing six separate throwaway scripts every time you need to check a date difference, calculate compound interest, generate an OTP, or peek inside a Python module, this toolkit puts all of it behind a single numbered menu that keeps running until you explicitly choose to exit.

| 📂 Module | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Datetime & Time Operations | Sub-menu | Current time, date difference, custom formatting, stopwatch, countdown |
| Mathematical Operations | Sub-menu | Factorial, compound interest, trigonometry, area of shapes |
| Random Data Generation | Sub-menu | Random number, random list, password generator, OTP generator |
| Unique Identifiers | Direct Action | Generates a UUID4 |
| File Operations | Sub-menu | Create, write, read, append files |
| Module Attribute Explorer | Sub-menu | Lists `dir()` attributes of standard modules |

The goal is to demonstrate **practical, everyday Python programming** through a clean, menu-driven interactive program.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🔁 **Infinite Menu Loop** | Program runs continuously until the user selects `7. Exit` |
| 🧩 **6 Independent Modules** | Datetime, Math, Random, UUID, File Ops, Module Explorer — each in its own nested loop |
| 🔀 **`match-case` Driven** | Modern structural pattern matching replaces long `if-elif` ladders |
| ⏱️ **Live Stopwatch & Countdown** | Real-time elapsed time tracking and a live countdown using `time.sleep()` |
| 🔢 **Math Toolbox** | Factorial, compound interest, trigonometric ratios, and shape areas |
| 🎲 **Randomization Suite** | Random numbers, lists, strong passwords, and numeric OTPs |
| 🆔 **UUID Generator** | Instantly generates RFC-4122 compliant unique identifiers |
| 📁 **Full File I/O Cycle** | Create → Write → Read → Append, each with proper exception handling |
| 🧭 **Live Module Introspection** | Inspect the real `dir()` output of `math`, `time`, `random`, `datetime`, `uuid` |
| ⚠️ **Input-Safe** | Wrapped `try/except ValueError` blocks prevent crashes on bad input |

---

## 🏗️ Project Structure

```
📦 multi-utility-toolkit/
│
├── 📄 multi_utility_toolkit.py   ← Main Python script (entry point)
├── 📄 README.md                  ← Project documentation (this file)
│
└── 📂 screenshots/                ← Console output screenshots + animated demo
    ├── 🎞️ demo.gif                ← Looping animated walkthrough (all 16 steps)
    ├── 01_welcome_and_datetime_menu.png
    ├── 02_custom_date_format.png
    ├── 03_countdown_timer.png
    ├── 04_compound_interest.png
    ├── 05_trigonometric_calculations.png
    ├── 06_area_of_square.png
    ├── 07_random_list_generation.png
    ├── 08_random_password_generation.png
    ├── 09_random_otp_generation.png
    ├── 10_generate_uuid.png
    ├── 11_file_create.png
    ├── 12_file_write.png
    ├── 13_file_read.png
    ├── 14_file_append.png
    ├── 15_explore_random_module.png
    └── 16_program_exit.png
```

---

## 🔄 Project Workflow

```
Program Start
      │
      ▼
┌───────────────────────────────┐
│      Display Main Menu        │  ← Options 1–7
└───────────────┬────────────────┘
                │
   ┌─────┬──────┼──────┬──────┬──────┐
   ▼     ▼      ▼      ▼      ▼      ▼
┌─────┐┌─────┐┌─────┐┌─────┐┌─────┐┌─────┐
│  1  ││  2  ││  3  ││  4  ││  5  ││  6  │
│Date ││Math ││Rand ││UUID ││File ││Expl │
│Time ││ Ops ││ Gen ││     ││ Ops ││ore  │
└──┬──┘└──┬──┘└──┬──┘└──┬──┘└──┬──┘└──┬──┘
   │      │      │      │      │      │
   ▼      ▼      ▼      ▼      ▼      ▼
 Nested Sub-Menu Loops Execute Chosen Task
   │      │      │      │      │      │
   └──────┴──────┴───┬──┴──────┴──────┘
                      ▼
            Loop Back to Main Menu
                      │
               (Choice: 7) Exit ✅
```

---

## 🕒 Part A — Datetime & Time Operations

> Five time-related tools live inside this sub-menu: current timestamp, date difference, custom formatting, a manual stopwatch, and a live countdown.

**Logic — Current Date/Time & Date Difference:**
```python
print(f"Current Date and Time: {datetime.datetime.now()}")

d1 = datetime.datetime.strptime(date1, "%d-%m-%Y")
d2 = datetime.datetime.strptime(date2, "%d-%m-%Y")
print("Difference : ", d2 - d1)
```

**Output — Main Menu & Current Date/Time:**

![Welcome and Datetime Menu](screenshots/01_welcome_and_datetime_menu.png)

**Logic — Custom Date Format (`strftime`):**
```python
if for_choice in ("A", "a"):
    print(f"Formatted Date : {d.strftime('%Y-%m-%d')}")
elif for_choice in ("B", "b"):
    print(f"Formatted Date : {d.strftime('%B %d, %Y')}")
elif for_choice in ("C", "c"):
    print(f"Formatted Date : {d.strftime('%A')}")
```

**Output — Custom Format (Month Day, Year):**

![Custom Date Format](screenshots/02_custom_date_format.png)

**Logic — Stopwatch & Countdown Timer:**
```python
# Stopwatch
start_time = time.time()
end_time = time.time()
elapsed_time = timedelta(seconds=int(end_time - start_time))

# Countdown
while seconds > 0:
    print(f"Time Remaining: {seconds} seconds", end="\r")
    time.sleep(1)
    seconds -= 1
```

**Output — Countdown Timer:**

![Countdown Timer](screenshots/03_countdown_timer.png)

---

## ➗ Part B — Mathematical Operations

> A small math toolbox: factorial, compound interest, trigonometric ratios, and geometric areas.

**Logic — Factorial:**
```python
fact = math.factorial(n)
print(f"The Factorial of {n} is {fact}.")
```
*(As seen partially carried over at the top of the screenshot below — `5! = 120` was computed just before switching to Compound Interest.)*

**Logic — Compound Interest:**
```python
amount = p * ((1 + r / 100) ** t)
print(f"Compound Interest: {amount:.2f}")
```

**Output — Compound Interest:**

![Compound Interest](screenshots/04_compound_interest.png)

**Logic — Trigonometric Calculations:**
```python
rad = math.radians(angle)
print(f"sin({angle}) = {math.sin(rad):.4f}")
print(f"cos({angle}) = {math.cos(rad):.4f}")
print(f"tan({angle}) = {math.tan(rad):.4f}")  # Undefined at 90°, 270°...
```

**Output — Trigonometric Calculations:**

![Trigonometric Calculations](screenshots/05_trigonometric_calculations.png)

**Logic — Area of Geometric Shapes:**
```python
area = math.pi * r * r        # Circle
area = l * w                  # Rectangle
area = s * s                  # Square
```

**Output — Area of Square:**

![Area of Square](screenshots/06_area_of_square.png)

---

## 🎲 Part C — Random Data Generation

> Four flavours of randomness: a single number, a list of numbers, a strong password, and a numeric OTP — all powered by Python's `random` module.

**Logic — Random List & Password:**
```python
for i in range(length):
    random_list.append(random.randint(start, end))

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$!%&*?"
password = "".join(random.choice(chars) for _ in range(length))
```

**Output — Random List Generation:**

![Random List Generation](screenshots/07_random_list_generation.png)

**Output — Random Password Generation:**

![Random Password Generation](screenshots/08_random_password_generation.png)

**Logic — Random OTP:**
```python
digits = "0123456789"
otp = "".join(random.choice(digits) for _ in range(length))
print(f"Generated Random OTP: {otp}")
```

**Output — Random OTP Generation:**

![Random OTP Generation](screenshots/09_random_otp_generation.png)

---

## 🆔 Part D — Unique Identifier Generation

> Generates a fresh, RFC-4122 compliant UUID on every call — no sub-menu needed, it's a single direct action.

**Logic:**
```python
unique_id = uuid.uuid4()
print(f"Generated UUID: {unique_id}")
```

**Output — UUID Generation:**

![Generate UUID](screenshots/10_generate_uuid.png)

---

## 📁 Part E — File Operations

> A complete file-handling cycle: create, write, read, and append — each wrapped in proper exception handling for missing or existing files.

**Logic:**
```python
with open(filename, "x") as file: pass        # Create (raises FileExistsError if it exists)
with open(filename, "w") as file: file.write(data)   # Write (overwrites)
with open(filename, "r") as file: data = file.read() # Read (raises FileNotFoundError)
with open(filename, "a") as file: file.write("\n" + data)  # Append
```

**Output — Create a New File:**

![File Create](screenshots/11_file_create.png)

**Output — Write to File:**

![File Write](screenshots/12_file_write.png)

**Output — Read from File:**

![File Read](screenshots/13_file_read.png)

**Output — Append to File:**

![File Append](screenshots/14_file_append.png)

---

## 🧭 Part F — Module Attribute Explorer

> A handy introspection tool — pick a standard-library module and instantly see every attribute and method it exposes via `dir()`.

**Logic:**
```python
if dir_choice == 3:
    print(f"\nAttributes of 'random' module:\n{dir(random)}")
```

**Output — Exploring the `random` Module:**

![Explore Random Module](screenshots/15_explore_random_module.png)

---

### 🏁 Program Exit

**Output — Exit Screen:**

![Program Exit](screenshots/16_program_exit.png)

---

## 🎬 Animation & Visual Effects (Future Scope)

> The [Live Demo](#-live-demo) GIF above already animates the *screenshots* — but the program's actual console output is still text-static. Here are lightweight, dependency-free ways the **runtime CLI itself** could be animated in a future version:

| Idea | Where It Fits | How It Could Work |
|------|----------------|--------------------|
| ⌛ **Spinner Animation** | UUID / Password / OTP generation | Cycle through `\|`, `/`, `-`, `\` characters with `\r` + `time.sleep(0.1)` to simulate "processing" before the result prints |
| 📊 **Animated Progress Bar** | Countdown Timer | Replace the plain `Time Remaining: X seconds` text with a filling `[█████-----]` bar that grows each second |
| ⌨️ **Typewriter Effect** | Welcome Banner | Print the `"Welcome To Multi-Utility Toolkit"` banner one character at a time using a tiny `time.sleep(0.02)` delay per character |
| 🌈 **ANSI Color Cycling** | Menu Headers | Use ANSI escape codes (`\033[31m`, `\033[32m`, etc.) to color-cycle the `====` separator lines for a "neon" CLI feel |
| ⏳ **Loading Dots** | File Operations | Print `Reading file` then animate `.`, `..`, `...` before showing file content, simulating an I/O delay |
| 🎉 **Exit Confetti** | Program Exit | A short animated sequence of random symbols (`✨ 🎊 ⭐`) printed line-by-line before the final "Thank You" message |

> 💡 These can all be built with pure standard-library tools (`time.sleep`, `\r`, ANSI codes) — or upgraded further using lightweight third-party libraries like `rich`, `colorama`, or `pyfiglet` for banner art and richer terminal animation.

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.10+ | Core programming language |
| 🔀 **`match` / `case`** | Python 3.10+ | Structural pattern matching for menu routing |
| 🔁 **`while` Loop** | Built-in | Persistent main menu and all sub-menus |
| 📅 **`datetime`** | Built-in | Date/time arithmetic and formatting |
| ⏱️ **`time`** | Built-in | Stopwatch, countdown, and `sleep()` delays |
| 🧮 **`math`** | Built-in | Factorial, trigonometry, π-based area formulas |
| 🎲 **`random`** | Built-in | Random numbers, lists, passwords, OTPs |
| 🆔 **`uuid`** | Built-in | UUID4 generation |
| 🖨️ **`print()` / `input()`** | Built-in | Console I/O |

---

## 📈 Results & Insights

After running the program, the following outputs are produced:

- ✅ **6 Fully Working Modules** — Datetime, Math, Random, UUID, File Ops, and Module Explorer
- ⏱️ **Real-Time Tools** — Live stopwatch and countdown timer with second-by-second updates
- 🔢 **Accurate Math Outputs** — Verified factorial, compound interest, trig, and area calculations
- 🎲 **Reliable Randomness** — Consistent password/OTP/list generation on every run
- 📁 **Safe File Handling** — `FileExistsError` and `FileNotFoundError` both caught gracefully
- 🔁 **Persistent Menu** — Program loops back after every task until choice `7` is entered
- ⚠️ **Error Feedback** — Invalid menu numbers caught via `try/except ValueError` instead of crashing

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Practical & Reusable** | Every module solves a genuine everyday problem (dates, math, passwords, files) |
| 🔄 **Modular Design** | Each menu option lives in its own nested loop — easy to extract into separate functions |
| 📚 **Modern Python** | Uses `match-case` instead of long `if-elif` chains for cleaner routing |
| 🖥️ **Zero Dependencies** | Runs with pure Python — only standard-library modules |
| ⚡ **Lightweight** | Single-file script, instantly runnable from any terminal |
| 🧪 **Extensible** | New sub-menus (e.g., unit converter, text utilities) can be added with one more `case` block |
| 🛡️ **Input Safety** | `try/except` blocks guard against invalid numeric input throughout |
| 🧭 **Self-Documenting** | The Module Explorer doubles as a live learning tool for Python's standard library |

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for full details.

```
MIT License — Free to use, modify, and distribute with attribution.
```

---

## 👤 Author

<div align="center">

### Krinal

[![GitHub](https://img.shields.io/badge/GitHub-yourhandle-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/)

> *"A toolkit isn't just code — it's every small problem you never want to solve twice."*

**🎓 Role:** Python Developer | Programming Enthusiast \
**📍 Location:** India \
**🛠️ Skills:** Python · Match-Case · CLI Applications · File Handling · Standard Library Mastery

*(Update the GitHub/LinkedIn badge links above with your own profile URLs.)*

</div>

---

## 🙏 Acknowledgements

Special thanks to the following resources that made this project possible:

- 📚 [Python Official Docs](https://docs.python.org/3/) — Official Python language reference
- 🔀 [Python `match` Statement Docs](https://docs.python.org/3/reference/compound_stmts.html#the-match-statement) — Structural pattern matching reference
- 📅 [Python `datetime` Docs](https://docs.python.org/3/library/datetime.html) — Date and time handling
- 🧮 [Python `math` Docs](https://docs.python.org/3/library/math.html) — Mathematical functions reference
- 🎲 [Python `random` Docs](https://docs.python.org/3/library/random.html) — Randomization utilities
- 🆔 [Python `uuid` Docs](https://docs.python.org/3/library/uuid.html) — UUID generation reference
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 22 June, 2026*

</div>
