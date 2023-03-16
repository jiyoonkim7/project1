#!/usr/bin/env python

import pickle
import logging
import pandas as pd
import sys

sys.tracebacklimit = 0 #hide errors, scary for the user xDhh

#regModel = "../models/regressor.pkl"

with open('regressor.pkl', "rb") as f:
    regressor = pickle.load(f)



genetic = float(input("Fill in your age: "))
length = float(input("Fill in your height : ")) 
mass = float(input ("Fill in your weight in kg: "))
alcohol = float(input("Fill in the glasses of alcohol per day: "))
sugar = float(input("Enter the number of sugar cubes per day: "))
smoking = float(input("Enter the number of cigarettes per day: "))
exercise = float(input("Enter the number of hours of exercise per day: "))
divider = pow(length/100, 2) if length >0 else None
bmi = round(mass/divider)
logging.debug(f'bmi: {bmi}')

data = {'genetic': genetic, 'length':[length],'mass': [mass], 'exercise': [exercise],
                                 'smoking': [smoking], 'alcohol': [alcohol], 'sugar': [sugar], 
                                   'bmi': [bmi]}
 
df = pd.DataFrame.from_dict(data )
 
lifespan_predict = regressor.predict(df)

df['predict']=lifespan_predict

premie_factor = genetic/lifespan_predict

premie_korting = (1-premie_factor)*100

print()
NewBMI = ("{:.2f}".format(bmi))

if bmi <= 18.5:
    print(f"Your BMI is {NewBMI}. It falls within the underweight range.")
elif bmi <= 22.9:
    print(f"Your BMI is {NewBMI}. This is normal.")
elif bmi <= 24.9:
    print(f"Your BMI is {NewBMI}. It falls within the healthy weight range.")
elif bmi <= 29.9:
    print(f"Your BMI is {NewBMI}. It falls within the overweight range.")
else:
    print(f"Your BMI is {NewBMI}.It falls within the obesity range.")
print()

print()
print(f'The life expectation is: {lifespan_predict}')
print(f'bmi is: {bmi})')
print()
if premie_korting > 0:
    print(f'The premium discount is: {premie_korting} %')
else:
    print(f'The premium increase is: {abs(premie_korting)} %')
print()
print()

 