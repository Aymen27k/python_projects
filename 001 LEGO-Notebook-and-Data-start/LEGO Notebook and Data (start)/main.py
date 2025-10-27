import pandas as pd
import matplotlib.pyplot as plt

""" 
color_df = pd.read_csv("./LEGO Notebook and Data (start)/data/colors.csv")
unique_colors = color_df["name"].nunique()
print(f"LEGO has {unique_colors} unique colors in production.")
print(f"{color_df.groupby('is_trans').count()}")
print(f"{color_df.is_trans.value_counts()}") """

# In which year were the first LEGO sets released and what were these sets called?
sets = pd.read_csv("./LEGO Notebook and Data (start)/data/sets.csv")
themes = pd.read_csv("./LEGO Notebook and Data (start)/data/themes.csv")
games = pd.read_csv("./LEGO Notebook and Data (start)/data/vgames.csv")
first_set = sets.sort_values('year', ascending=True)
#print(f"The first set release is {first_set[['name', 'year']].head(5)}")

""" # How many different products did the LEGO company sell in their first year of operation?
set_1949 = sets[sets['year'] == 1949]
unique_products = set_1949['name'].nunique()
print(f"LEGO released {unique_products} in 1949")

# What are the top 5 LEGO sets with the most number of parts? 
print(sets.sort_values('num_parts', ascending=False).head(5)) """

themes_by_year = sets.groupby('year').agg({'theme_id' : pd.Series.nunique})
#print(f"Themes per year : {themes_by_year.head(5)}")
clean_theme_by_year = themes_by_year.iloc[:len(themes_by_year)-2]



sets_by_year = sets.groupby("year").count()
#print(sets_by_year['set_num'].head())
clean_sets_by_year = sets_by_year.iloc[0:len(sets_by_year)-2]



""" plt.xlabel("Years")

plt.xticks(ticks=themes_by_year.index[::5], rotation=90)
plt.xlim(1949,2019)
ax1 = plt.gca()
ax2 = ax1.twinx()

ax2.set_ylabel('Number of Unique Themes', color = 'blue')
ax1.set_ylabel('Number of sets', color= 'green')
plt.tight_layout()
ax1.plot(clean_sets_by_year, color='green')
ax2.plot(clean_theme_by_year, color= 'blue')
plt.show() """

""" parts_per_year = sets.groupby('year')['num_parts'].mean()
print(parts_per_year.head(5))
plt.scatter(x=parts_per_year.index[:-2], y=parts_per_year.values[:-2])
plt.show() """


""" star_wars_id = [18,158,209,261,345]

star_wars = sets[sets['theme_id'].isin(star_wars_id)]
print(star_wars['theme_id'].value_counts()) """

""" set_theme_count = sets['theme_id'].value_counts()
set_theme_count[:5]
set_theme_count = pd.DataFrame({'id': set_theme_count.index, 'set_count': set_theme_count.values})
merged_df = pd.merge(set_theme_count, themes, on='id')
print(merged_df) """

""" plt.figure(figsize=(14,8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel('Nr of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)
plt.bar(merged_df.name[:10], merged_df.set_count[:10])

plt.show() """


# Practicing Data analysis
#  Challenge 1: Top Publishers by Global Sales

    #Group by Publisher, sum Global_Sales, and show the top 3.
publisher_sales = games.groupby("Publisher")['Global_Sales'].sum()
top_publishers = publisher_sales.sort_values(ascending=False).head(3)
#print(top_publishers)

# Challenge 2: Genre Popularity

   # Use .value_counts() on Genre to find the most common genre.

genre_games = games.value_counts("Genre")
#print(genre_games.sort_values(ascending=False))


#Challenge 3: Sales Over Time

    # Group by Year, sum Global_Sales, and plot a line chart.

games_by_year = games.groupby('Year')['Global_Sales'].sum()
print(games_by_year.head())
plt.title("Global Video Game Sales Over Time")
plt.xlabel("Year")
plt.xticks(rotation=45)
plt.grid(True)
plt.ylabel("Million of games sold")
plt.plot(games_by_year)
#plt.show()

# Bonus: Platform Dominance

   # Which platform has the highest average global sales per game?

games_per_platform = games.groupby("Platform")['Global_Sales'].mean()
print(games_per_platform.head())