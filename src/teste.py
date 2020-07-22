import pandas as pd
from datetime import datetime

historic = pd.DataFrame(columns=['last_event', 'enabled_events', 'states', 'time'])

print("Empty Dataframe ", historic, sep='\n')

time = datetime.now().strftime("%H:%M:%S")


historic = historic.append({"last_event" : 'bat_L', "enabled_events": [], "states":[], "time": time}, ignore_index=True)

print("Dataframe Contens ", historic, sep='\n')

historic = historic.append({"last_event" : 'bat_OK', "enabled_events": [], "states":[], "time": time}, ignore_index=True)
historic = historic.append({"last_event" : 'bat_Ossss', "enabled_events": [], "states":[], "time": time}, ignore_index=True)

print("Dataframe Contens ", historic, sep='\n')

print(historic.tail(1))

historic.loc[historic.tail(1).index,'enabled_events'] =  ['battt']
print("Dataframe Contens ", historic, sep='\n')

e = historic.tail(1)['enabled_events'].array[0]
print(e)

print("\n\n")
x = None
print(historic.tail(1).index[0] == x)

x = historic.tail(1)
print(historic.tail(1).index[0])