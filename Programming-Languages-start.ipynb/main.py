import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("QueryResults.csv")
df.columns = ['DATE', 'TAG', 'POSTS']
df['DATE'] = pd.to_datetime(df['DATE'])
#print(df.shape)
#print(df.count())
post_per_lang = df.groupby('TAG', as_index=False)['POSTS'].sum().sort_values(by='POSTS',ascending=False)

#print(post_per_lang.head(5))

#print(df.groupby('TAG').count())
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
reshaped_df.fillna(0, inplace=True)
print(reshaped_df.isna().values.any())
print(reshaped_df.head())


roll_df = reshaped_df.rolling(window=3).mean()

plt.figure(figsize=(16,10))
plt.title('Programming language Popularity Over Time', fontsize=16)
plt.grid(True)
plt.legend(['Java'], loc='upper right')

plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

""" plt.plot(reshaped_df['java'])
plt.plot(reshaped_df['python'])
plt.legend(['Java', 'Python'], loc='upper right') """

legend_list = []
for column in roll_df:
    plt.plot(roll_df[column])
    legend_list.append(column)

plt.legend(legend_list, loc='upper right')
    
plt.show()


# Practicing Pivot()
""" 

test_df = pd.DataFrame({'Age': ['Young', 'Young', 'Young', 'Young', 'Old', 'Old', 'Old', 'Old'],
                        'Actor': ['Jack', 'Arnold', 'Keanu', 'Sylvester', 'Jack', 'Arnold', 'Keanu', 'Sylvester'],
                        'Power': [100, 80, 25, 50, 99, 75, 5, 30]})

pivot_test_df = test_df.pivot(index='Age', columns='Actor', values='Power')
print(pivot_test_df)

games_df = pd.DataFrame({
    'Platform': ['PC', 'PC', 'PC', 'Console', 'Console', 'Console'],
    'Game': ['Halo', 'Zelda', 'Minecraft', 'Halo', 'Zelda', 'Minecraft'],
    'Rating': [85, 92, 95, 88, 90, 93]
})

pivot_games_df = games_df.pivot(index='Platform', columns='Game', values='Rating')
print(pivot_games_df) """
