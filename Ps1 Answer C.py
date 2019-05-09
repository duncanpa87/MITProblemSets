# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 21:04:56 2019

@author: Duncan Aronstein
"""

r = .04 #Annual rate of return of savings
low = 1
high = 10000
guess = int((low + high)/2)
semi_annual_raise = .07
annual_salary = float(input("Enter your salary: "))
x = annual_salary
months = 36
for i in range(20):
    annual_salary = x
    print(i)
    current_savings = 0
    guess = int((low + high)/2)
    print('guess:',guess)
    for i in range(36):        
        if i%6 == 0 and i > 0:
            annual_salary *= (1+semi_annual_raise)
        current_savings += (current_savings*r + annual_salary*guess/10000)/12
    print('savings: %.2f'%current_savings)
    if current_savings-250000 > 100:
        high = guess
        print('high:',high)
    elif 250000-current_savings > 100:
        if low == guess:
            print("Need more money" if guess == 9999 else "Income over 9000! You need a better house")
            break
        low = guess
        print('low:',low)
    else:
        print('winning guess =', guess/10000)
        break

   