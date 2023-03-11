#CBS Data collection

#Retrieve data from Centraal Bureau voor de Statistiek with Python

#Installation
#From PyPi

# pip install cbsodata

import cbsodata
import pandas as pd

# search the data on CBS website
# https://www.cbs.nl/nl-nl/cijfers/detail/85445NED?q=brede%20welvaart
# https://www.cbs.nl/nl-nl/cijfers/detail/84842NED

lifeExpentancy = pd.DataFrame(cbsodata.get_data('85445NED'))
lifeExpentancy = lifeExpentancy[['LeeftijdOp31December','InkomenEnWelvaart', 'Levensverwachting_1']]
 
print(lifeExpentancy.tail())
print(lifeExpentancy)

lifeExpentancy_Onderwijs = pd.DataFrame(cbsodata.get_data('84842NED'))
lifeExpentancy_Onderwijs = lifeExpentancy_Onderwijs[['LeeftijdOp31December','Onderwijsniveau','Levensverwachting_1']]
 
print(lifeExpentancy_Onderwijs.tail())
print(lifeExpentancy_Onderwijs)

lifeExpentancy_diff= pd.merge(lifeExpentancy, lifeExpentancy_Onderwijs, how='inner',on = ['LeeftijdOp31December', 'Levensverwachting_1'])

lifeExpentancycap_diff = lifeExpentancy_diff.fillna(0) #NaN=0
print(lifeExpentancycap_diff.head) 

# save dataframe to csv
lifeExpentancycap_diff.to_csv('levensverwachting.csv')