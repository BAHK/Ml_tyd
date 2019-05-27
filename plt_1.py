import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv('unrate.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE'])
print(unrate.head(12))

#plt.plot()
#plt.show()

first_twelve = unrate[0:12]
plt.plot( first_twelve['DATE'],first_twelve['VALUE'])
plt.xticks( rotation= 45 )
plt.xlabel('Month')
plt.ylabel('Unemployment Rate')
plt.title('Monthly Unemployment Trends, 1948')
plt.show()



