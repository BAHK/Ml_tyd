import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#fig = plt.figure()
#ax1 = fig.add_subplot(4,3,1)
#ax2 = fig.add_subplot(4,3,2)
#ax3 = fig.add_subplot(4,3,6)
#ax12= fig.add_subplot(4,3,12)
#
#ax1.plot( np.random.randint( 1,5,5 ), np.arange( 5 ))
#ax2.plot( np.arange( 10 ) * 3, np.arange( 10 ))

unrate = pd.read_csv('unrate.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE'])

unrate['MONTH'] = unrate['DATE'].dt.month
#unrate['MONTH'] = unrate['DATE'].dt.month
fig = plt.figure(figsize = ( 6, 3 ))

plt.plot(unrate[0:12]['MONTH'], unrate[0:12]['VALUE'], c = 'red')
plt.plot(unrate[12:24]['MONTH'], unrate[12:24]['VALUE'], c = 'blue')
plt.legend( loc='best' )

plt.show()

