# Course: ENGG 680 Intro to Digital Engineering
# Assignment #: 3
# Topic: Pandas Health Report (4 pts)
# Name: Deep Vyas
# UCID: 30139014

import pandas as pd


# Your solution goes here - complete the code bellow


def main():
    df = pd.read_csv('data.csv', index_col=False, header=0, na_values="?")

    # report 1
    print("Report1\n \tthe average age of patients are: ", df['age'].mean())

    # report2
    print("\nReport2")
    for i in [20, 30, 40, 50, 60]:
        sub_df = df[df["age"] >= i]
        print("\tfor people with age in range of", i, i + 9, "average CHOL is: ", sub_df[sub_df["age"] < i+10]['chol'].mean())

    # report3
    chol_min = df['chol'].min()
    chol_max = df['chol'].max()
    chol_30_low = chol_min + (chol_max - chol_min)*0.3
    chol_30_high = chol_max - (chol_max - chol_min)*0.3
    print("\nReport3")
    print("\tfor patients with lowest 30% of chol, average trestbps is: ", df[df["chol"] < chol_30_low]['trestbps'].mean())
    print("\tfor patients with highest 30% of chol, average trestbps is: ", df[df["chol"] > chol_30_high]['trestbps'].mean())

    # report4
    sub_df_all = df[df["num"] == 1]
    sub_df_all_count = sub_df_all['num'].count()
    sub_df_male = sub_df_all[sub_df_all["gender"] == 1]
    sub_df_female = sub_df_all[sub_df_all["gender"] == 0]

    print("\nReport4")
    print("\t{0:.2f}% of patients diagnosed with heart decease are men and ".format(sub_df_male['gender'].count()/sub_df_all_count*100),
          "{0:.2f}% of them are women".format(sub_df_female['gender'].count()/sub_df_all_count*100))


if __name__ == "__main__":
    main()
