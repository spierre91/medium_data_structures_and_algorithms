import pandas as pd 

df = pd.read_csv("r_dataisbeautiful_posts.csv")
print(df.head())

print("Length of data frame before row selection: ", len(df))
df = df.iloc[:500]
print("Length of data frame after row selection: ", len(df))


print("Length of data frame before filtering: ", len(df))
df = df.loc[df.num_comments >= 50]
print("Length of data frame after filtering: ", len(df))

print(set(df['num_comments']))

df.to_csv("new_file_r_dataisbeautiful_posts.csv")

new_df = pd.read_csv("new_file_r_dataisbeautiful_posts.csv")
print("Length of new data frame: ", len(new_df))
print("set of number of comments values: ")
print(set(new_df['num_comments']))