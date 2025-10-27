import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df_tesla = pd.read_csv('Google Trends Data Viz (start)/TESLA Search Trend vs Price.csv')

df_btc_search = pd.read_csv('Google Trends Data Viz (start)/Bitcoin Search Trend.csv')
df_btc_price = pd.read_csv('Google Trends Data Viz (start)/Daily Bitcoin Price.csv')

df_unemployment = pd.read_csv('Google Trends Data Viz (start)/UE Benefits Search vs UE Rate 2004-19.csv')
df_ue_2020 = pd.read_csv('Google Trends Data Viz (start)/UE Benefits Search vs UE Rate 2004-20.csv')

df_ue_2020.MONTH = pd.to_datetime(df_ue_2020['MONTH'])

print("TESLA DataFrame")
print(f"Shape of the DF : {df_tesla.shape}")
print(f"Size of the DF : {df_tesla.count()}")
print(f"Columns of the DF : {df_tesla.columns.tolist()}")

largest_search_value = df_tesla['TSLA_WEB_SEARCH'].describe()['max']
print(f"Largest search value: {largest_search_value}")

print(f"NaN? : {df_tesla.isna().values.any()}")


print(type(df_tesla['MONTH']))

df_tesla['MONTH'] = pd.to_datetime(df_tesla['MONTH'])

print(df_tesla['MONTH'].dtype)



print("----------------------------------------------------")

print("Unemployment DataFrame")
print(f"Shape of the DF : {df_unemployment.shape}")
print(f"Size of the DF : {df_unemployment.count()}")
print(f"Columns of the DF : {df_unemployment.columns.tolist()}")
largest_search_value_ue = df_unemployment['UE_BENEFITS_WEB_SEARCH'].describe()['max']
print(f"Largest search value: {largest_search_value_ue}")

print(f"NaN? : {df_unemployment.isna().values.any()}")
df_unemployment['MONTH'] = pd.to_datetime(df_unemployment['MONTH'])
print(df_unemployment['MONTH'].dtype)


print("----------------------------------------------------")

print("Btc_search DataFrame")
print(f"Shape of the DF : {df_btc_search.shape}")
print(f"Size of the DF : {df_btc_search.count()}")
print(f"Columns of the DF : {df_btc_search.columns.tolist()}")
largest_search_value_btc_search = df_btc_search['BTC_NEWS_SEARCH'].describe()['max']
print(f"Largest search value: {largest_search_value_btc_search}")

print(f"NaN? : {df_btc_search.isna().values.any()}")
df_btc_search['MONTH'] = pd.to_datetime(df_btc_search['MONTH'])
print(df_btc_search['MONTH'].dtype)
print(df_btc_search.head(5))

print("----------------------------------------------------")

print("Btc_price DataFrame")
print(f"Shape of the DF : {df_btc_price.shape}")
print(f"Size of the DF : {df_btc_price.count()}")
print(f"Columns of the DF : {df_btc_price.columns.tolist()}")
largest_search_value_btc_search = df_btc_price['VOLUME'].describe()['max']
print(f"Largest search value: Data Not found !")

print(f"NaN? : {df_btc_price.isna().values.any()}")
print(f"Number of NaN : {df_btc_price.isna().sum()}")

df_btc_price = df_btc_price.dropna()
print(f"Number of NaN after Cleaning: {df_btc_price.isna().sum()}")
df_btc_price['DATE'] = pd.to_datetime(df_btc_price['DATE'])
print(df_btc_price['DATE'].dtype)
df_btc_price.set_index('DATE', inplace=True)
df_btc_price = df_btc_price.resample('M').last()
print(f"Monthly BitCoints Price : {df_btc_price.head(5)}")


# Graphs constructions :
# TESLA 👇
plt.figure(figsize=((14,8)), dpi=100)
plt.xlabel("Years")

plt.xticks(ticks=df_tesla.MONTH, rotation=45, fontsize=12)
plt.title('Tesla Web Search vs Price')
plt.grid()

ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.set_xlim(pd.Timestamp('2010-01-01'), pd.Timestamp('2020-12-31'))

ax1.set_ylabel('TSLA Stock Price', color= 'blue', fontsize=14)
ax2.set_ylabel('Search Trend', color='red', fontsize=14)


ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color='#FF2A00', linewidth=3)
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color= 'steelblue', linewidth=3)

# Locators
years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_minor_locator(months)
plt.tight_layout()
# BITCOIN 👇
plt.figure(figsize=((14,8)), dpi=100)
plt.xlabel("Years")

plt.xticks(rotation=45, fontsize=12)
plt.title('Bitcoin News Search vs resampled Price')
plt.grid()

ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.set_xlim(pd.Timestamp('2014-09-17'), pd.Timestamp('2020-09-28'))

ax1.set_ylabel('Search Trend', color= 'blue', fontsize=14)
ax2.set_ylabel('BTC Price', color='red', fontsize=14)


ax1.plot(df_btc_search.MONTH,df_btc_price.CLOSE, color="#FF7B00", linewidth=3, linestyle='--')
ax2.plot(df_btc_search.MONTH,df_btc_search.BTC_NEWS_SEARCH, color= 'steelblue', linewidth=3, marker='o')

# Locators
years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_minor_locator(months)
plt.tight_layout()

# UE 👇
plt.figure(figsize=((14,8)), dpi=100)
plt.xlabel("Years")

plt.xticks(rotation=45, fontsize=12)
plt.title('Monthly US "unemployment Benefits" Web search vs UNRATE incl 2020')
plt.grid()

ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.set_xlim(pd.Timestamp('2004-01-01'), pd.Timestamp('2020-08-01'))

ax1.set_ylabel('Search Trend', color= 'blue', fontsize=14)
ax2.set_ylabel('FRED U/E Rate', color='red', fontsize=14)
#ax1.set_xlim(0,15)


ax1.plot(df_ue_2020.MONTH,df_ue_2020.UNRATE, color="#250A86", linewidth=3)
ax2.plot(df_ue_2020.MONTH,df_ue_2020.UE_BENEFITS_WEB_SEARCH, color= 'steelblue', linewidth=3)

# Locators
years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_minor_locator(months)
plt.tight_layout()

plt.show()
