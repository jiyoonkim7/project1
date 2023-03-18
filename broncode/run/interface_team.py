#!/usr/bin/env python

import pickle
import logging
import pandas as pd
import sys
import statsmodels as sm
import statsmodels.formula.api as smf
import sqlite3
from datetime import datetime
45

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


print ()
gdpr_check = input('Please ask if the patient grants permission to save the input of the data reguarding their current habits in accordance with the GDPR. If permission is granted type: Yes : ').title()


if gdpr_check == 'Yes':
    print ('This sessions patients initial data will be saved')
    client_nr = input ('Enter the patient nr : ').title()
    
    
else:
    print ('No data will be saved this session')


#hide errors, scary for the user xD
sys.tracebacklimit = 0 

# input safeguarding


def inputDigit(message, acceptableRange):
    inputStr = str()
    withinRange = False
    numberOfTries = 3
    inputNum = None
    i = 0

    while not (inputStr.isdigit() and withinRange) and i < numberOfTries:
        inputStr = input(message)
        logging.debug(inputStr)

        if inputStr.isdigit():
            inputNum = float(inputStr)

            if inputNum in acceptableRange:
                return inputNum

        i += 1
        if i == 3:
            raise Exception("Number of incorrect inputs has been exceded. Programe will quit. It can be started again.")

    return None



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

# create df to be saved and save it in SQL
# create date
date = datetime.now().strftime("%Y-%m-%d")

if gdpr_check == 'Yes':
    data_to_save = {'feature': ['client_nr','date','lifespan_predict','genetic', 'length', 'mass', 'alcohol', 'sugar', 'smoking', 'exercise'],
        f'{client_nr}_{date}': [client_nr, date, lifespan_predict, genetic, length, mass, alcohol, sugar, smoking, exercise]}

    df_to_SQL = pickle.dump(regressor, open('regressor_out.pkl', "wb"))

    

# close SQL connection
#dbConnection.close()

    # print (df_to_SQL)

# df_save_to_SQLlite = 
############## nog bouwen!!!!!!!!!!

# transpose df input for finish function55
# df_input=df_input.transpose()

# print(df_input)
# df_input['predicted_lifespan']=[lifespan_predicted]

def finised ():
    end_programme = input('press any key to show all results and exit the programme.')
    print()
    print (df_input)
    return quit()

 