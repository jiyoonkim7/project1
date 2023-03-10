#CBS Data collection

#Retrieve data from Centraal Bureau voor de Statistiek with Python

#Installation
#From PyPi

# pip install cbsodata

import cbsodata
import pandas as pd

InkomenEnWelvaart = pd.DataFrame(cbsodata.get_data('85445NED'))
InkomenEnWelvaart = InkomenEnWelvaart[['LeeftijdOp31December', 'InkomenEnWelvaart','InkomenEnWelvaart']]
 
print(InkomenEnWelvaart.tail())

lifeExpentancy = pd.DataFrame(cbsodata.get_data('85445NED'))
lifeExpentancy = lifeExpentancy[['LeeftijdOp31December','InkomenEnWelvaart', 'Levensverwachting_1','LeeftijdOp31December']]
 
print(lifeExpentancy.tail())
print(lifeExpentancy)


