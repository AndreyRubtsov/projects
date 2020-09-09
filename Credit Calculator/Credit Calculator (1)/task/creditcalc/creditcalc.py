import math
print('''What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for credit principal:''')
chose = input()
if chose == "p":
    print('Enter the annuity payment:')
    annuity = float(input())
    print('Enter the number of periods:')
    periods = float(input())
    print('Enter the credit interest:')
    credit = float(input())
    interest = credit / (12 * 100)
    res = annuity / ((interest * pow((1 + interest),periods)) / (pow((1 + interest),periods) - 1))
    print(f'Your credit principal = {round(res)}!')
if chose == "a":
    print('Enter the credit principal:')
    principal = float(input())
    print("Enter the number of periods:")
    periods = float(input())
    print('Enter the credit interest:')
    credit = float(input())
    interest = credit / (12 * 100)
    res = principal * ((interest * pow((1 + interest),periods)) / (pow((1 + interest),periods) - 1))
    print(f'Your monthly payment = {math.ceil(res)}!')
if chose == "n":
    print('Enter the credit principal:')
    principal = float(input())
    print('Enter the monthly payment:')
    annuity = float(input())
    print('Enter the credit interest:')
    credit = float(input())
    interest = credit / (12 * 100)
    res = math.log((annuity / (annuity - principal * interest)),(1 + interest))
    year = round(res) / 12 
    month = res % 12
    if month != 0 and year != 0:
        print(f'It will take {round(year)} years and {math.ceil(month)} months to repay this credit!')
    if month == 0 and year != 0:
        print(f'It will take {round(year)} years to repay this credit!')
    if month != 0 and year == 0:
       print(f'It will take {round(month)} months to repay this credit!')