from pandas import read_table

#using CostId as index in dataframe
dogs_dataframe = read_table("dogslogs.tsv", index_col='CostId')

#finding max CostValue an printing the whole string all information
string_with_maxcost = dogs_dataframe['CostValue'].idxmax()
print (df.loc[string_with_maxcost])