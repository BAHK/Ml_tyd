from pandas import Series
import pandas as pd

fandango = pd.read_csv('fandango_score_comparison.csv')
series_film = fandango['FILM']
#print( type(series_film))
#print(series_film[0:5])
series_rt = fandango['RottenTomatoes']
#print( series_rt[0:5])

film_names = series_film.values
print(type(film_names))
#print(film_names)
rt_scores = series_rt.values
#print(rt_scores)
series_custom = Series(rt_scores , index = film_names)
print(series_custom[['Minions (2015)','Leviathan (2014)']])

