import pandas as pd
import matplotlib.pyplot as plt
from numpy import arange

reviews = pd.read_csv('fandango_scores.csv')
cols = ['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
norm_reviews = reviews[ cols ]

print( norm_reviews[ : 5])

#fig, ax = plt.subplots()
#ax.boxplot( norm_reviews['RT_user_norm'])
#ax.set_xticklabels(['Rotten Tomatoes'])
#ax.set_ylim( 0,5 )
#
#plt.show()

num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']
fig, ax = plt.subplots()
ax.boxplot( norm_reviews[num_cols ].values )
ax.set_xticklabels(num_cols, rotation = 90 )
ax.set_ylim( 0,5 )

plt.show()



