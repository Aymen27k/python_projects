import pandas as pd


df = pd.read_csv('./data/salaries-by-college-major.csv')
""" print(df.head)
print(df.shape)
print(df.columns)
print(df.isna().sum()) """

clean_df = df.dropna()
""" print(clean_df.tail())
print(clean_df['Starting Median Salary'].idxmax())
print(clean_df['Undergraduate Major'].loc[43])
print(clean_df.loc[43]) """

# Challenge 1
""" print(f"Highest mid-career  => {clean_df['Mid-Career Median Salary'].max()}")
print(f"Highest mid-career ID: => {clean_df['Mid-Career Median Salary'].idxmax()}")
print(f"Job with highest mid-Career salary : => {clean_df['Undergraduate Major'].loc[8]}")
print(f"Lowest Start-career {clean_df['Starting Median Salary'].min()}" )
print(f"Lowest Start-career ID : {clean_df['Starting Median Salary'].idxmin()}" )
print(f"Job with highest mid-Career salary : => {clean_df['Undergraduate Major'].loc[49]}")
print(f"Lowest mid-career {clean_df['Mid-Career Median Salary'].min()}" )
print(f"Lowest mid-career ID :  {clean_df['Mid-Career Median Salary'].idxmin()}" )
print(f"Job with highest mid-Career salary : => {clean_df['Undergraduate Major'].loc[18]}") """

""" spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)
print(clean_df.head())
low_risk = clean_df.sort_values('Spread')
print(f"Lowest risk Spread => {low_risk[['Undergraduate Major','Spread']].head()}") """

# Challenge 2
""" highest_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
print(f"Degrees with the highest potential : {highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head()}")

spread_salary = clean_df.sort_values('Mid-Career Median Salary', ascending=False)
print(spread_salary[['Undergraduate Major','Mid-Career Median Salary']].head(5)) """


pd.options.display.float_format = '{:,.2f}'.format

print(clean_df.groupby('Group').count())
print(clean_df.groupby('Group').mean(numeric_only=True))
