import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('NYC_Central_Park_weather_1869-2022.csv')
year1869=(df[i] for df['DATE'] in '1869')
#print(df.head())

#fig, ax=plt.subplots(figsize=(20, 2))

#df.plot(x='DATE', y='TMAX', kind='line', rot=45)
#plt.show()

