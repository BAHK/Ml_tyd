import pandas as pd
import numpy as np

titanic_survival = pd.read_csv("titanic_train.csv")
#print("===============  Titanic Train Head =============")
#print( titanic_survival.head())

age = titanic_survival["Age"]
#print("========================")
#print(age.loc[0:10])

#print("========================")
age_is_null = pd.isnull(age)
#print( age_is_null )
age_null_true = age[ age_is_null ]
#print( age_null_true )
age_null_count = len( age_null_true )

mean_age = sum(titanic_survival["Age"]) / len(titanic_survival["Age"])
#print( mean_age )

good_ages = titanic_survival["Age"][age_is_null == False]
correct_mean_age = sum(good_ages) / len( good_ages )
#print( correct_mean_age )


good_ages = titanic_survival["Age"].mean()
#print( correct_mean_age )


passenger_survival = titanic_survival.pivot_table(index = "Pclass", 
        values = "Survived", aggfunc = np.mean )
#print( passenger_survival )


port_stats = titanic_survival.pivot_table(index = "Embarked", 
        values = ["Fare","Survived"], aggfunc = np.sum )
#print( port_stats )


new_titanic_survival = titanic_survival.sort_values("Age",ascending = False)
#print( new_titanic_survival[0:10] )
titanic_reindexed = new_titanic_survival.reset_index( drop = True )
#print("-------------------")
#print( titanic_reindexed[0:10] )

def hundredth_row(column):
    hundredth_item = column.loc[99]
    return hundredth_item

hundredth_row = titanic_survival.apply( hundredth_row )

def not_null_count( column ):
    column_null = pd.isnull( column )
    null = column[column_null]
    return len( null )

column_null_count = titanic_survival.apply( not_null_count )

#print( hundredth_row )
print( column_null_count )





