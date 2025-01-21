import pandas as pd

data = pd.read_csv('state_crop_data.csv', thousands=',')

corn_planted = data[data['Data Item'] == 'CORN - ACRES PLANTED'].copy()
corn_planted['Value'] = pd.to_numeric(corn_planted['Value'])

corn_harvested = data[data['Data Item'] == 'CORN, GRAIN - ACRES HARVESTED'].copy()
corn_harvested['Value'] = pd.to_numeric(corn_harvested['Value'])

corn_yield = data[data['Data Item'] == 'CORN, GRAIN - YIELD, MEASURED IN BU / ACRE'].copy()
corn_yield['Value'] = pd.to_numeric(corn_yield['Value'])

corn_planted = corn_planted[['Year', 'State', 'Value']].rename(columns={'Value': 'Planted'})
corn_harvested = corn_harvested[['Year', 'State', 'Value']].rename(columns={'Value': 'Harvested'})
corn_yield = corn_yield[['Year', 'State', 'Value']].rename(columns={'Value': 'Yield Per Acre'})

merged_data = corn_planted.merge(corn_harvested, on=['Year', 'State']).merge(corn_yield, on=['Year', 'State'])

print(merged_data)

merged_data.to_csv('state_crop_data_merged.csv', index=False)
