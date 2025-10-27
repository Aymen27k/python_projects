import pandas as pd
import plotly.express as px


df_apps = pd.read_csv('./apps.csv')
# Removing two unwanted columns
df_apps.drop(['Last_Updated', 'Android_Ver'], axis=1, inplace=True )
df_apps_clean = df_apps.dropna()
duplicated_rows = df_apps_clean[df_apps_clean.duplicated()]
df_apps_clean = df_apps_clean.drop_duplicates(subset=['App', 'Type', 'Price'])
ratings = df_apps_clean.Content_Rating.value_counts()
# Different prints
""" print(df_apps.sample(5))
print(df_apps.count())
print(df_apps.shape) """
""" print(df_apps.columns)
print(duplicated_rows.shape)
print(df_apps_clean[df_apps_clean.App == 'Instagram'])

print(df_apps_clean.sort_values('Rating', ascending=False).head(5))
print(df_apps_clean.sort_values('Size_MBs', ascending=False).head(2))
print(df_apps_clean.sort_values('Reviews', ascending=False).head(50))
print(ratings)
 """
# Working with Plotly
fig = px.pie(labels=ratings.index, values=ratings.values, title='Content Rating', names=ratings.index, hole=0.3)
fig.update_traces(textinfo='label+percent', pull=[0.05, 0, 0, 0, 0])
#fig.show()


# Turning Install from Object to int
df_apps_clean.Installs = df_apps_clean.Installs.astype(str).str.replace(',', "")
df_apps_clean.Installs = pd.to_numeric(df_apps_clean.Installs)
df_apps_clean[['App','Installs']].groupby('Installs').count()

# Turning Price from Object datatype to int
df_apps_clean.Price = df_apps_clean.Price.astype(str).str.replace('$', "", regex=False)
df_apps_clean.Price = df_apps_clean.Price.astype(str).str.replace('FREE', "0")
df_apps_clean.Price = df_apps_clean.Price.astype(str).str.replace('.', "")
df_apps_clean.Price = pd.to_numeric(df_apps_clean.Price)
df_apps_clean[['App','Price']].groupby('Price').count()
df_apps_clean = df_apps_clean[df_apps_clean['Price'] <= 250 ]
df_apps_clean['Revenue_Estimate'] = df_apps_clean['Price'].mul(df_apps_clean.Installs, fill_value=0)
#print(df_apps_clean.sort_values('Price', ascending=False).head(20))
#print(df_apps_clean['Installs'].dtype)
top_10_gross_revenue = df_apps_clean.sort_values('Revenue_Estimate', ascending=False)
#print(top_10_gross_revenue.head(10))
games_count = top_10_gross_revenue[top_10_gross_revenue['Genres'].str.contains('Games', case=False, na=False)]
#print(games_count.sort_values('Revenue_Estimate', ascending=False).head(10))

#print(f" Unique Categories : {df_apps_clean.Category.nunique()}")
top_10_category = df_apps_clean.Category.value_counts()[:10]

category_installs = df_apps_clean.groupby('Category').agg({'Installs' : pd.Series.sum})
category_installs.sort_values('Installs', ascending=False, inplace=True)
#print(category_installs)

summary_df = df_apps_clean.groupby('Category').agg(Number_of_apps=('App', 'count'),Total_Installs=('Installs', 'sum')).sort_values('Total_Installs', ascending=False)
#print(summary_df)
fig = px.scatter(data_frame=summary_df.reset_index(), x='Number_of_apps', y='Total_Installs', size='Number_of_apps', color='Total_Installs', title='Category Concentration')



#print(top_10_category)
bar = px.bar(x = top_10_category.index, y= top_10_category.values)
h_bar = px.bar(x=category_installs.Installs, y=category_installs.index, orientation='h')
h_bar.update_layout(
    title='Total Installs by Category',
    xaxis_title='Installs',
    yaxis_title='Category'
)


""" print(df_apps_clean.Genres.nunique())
stack = df_apps_clean.Genres.str.split(';', expand=True).stack()
print(f"We now have a single column with shape : {stack.shape}")
num_genres = stack.value_counts()
print(f"Number of genres {len(num_genres)}")

bar_genres = px.bar(x=num_genres.index[:15], y=num_genres.values[:15],color=num_genres.values[:15], color_continuous_scale='solar', title='Top Genres')
bar_genres.update_layout( xaxis_title='Genre', yaxis_title='Number of Apps', coloraxis_showscale=False)
#bar_genres = px.colors.sequential._swatches_continuous()
bar_genres.show() """
""" print(df_apps_clean.Type.value_counts())
df_free_vs_paid = df_apps_clean.groupby(['Category','Type'], as_index=False).agg({'App': pd.Series.count})
print(df_free_vs_paid.head())


fig = px.bar(df_free_vs_paid, x='Category', y='App',color='Type',barmode='group', title='Free vs Paid Apps by Category',color_discrete_map={
        'Free': 'blue',
        'Paid': 'red'
    })
fig.update_layout(xaxis_title='Category',
                    yaxis_title='Number of Apps',
                    xaxis={'categoryorder':'total descending'},
                    yaxis=dict(type='log')) """


""" fig = px.box(df_apps_clean, x='Type', y='Installs', title='How Many Downloads are Paid Apps Giving up?', points='all', notched=True, color='Type')
fig.update_layout(xaxis_title='Type', yaxis_title='Installs', yaxis=dict(type='log')) """

df_paid_apps = df_apps_clean[df_apps_clean['Type'] == 'Paid']
df_paid_apps_clean = df_apps_clean[df_apps_clean['Price'] > 0] 

""" fig = px.box(df_paid_apps, x='Category', y='Revenue_Estimate')
fig.update_layout(xaxis_title='Category', yaxis_title='Paid App Ballpark Revenue', yaxis=dict(type='log'), xaxis={'categoryorder': 'median descending'}, xaxis_tickangle= -45) """

fig = px.box(df_paid_apps, x='Category', y='Price', points='all', title='Price per Category',)
fig.update_layout(xaxis_title='Category', yaxis_title='Paid App Price (USD)', yaxis=dict(type='log'),  xaxis={'categoryorder': 'median descending'}, xaxis_tickangle= -45)
print(df_paid_apps.Price.head())
fig.show()
