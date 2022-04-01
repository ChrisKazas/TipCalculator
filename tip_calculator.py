'''The MIT License (MIT)

Copyright (c) 2022 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''


# get cost of food
def get_bill():
    
    try:
        cost = float(input("What is the cost of the meal? "))
    except Exception as e:
        print('ERROR: Value must be a number')
        cost = float(input("What is the cost of the meal? "))
        
    return cost

# get number of diners
def get_num_diners():
    try:
        usr_input = float(input("How many diners will be splitting the bill? "))
    except Exception as e:
        print("ERROR: Value must be a number")
        usr_input = float(input("How many diners will be splitting the bill? "))
    
    return usr_input

# get tip percentage
def get_tip_percentage():
    try:
        usr_input = float(input("What will the tip percentage be? "))
    except Exception as e:
        print("ERROR: Value must be a number")
        usr_input = float(input("What will the tip percentage be? "))
        
    return usr_input / 100 

# return total cost for dinner
def get_total(bill_total, tip_rate):
    return (bill_total + (bill_total * tip_rate) + (bill_total * .1))

# return the cost per diner
def get_split(bill, num_diners):
    return bill / num_diners

# run the program
def calculate():
    calcuate = "y"
    while calcuate.lower() == "y":
        bill_wo_tx = get_bill()
        num_diners = get_num_diners()
        tip_rate = get_tip_percentage()
        total_bill = round(get_total(bill_wo_tx, tip_rate), 2)
        split = round(get_split(total_bill, num_diners), 2)
        
        print('Total cost of dinner: ', total_bill)
        print('Cost per diner: ', split)
        
        
        print("Please choose Y or N")
        calcuate = input("Would you like to calculate another tip? Y or N: ")
        while calcuate.lower() != "y" and calcuate.lower() != 'n':
            print("please choose Y or N")
            calcuate = input("Would you like to calculate another tip? Y or N: ")


calculate()



# unit testing

# Inputs
# * Food costs $15
# * 1 person paying
# * 20% tip

# Expected output:
# * `Total bill: $19.50`

#### A feast to remember

# Inputs
# * Food costs $25000000
# * 3 people paying
# * 31% tip

# Expected output:
# * `Total bill: $35,250,000.00`
# * `Each person should pay $11,750,000.00`

# #### No tip

# Inputs
# * Food costs $78.99
# * 6 people paying
# * 0 tip

# Expected output:
# * `Total bill: $86.89`
# * `Each person should pay $14.48`

#### Sharing the bill among many

# Inputs:
# * Food costs $5000
# * 876 people paying
# * 12% tip

# Expected output:
# * `Total bill: $6,100.00`
# * `Each person should pay $6.96`



