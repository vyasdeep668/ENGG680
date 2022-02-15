import pandas as pd
import json

DATA_CSV_PATH = "C:/Users/vyasd/Desktop/ENGG680/Assignments/Assignment_3/data.csv"
df = pd.read_csv(DATA_CSV_PATH, na_values='?')
#print(df.shape)
# df = df.replace('?', '-1')
# df['chol'] = df['chol'].astype(int)
# print(df['chol'].mean())
# Report1: what is the average age of patients?
#print(df['age'].mean())
# Report2: report the average chol level of people in intervals of 10 years old ([20,30],[30,40],[40,50],[50,60])
#df = df.drop(df[df['chol'] == '?'].index)
#df['chol'] = df['chol'].astype(int)
#print(df['chol'].mean())
# df['age'] = df['age'].astype(int)

# df['age_bin_index'] = df['age_bin'] = (df['age'] - df['age'].mod(10))
# # df['age_bin_index'] = df['age_bin']
# df_dict = dict(df.groupby(['age_bin_index'])[['age_bin', 'chol']].mean().values)
# df.__delitem__('age_bin_index')
# df.__delitem__('age_bin')
# print(df_dict)
# chol_min = df['chol'].min()
# chol_max = df['chol'].max()
# chol_30_low = chol_min + (chol_max - chol_min)*0.3
# chol_30_high = chol_max - (chol_max - chol_min)*0.3
# print(chol_30_low, chol_30_high)
#
# df['chol_bin_index'] = df['chol_bin'] = df['chol'].apply(lambda x: 0 if x < chol_30_low else (2 if x > chol_30_high else 1))
# df_dict = dict(df.groupby(['chol_bin_index'])[['chol_bin', 'trestbps']].mean().values)
# df.__delitem__('chol_bin_index')
# df.__delitem__('chol_bin')
# print(df_dict)

# Report4: report percentage of men and women with a positive diagnosis of heart disease(num=1).

#print(df[df["age"] >= 30][df[df["age"] >= 30]["age"] < 40]['chol'].mean())
# sub_df_all = df[df["num"] == 1]
# sub_df_all_count = sub_df_all['num'].count()
# sub_df_male = sub_df_all[sub_df_all["gender"] == 1]
# sub_df_female = sub_df_all[sub_df_all["gender"] == 0]
# print(sub_df_male['gender'].count()/sub_df_all_count*100) #sub_df_all['num'].count())

quotes_jason_pth = 'C:/Users/vyasd/Desktop/ENGG680/Assignments/Assignment_3/quotes-100-en.json'
quotes_jason_file = open(quotes_jason_pth, "rt", encoding='utf-8')
quotes_jason_dict = json.load(quotes_jason_file)
print(type(quotes_jason_dict))
name = "\"Weird Al\" Yankovic"
quote = "Alanis Morissette and I actually used to date. I especially liked it when we went to the movies."
if name in quotes_jason_dict.keys():
    if quote in quotes_jason_dict[name]:
        print(name, ':', quote)


# def search_quotes(name, quotes):
#     """
#         TODO:
#         2- Write a function search_quotes that takes a string as argument,
#            searches the keys in the quotes dictionary for items containing
#            the search string and prints the matching name (key) and quotes.
#     """
#     if name in quotes_jason_dict.keys()








