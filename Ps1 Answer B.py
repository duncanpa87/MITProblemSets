# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 14:46:21 2019

@author: Duncan Aronstein
"""
portion_down_payment = .25
current_savings = 0
r = .04 #Annual rate of return of savings
annual_salary = float(input("Enter your salary: "))
portion_saved = float(input("Enter the percentage of salary you will save annually, as a decimal: "))
total_cost = float(input("Enter the price of your dream home: "))
semi_annual_raise = float(input("What's your semi ann raise as a decimal %? "))
months = 0
while current_savings < portion_down_payment*total_cost:        
    if months%6 == 0 and months > 0:
        annual_salary *= (1+semi_annual_raise)
    months +=1
    current_savings += (current_savings*r + annual_salary*portion_saved)/12
print("It will take you",months,"months to afford your dream home which now costs double sorry")