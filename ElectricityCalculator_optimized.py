#This code can calculate and provide the total payable ammount

text = "Welcome to Electricity bill calculator.Please provide the data correctly.This program will provide the Total payment with fixed charges included."
width = 20
centered_text = text.center(width)
print(centered_text)

#Gets units 
#1.PrevU = Total no.of units consumed upto last month.
#2. NewU = Total no.of units consumed upto this/current month.
PrevU=float(input("Enter the previous Month Units    : ")) 
NewU=float(input("Enter the current month Units: "))

#Gets no of CONSUMED units (this month) ConUn = Difference of units consumed.
ConUn = NewU-PrevU
CR=0
if ConUn < 0 :
    print("ERROR!!, NO. Of Units be positive value, Process cannot continue, Please Check Again")
    exit()  # Exit early if invalid input
else:
    CR=float(input("Enter previous dues (if any):    LKR "))

#Please check below for Unit prices , Fixed charges and it's ranges |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| B represents ' Block '
#\\\\\\\\\\\\\\\\\\\\\\\\\\\|||||||||||||||///////////////////////////////////////////////////////////////////////////////////////////////// 
#Units less than 60
#B 1 0-30 - 10.00 fixed 150
#B 2 31-60 - 25.00  fixed 300

#more than 60
#B1  0-60 - 32.00  FIXED 300  \\\\\\\\\\\\\\  The letter before B represents digits in a letter , F= First , S= Second etc...
FBlock=0
#B2  61-90 35.00  fixed 400
SBlock=60*32
#B3  91-120 - 50.00  fixed 1000
TBlock=(60*32)+(30*35)
#B4  121-180 50.00  fixed 1500
FOBlock=(60*32)+(30*35)+(30*50)
#B5  181 + 75.00  fixed 2000
lBlock=(60*32)+(30*35)+(30*50)+(30*50)

# ==================================  TARIFF STRUCTURE ====================================
# Define tariff blocks as (min_units, max_units, unit_price, fixed_charge)
tariff_blocks = [
    (0, 30, 10.00, 150.00),
    (31, 60, 25.00, 300.00),
    (60, 60, 32.00, 300.00),   # Special case for exactly 60 units
    (61, 90, 38.00, 400.00),
    (91, 120, 50.00, 1000.00),
    (121, 180, 50.00, 1500.00),
    (181, float('inf'), 75.00, 2000.00)
]
# ==================================  TARIFF STRUCTURE END ====================================

# Initializing variables__________________________________________________________________________
calc = 0.0
fixedcharges = 0.0
ConUnNew = 0
Totunitcon = 0

# Finds the applicable tariff block_____________________________________________________________
if ConUn == 0:
    # Special case: zero units
    Totunitcon = 0
    ConUnNew = 0
    calc = 0.00
    fixedcharges = 0.00  # No fixed charges for zero consumption
else:
    for min_units, max_units, unit_price, fixed_charge in tariff_blocks:
        if min_units <= ConUn <= max_units:
            calc = unit_price
            fixedcharges = fixed_charge
            
            if min_units == 0 and max_units == 30:
                # First block: 0-30 units
                Totunitcon = 0
                ConUnNew = ConUn
            elif min_units == 31 and max_units == 60:
                # Second block: 31-60 units
                Totunitcon = 30 * 10  # Cost of first 30 units
                ConUnNew = ConUn - 30
            elif min_units == 60 and max_units == 60:
                # Special case: exactly 60 units
                Totunitcon = 0
                ConUnNew = ConUn
            else:
                # Blocks 61-90, 91-120, 121-180, 181+
                # Calculate previous blocks' total
                for prev_min, prev_max, prev_price, prev_fixed in tariff_blocks:
                    if prev_max < min_units:
                        if prev_max == 60 and prev_min == 60:
                            # Skip the special 60-unit block in cumulative calculation
                            continue
                        units_in_block = prev_max - prev_min + 1
                        Totunitcon += units_in_block * prev_price
                    else:
                        break
                
                # Calculate units in current block
                if ConUn > min_units:
                    ConUnNew = ConUn - min_units + 1
                else:
                    ConUnNew = ConUn
            break

# Calculation starts /////////////////////////////////////////////////////////////////////////////////
TotalPayment = calc * ConUnNew

# Final calculation ////////////////////////////////////////////////
# Addition of DUE/CR if available
if CR >= 0:
    Totfinaltotal = TotalPayment + Totunitcon + fixedcharges + CR
else:
    Totfinaltotal = TotalPayment + Totunitcon + fixedcharges

# Output section (keeping original display logic)
print("--------------")
print("Units consumed:", ConUn, "(Units)")
print("--------------")  #Used to seperate neatly

if ConUn == 0:
    print("No units have been consumed, this price only includes 'Fixed charges'")
    print("--------------")
    # Set unit price display for zero case
    calc_display = 0.00
else:
    # Unit price display logic (simplified)
    if ConUn < 0:
        calc_display = 0
    elif ConUn <= 30:
        calc_display = 10.00
    elif 30 < ConUn <= 60:
        calc_display = 25.00
    elif ConUn == 60:
        calc_display = 32.00
    elif 60 < ConUn <= 90:
        calc_display = 38.00
    elif 91 <= ConUn <= 120:
        calc_display = 50.00
    elif 121 <= ConUn <= 180:
        calc_display = 50.00
    else:
        calc_display = 75.00
    
    print("Unit price: LKR", calc_display)

print("-----------------------------------------------------------")
print("Previous dues: LKR", CR)
print("--------------")
print("Fixed charges: LKR", fixedcharges)
print("--------------")
print(f"Total payment: LKR {Totfinaltotal:.2f}")
print("-----------------------------------------------------------")

print("This simple program is created using 'Python' by 'Arosha Silva - 2024 SURDS (ICT-A/L)'\
        Prices used to calculate are of 2023 existing tariffヾ≧▽≦*o " )  
#Please do not edit any . There were no error(s) encountered while testing nor the time saved and finished

#https://www.pucsl.gov.lk/wp-content/uploads/2023/10/20-OCT-2023-CEB.pdf

#                            *****
