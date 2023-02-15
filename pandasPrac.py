import pandas as pd

mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

a = [1, 7, 2]
# take a list, and turn it into a series

# series is like a column in a table

#can call specific values with an index argument. can also use that to name labels. in absense of labels, index is used



myvar = pd.Series(a, index = ['x', 'y', 'z'])

# print(myvar['y'])


#dataframe: 2d data structure, like a 2d array, or table w/ rows and columns

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

# now we load it into a dataframe object

df = pd.DataFrame(data, index=["day1", "day2", "day3"])
# when accessing mulitple locations, it makes a sub-dataframe
# print(df.loc[[0, 1]])

# print(df)

# print(pd.options.display.max_rows)
#60 rows is default

df2 = pd.read_csv("data.csv")


df3 = pd.read_json("data.json")

# print(df2.tail(7))
# print(df2.head())

# print(df3.info())
# tells you number of rows and columns, how many entries in each, and data type of each, memory usage

#When there are null vals, we should remove them. Cleaning. 



new_df = df2.dropna()

df2.dropna(inplace = True)

# print(new_df.info())

# instead of dropping columns with empty cells, we can fill them
df3.fillna(130, inplace = True)

# print(df3.info())
#now df3 has no emtpy cells

#replace just specific  column emtpy vals

df4 = pd.read_csv("data.csv")
# print(df4.to_string())

df4["Calories"].fillna(130, inplace = True)
# print(df4.to_string())


df = pd.read_csv("data.csv")

# print(df["Calories"].mode()[0])
#need the [0] because otherwise you get a series, starting with 0? then the mode? or multimodes?

x = df["Calories"].mode()[0] 
#weird, b/c doesn't seem like you can put anythiing errlse in the brackets. 

df["Calories"].fillna(x, inplace = True)


df["Date"] = pd.to_datetime(df["Date"])
#this changes NaN to NaT...still a null val. fixes the other date format tho

#remove the row w/ the Nat val

df.dropna(subset= ["Date"], inplace = True)

#interesting...it doesn't reindex. there just isn't a row 22 anymore

#fixing values: not emtpy, or wrong format, but just entered incorrectly. i.e. 450 min duration for workout

#can replace on case by case basis for a small data set like this

df.loc[7, "Duration"] = 45

#but that's impracttical. for large sets, we have to set some rules, then loop through data apply them, like this. for each row in the index, if the duration value at that row is more than 120, replace it with 120

for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"] = 120

# or just drop the row if the data is wrong

for y in df.index:
    if df.loc[y, "Duration"] <= 0:
        df.drop(y, inplace = True)



#rm duplicates...first check for themn:
print(df.duplicated())

# to rm, drop dupes method

df.drop_duplicates(inplace = True)
# rm row 12, which was a dupe of 11
print(df.to_string())