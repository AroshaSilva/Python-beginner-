#Electricity Bill Calculator (Sri Lanka Tariff 2023)

#📌 Project Overview
This Python program calculates the total electricity bill for Sri Lankan consumers based on the CEB tariff structure effective from October 2023. It takes monthly unit consumption and previous dues as input, then applies the correct progressive block rates and fixed charges to determine the final payable amount.

#🎯 **Created for A/L project 2023/2024 (ICT).

Real-World Application: Demonstrates understanding of tariff structures, conditional logic, and user input handling in Python.

#🧮 Tariff Structure Implemented
The program uses the following block rates (as per the 2023 CEB tariff):

Consumption Block (Units)	Unit Price (LKR)	Fixed Charge (LKR)
0 - 30	10.00	150.00
31 - 60	25.00	300.00
0 - 60 (Special)	32.00	300.00
61 - 90	38.00	400.00
91 - 120	50.00	1000.00
121 - 180	50.00	1500.00
181+	75.00	2000.00
Note: The program uses the "Special" block for exactly 60 units (32.00 LKR/unit).

#⚙️ How It Works
Input Phase:
Previous month's meter reading
Current month's meter reading
Any outstanding dues (CR)

Processing:
Calculates consumed units (Current - Previous)
Validates input (no negative units allowed)
Applies appropriate block rate based on consumption
Adds fixed charges based on the consumption tier

Output:
Units consumed
Applicable unit price
Previous dues
Fixed charges
Total payment (including all components)

#🖥️ Sample Output
text
Welcome to Electricity bill calculator.Please provide the data correctly.
This program will provide the Total payment with fixed charges included.
Enter the previous Units    : 450
Enter the current month Units: 520
Enter previous dues (if any):    LKR 0
--------------
Units consumed: 70 (Units)
--------------
Unit price: LKR 38.0
-----------------------------------------------------------
Previous dues: LKR 0.0
--------------
Fixed charges: LKR 400.0
--------------
Total payment: LKR 1680.00
-----------------------------------------------------------

#🔧 Requirements
Language: Python 3.x

Libraries Used: itertools, tkinter (imported but not actively used in this version)

#💻 How to Run
Save the code as ElectricityCalculator.py
Open terminal/command prompt
Run:
bash
python ElectricityCalculator.py
Follow the prompts to enter meter readings and dues.

#📊 Key Concepts Applied
Conditional Logic: if-elif-else statements for tier-based calculations
User Input: input() for data collection with float() conversion
Mathematical Operations: Basic arithmetic for bill computation
String Formatting: f-strings and .center() for clean output formatting
Error Handling: Basic validation for negative units

👨‍💻 Author
Arosha Silva/Gamerlaza
2024 A/L Python Project#1

#📚 References
Public Utilities Commission of Sri Lanka (PUCSL) - Official tariff announcement

🏷️ Tags
#python #electricity-bill #ceb-tariff #sri-lanka #tariff-calculator #education #2024A/L
