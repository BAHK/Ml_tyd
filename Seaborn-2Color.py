import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set( rc = { "figure.figsize": ( 6, 6 )})

current_palette = sns.color_palette()
#sns.palplot( current_palette )
#sns.palplot( sns.color_palette( "Blues" ) )
sns.palplot( sns.color_palette( "BuGn_r" ) )
#plt.show()

#data = np.random.normal( size = ( 20, 8 )) + np.arange ( 8 ) / 2
#sns.boxplot( data = data, palette = sns.color_palette("hls", 8))
#plt.show()

x, y = np.random.multivariate_normal([0,0],[[1, -5],[-.5,1]], size = 300).T
pal = sns.dark_palette("green", as_cmap = True )
sns.kdeplot( x , y, cmap = pal)
plt.show()
