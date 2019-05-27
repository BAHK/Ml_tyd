import pandas

food_info = pandas.read_csv("food_info.csv")

print( type( food_info ))
#print( food_info.dtypes)
#print( help( pandas.read_csv))


head = food_info.head(6)
tail = food_info.tail(8)
print( "====== head ======")
print( head )
print( "====== tail ======")
print( tail )


print( "====== The columns Name ======")
print( food_info.columns )

print( food_info.shape )


print( food_info.loc[0] )

print( food_info.loc[3:6] )

ndb_col = food_info[ "NDB_No" ]
print( ndb_col )

columns = ["Zinc_(mg)", "Copper_(mg)"]
zinc_copper = food_info[ columns ]
print( zinc_copper )


col_names = food_info.columns.tolist()
print( col_names )
gram_columns = []

for c in col_names:
    if c.endswith("(g)"):
        gram_columns.append( c )
gram_df = food_info[ gram_columns ]
print( gram_df.head( 3 ))





