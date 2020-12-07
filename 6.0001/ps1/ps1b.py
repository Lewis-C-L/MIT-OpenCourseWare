#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:27:17 2020

@author: lewisling
"""
# Part B


# initializations
portion_down_payment = 0.25
current_savings = 0
r = 0.04
i=0

# inputs
print("Enter your annual salary:​")

annual_salary = float(input())

print("Enter the percent of your salary to save, as a decimal:​")
portion_saved = float(input())

print("Enter the cost of your dream home:")
total_cost = float(input())

print("Enter the semi­annual raise, as a decimal:​")
semi_annual_raise = float(input())


# Calculations

down_payment = total_cost * portion_down_payment
monthly_salary = annual_salary/12
monthly_saved = monthly_salary * portion_saved

while current_savings<down_payment:
      
    current_savings = (1+r/12) * current_savings
    current_savings = current_savings + monthly_saved*(1+semi_annual_raise)**(i//6)
    
    i +=1


# Outputs

print("Number of months:​",i)
