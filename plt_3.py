import pandas as pd
import matplotlib.pyplot as plt
from numpy import arange

reviews = pd.read_csv('fandango_scores.csv')
cols = ['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
norm_reviews = reviews[ cols ]

#print( norm_reviews[ : 1])

#num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
#
#bar_heights = norm_reviews.loc[ 0, num_cols ].values
##print( bar_heights )
#
#bar_positions = arange( 5 ) + 0.75
#print( bar_positions )
#
#fig, ax = plt.subplots()
#ax.bar( bar_positions, bar_heights, 0.5 )
#plt.show()

fig, ax = plt.subplots()
ax.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['RT_user_norm'])
ax.set_xlabel('Fandango')
ax.set_ylabel('Rotten Tomatoes')
plt.show()
