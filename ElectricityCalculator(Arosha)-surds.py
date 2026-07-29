#This code can calculate and provide the total payable ammount

from itertools import count
from tkinter import UNITS
from typing import Counter

text = "Welcome to Electricity bill calculator.Please provide the data correctly.This program will provide the Total payment with fixed charges included."
width = 20
centered_text = text.center(width)
print(centered_text)

#Gets units
PrevU=float(input("Enter the previous Units    : ")) 
NewU=float(input("Enter the current month Units: "))

#Fix_charges=input("Do You need the Total payment to be displayed including Fixed charges? (Y/N)")


#Gets no of CONSUMED units (this month)
ConUn = NewU-PrevU
CR=0
if ConUn< 0 :
    print("ERROR!!, NO. Of Units be positive value, Process cannot continue, Please Check Again")
    
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
#Starts Process ////////////////////////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#=======================================================================================================================================================#
# Units less than or equal to 60
if ConUn < 60:
     if ConUn == 0:
        Totunitcon = 0
        ConUnNew=ConUn
        calc = 0.00
        calc1=calc
        fixedcharges=150.00
     elif ConUn<=30:
          Totunitcon=0
          ConUnNew=ConUn
          calc=10.00
          calc2=calc
          fixedcharges=150.00
     else:
          Totunitcon=30*10
          ConUnNew=ConUn-31
          calc=25.00
          calc3=calc
          fixedcharges=300.00
# Units less than or equal to 180 !!!!!!!!! Second phase of checking !!!!!!!!!
elif ConUn>=60:
    
    if ConUn==60:
        Totunitcon=0                                         #Totunitcount = charges till that amount
        ConUnNew=ConUn  
        calc=32.00
        calc4=calc                        #ConUnNew is used to get the value of the no. of units that needs to be calculated of that range 
        fixedcharges=300.00                              #eg - if the bill is 70 and the range is ConUn<=90 the no. of units that will be calculated is 70-60 = 10*38
        
    elif ConUn<=90:
        Totunitcon=SBlock
        ConUnNew=ConUn-61
        calc=38.00
        calc5=calc
        fixedcharges=400.00
        
    elif ConUn<=120:
        Totunitcon=TBlock
        ConUnNew=ConUn-91
        calc=50.00
        calc6=calc
        fixedcharges = 1000.00
    else :#ConUn<=180:  @@
        if ConUn<=180:
            Totunitcon=FOBlock
            ConUnNew=ConUn-121
            calc = 50.00
            calc7=calc
            fixedcharges = 1500.00
        else:     #Last check ( ConUn >= 181 ) !!@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@!!
            Totunitcon=lBlock
            ConUnNew=ConUn
            calc=75.00
            calc8=calc 
            fixedcharges=2000.00
# Units greater than 180
#elif ConUn>180:
   # calc=75
    #fixedcharges=1500
    
else:
    print("Please check the 'No. of Units' You have entered. VALUES BELOW 0 IS NOT ALLOWED")

# Calculation starts/////////////////////////////////////////////////////////////////////////////////

TotalPayment=(calc*ConUnNew)

#final calculation////////////////////////////////////////////////

# Addition of DUE/CR if available
if CR>=0:
    Totfinaltotal=TotalPayment+Totunitcon+fixedcharges+CR
else:
    Totfinaltotal=TotalPayment+Totunitcon+fixedcharges

#//////////////////////////////////////////////////////////////
print("--------------")
print("Units consumed:", ConUn, "(Units)")
print("--------------")  #Used to seperate neatly

if Totfinaltotal==180:
                                #This will help to fix errors if 0 or negative value is entered.
    print("No units have been consumed, this price only includes 'Fixed charges'")
    print("--------------")
    
else:
#TotalCount=Total_Payment+fixedcharges
     if ConUn <0:
          print("Unit Price: LKR",calczero, )
     elif ConUn == 0:
          print("Unit price: LKR",calc1,)
     elif ConUn <=30:
          print("Unit price: LKR",calc2,)
     elif 30 <ConUn <=60:
          print("Unit price: LKR",calc3,)
     elif ConUn == 60 :
          print("Unit price: LKR",calc4,)
     elif 60 < ConUn <=91 :
          print("Unit price: LKR",calc5,)
     elif 91 < ConUn <=120 :
          print("Unit price: LKR",calc6,)
     elif 121 < ConUn <=180 :
          print("Unit price: LKR",calc7,)
     else:
          print("Unit price: LKR",calc8,)
     
print("-----------------------------------------------------------")
print("Previous dues: LKR",CR,)
print("--------------")
print("Fixed charges: LKR",fixedcharges,)
print("--------------")
print(f"Total payment: LKR {Totfinaltotal:.2f}")
print("-----------------------------------------------------------")

print("This simple program is created using 'Python' by 'Chaveen Arosha - 2024 SURDS'\
        Prices used to calculate are of 2023 existing tariffヾ≧▽≦*o " )  
#Please do not edit any . There were no error(s) encountered while testing nor the time saved and finished
#https://www.pucsl.gov.lk/wp-content/uploads/2023/10/20-OCT-2023-CEB.pdf
  
