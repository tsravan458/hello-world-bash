import pandas as pd
file_url = '/Users/sravantadepalli/Downloads/salaries.csv'
df = pd.read_csv(file_url)
# print(df)
# print("Hello, World!")
# count_twenty_four = len(df[df.Age == 36])
# count_twenty_four = df[df['Age'].between(20, 30)]
#Age = df[df.Age between  20 and 30]
filtered_df =df.query('Age >= 20 and Age < 30')
print(filtered_df['Name'])
Total = filtered_df['Salary'].tolist()


final = sum(map(float,Total))
#print(final)
#df['Salary'].sum()

