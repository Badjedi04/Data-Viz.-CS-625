import pandas as pd

# read in the original dataset
data = pd.read_csv('co-est2019-alldata.csv', encoding='latin1')

# drop rows that are aggregate with respect to States
data.drop(data[data['STNAME'] == data['CTYNAME']].index, inplace=True)

# save the modified dataset to a new CSV file
data.to_csv('original_dataset.csv')

# select only the required columns
data = data[['STNAME', 'CTYNAME', 'CENSUS2010POP', 'POPESTIMATE2015', 'POPESTIMATE2019']]

# convert the value columns to rows
data = data.melt(id_vars=['STNAME', 'CTYNAME'], var_name="Year", value_name="Population")

# sort the data by population in descending order
data = data.sort_values(by=['Population'], ascending=False)

# save the modified dataset to a new CSV file
data.to_csv('final_dataset.csv')

# remove the 3rd and 2nd Quartiles from the data
data.drop(data[data['Population'] > (data['Population'].max() * 0.75)].index, inplace=True)
data.drop(data[data['Population'] < (data['Population'].max() * 0.25)].index, inplace=True)

# save the modified dataset to a new CSV file
data.to_csv('final_dataset_without_outliers.csv')

# select only the rows where STNAME is equal to CTYNAME
dataset = pd.read_csv('co-est2019-alldata.csv', encoding='latin1')
dataset = dataset[dataset['STNAME'] == dataset['CTYNAME']]

# sort the data by CENSUS2010POP in descending order
dataset = dataset.sort_values(by=['CENSUS2010POP'], ascending=False)

# save the modified dataset to a new CSV file
dataset.to_csv('dataset_state_population.csv')

# select only the rows where STNAME is equal to CTYNAME and select the required columns
dataset_1 = pd.read_csv('co-est2019-alldata.csv', encoding='latin1')
dataset_1 = dataset_1[dataset_1['STNAME'] == dataset_1['CTYNAME']]
dataset_1 = dataset_1[['STNAME', 'POPESTIMATE2010', 'POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015', 'POPESTIMATE2016', 'POPESTIMATE2017', 'POPESTIMATE2018', 'POPESTIMATE2019']]

# convert the value columns to rows
dataset_1 = dataset_1.melt(id_vars=['STNAME'], var_name="Year", value_name="Population")

# sort the data by population in descending order
dataset_1 = dataset_1.sort_values(by=['Population'], ascending=False)

# save the modified dataset to a new CSV file
dataset_1.to_csv('dataset_pivot_popest.csv')

# select the required columns and sort the data by POPESTIMATE2019 in descending order
birthdata = pd.read_csv('co-est2019-alldata.csv', encoding='latin1')
birthdata.drop(birthdata[birthdata['STNAME'] == birthdata['CTYNAME']].index, inplace=True)
birthdata = birthdata[['STNAME', 'CTYNAME', 'POPESTIMATE2019', 'BIRTHS2019']]
birthdata = birthdata.sort_values(by=['POPESTIMATE2019'], ascending=False)

# save the modified dataset to a new CSV file
birthdata.to_csv('dataset_birthdata.csv')