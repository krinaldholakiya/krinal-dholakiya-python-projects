\# Personal Data Collector



A simple command-line Python utility that collects user demographics, performs data type casting, displays system memory addresses, and estimates birth years.



\## Features



\- \*\*Interactive CLI:\*\* Prompts users for text, integer, and float inputs.

\- \*\*Type Checking:\*\* Explicitly displays the Python data type class for each input.

\- \*\*Low-Level Insights:\*\* Outputs the unique memory address (`id()`) of variables.

\- \*\*Calculated Fields:\*\* Predicts approximate birth year based on the current calendar year.



```bash

python data\_collector.py

```



\## Sample Input/Output Simulation



```text

Welcome to the Personal Data Collector.



Please enter your name: Alice

Please enter your age: 25

Please enter your height in meters: 1.65

Please enter your favorite number: 7



Thank you! Here is the information we collected:



Name: Alice <class 'str'>, Memory address: 14041123456789

Age: 25 <class 'int'>, Memory address: 14041198765432

Height: 1.65 <class 'float'>, Memory address: 14041155555555

Favorite Number: 7 <class 'int'>, Memory address: 14041198765111



Your birth year is approximately: 2001



Thank you for using Personal Data Collector, goodbye!

```





