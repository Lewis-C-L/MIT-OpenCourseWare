#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:45:02 2020

@author: lewisling
"""

semi_annual_raise = 0.07
r = 0.04
portion_down_payment = 0.25
total_cost = 1000000
current_savings = 0
i=0
bisections = 0


print("Enter the starting salary:")
annual_salary = float(input())


# Calculations
down_payment = total_cost * portion_down_payment
monthly_salary = annual_salary/12


portion_saved = 0.5
bottom = 0
top = 1
Accuracy = 100
stop_val = Accuracy + 1


####
monthly_saved = monthly_salary
while i<37:
      
    current_savings = (1+r/12) * current_savings
    current_savings = current_savings + monthly_saved*(1+semi_annual_raise)**(i//6)
    
    i +=1

if current_savings<down_payment:
    print("It is not possible to pay the down payment in three years.")
#####
else:
    while stop_val>Accuracy:
        monthly_saved = monthly_salary * portion_saved
        current_savings=0
        i=0
        while current_savings<down_payment:
          
            current_savings = (1+r/12) * current_savings
            current_savings = current_savings + monthly_saved*(1+semi_annual_raise)**(i//6)  
            i += 1
       
        
        if i <=36:
            top = portion_saved                     
        else:
            bottom = portion_saved                  
        
        portion_saved = (bottom + top) / 2   
        bisections += 1
        stop_val = abs(down_payment-current_savings)
    
    print("Best Saving Rate:",portion_saved)    
    print("Steps in bisection search:",bisections)

   
    
    
    