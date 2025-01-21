import pandas as pd

def load_data(file_path, state_name, variable_name):
    df = pd.read_csv(file_path)
    df['Year'] = df['Date'].astype(str).str[:-4]
    df = df.rename(columns={'Value': variable_name})
    df = df[['State', 'Year', variable_name]]
    df['State'] = state_name
    return df

kansas_temp = load_data('kansas-average-temp.csv', 'Kansas', 'Avg_Temp')
missouri_temp = load_data('missouri-average-temp.csv', 'Missouri', 'Avg_Temp')
ohio_temp = load_data('ohio-average-temp.csv', 'Ohio', 'Avg_Temp')
virginia_temp = load_data('virginia-average-temp.csv', 'Virginia', 'Avg_Temp')
wisconsin_temp = load_data('wisconsin-average-temp.csv', 'Wisconsin', 'Avg_Temp')
df_temp = pd.concat([kansas_temp, missouri_temp, ohio_temp, virginia_temp, wisconsin_temp], ignore_index=True)

kansas_prep = load_data('kansas-average-precipitation.csv', 'Kansas', 'Precipitation')
missouri_prep = load_data('missouri-average-precipitation.csv', 'Missouri', 'Precipitation')
ohio_prep = load_data('ohio-average-precipitation.csv', 'Ohio', 'Precipitation')
virginia_prep = load_data('virginia-average-precipitation.csv', 'Virginia', 'Precipitation')
wisconsin_prep = load_data('wisconsin-average-precipitation.csv', 'Wisconsin', 'Precipitation')
df_prep = pd.concat([kansas_prep, missouri_prep, ohio_prep, virginia_prep, wisconsin_prep], ignore_index=True)

df = df_temp.merge(df_prep)

print(df.head(40))
df.to_csv('statewise_weather.csv', index=False)
