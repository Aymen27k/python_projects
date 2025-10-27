import pandas as pd
import plotly.express as px

os_df = pd.read_csv('./data/os_combined-TN-monthly-202409-202509.csv')
os_df['Date'] = pd.to_datetime(os_df['Date'])
os_df['Apple Desktop'] = os_df['OS X'] + os_df['macOS']
os_df.drop(columns=['OS X', 'macOS', 'Other'], inplace=True)
id_columns = ['Date']
value_columns = ['Windows', 'Linux', 'Chrome OS', 'Apple Desktop']
os_df_long = pd.melt(os_df, id_vars=id_columns, value_vars=value_columns, var_name='OS Name', value_name='Usage percentage')

# Calculating the monthly changes
os_df_long['Previous Usage'] = os_df_long.groupby('OS Name')['Usage percentage'].shift(1)
os_df_long['Monthly Change'] = os_df_long['Usage percentage'] - os_df_long['Previous Usage']

os_df_long.drop(columns=['Previous Usage'], inplace=True)
df_plot = os_df_long.dropna(subset=['Monthly Change'])

 
""" print(os_df.shape)
print(os_df.head()) """
print("--- Melted Data Preview ---")
# Display the first few rows to show the stacked structure
print(os_df_long.head(10))
print(f"\nDataFrame shape after melt: {os_df_long.shape}")

#fig = px.line(os_df_long, x='Date', y='Usage percentage', title='OS Market share in Tunisia', color='OS Name')
fig = px.line(df_plot, x='Date', y='Monthly Change', title='Monthly evolution for Each OS', color='OS Name')
fig.update_traces(mode='lines+markers', line_shape='spline')
fig.update_layout(title_font_size=24, xaxis=dict(title_font_size=18, tickfont_size=14), yaxis=dict(title_font_size=18, tickfont_size=14))


fig.show()