import math
#finance calculator
#Program which allows user to select type of calculation they would like to do investment or bond and does the calculation based on that selection

#getting user input on type of calculation
print("Choose either 'investment' or 'bond' from the menu below to proceed: ")
print("")
#displaying an explanation to user of the different calculations as per task request
print("investment \t- to calculate the amount of interest you'll earn on interest")
print("bond       \t- to calculate the amount you'll have to pay on a home loan")
print("")
type_calculation = input()

#calculations based on user input, investment or bond
if type_calculation.lower() == "investment":
    #calculation if investment option is selected
    P = float(input("Please enter deposit amount: R "))
    r = (float(input("Please enter interest rate as a percentage e.g. 8: ")))/100
    t = int(input("Please enter the number of years: "))
    
    #choosing type of interest then calculating based on choosen interest
    interest = input("Choose interest type either 'simple' or 'compound': ")
    if interest.lower() == "simple":
        A = round((P*(1+r*t)),2) #simple interest formula
        print(f"Total amount = R {A} based on simple interest formula")
    elif interest.lower() == "compound":
        A = round((P*math.pow((1+r),t)),2)#compound interest formula
        print(f"Total amount = R {A} based on compound interest formula")
    else:
        print("Incorrect input!")
        
elif type_calculation.lower() == "bond":
    #calculation if bond option is selected
    P = float(input("Please enter present value of the house: R "))
    i = (float(input("Please enter interest rate as a percentage e.g. 7: ")))/100
    n = int(input("Please enter the number of months you plan to repay the bond: "))

    x = round((((i/12)*P)/(1-math.pow((1+(i/12)),(-n)))),2) #monthly bond calculation equation
    print(f"Your monthly repayment is: R {x}")
    
else:
    print("Incorrect selection!")
    
