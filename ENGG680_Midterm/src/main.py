# Course: ENGG 680 Intro to Digital Engineering
# Midterm Project
# File: webscrap.py
# Group Members: Deep Vyas, Aditya Porwal, Sparsh Mehta, Anand Kulkarni

import concurrent.futures
import pandas as pd
from backend import webscrap


def main():
    print("Working...")
    df = webscrap.get_faculty_data()
    prof_url_list = df['homepage'].to_list()
    prof_additional_info_list = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(webscrap.get_prof_data, prof_url_list)
        for result in results:
            prof_additional_info_list.append([result[0], result[1]])

    df[['contact', 'location']] = pd.DataFrame(prof_additional_info_list)
    df.to_csv(path_or_buf='C:/Users/vyasd/Desktop/ENGG680/ENGG680_Midterm/data/uofc_prof.csv', index=True)

    print('Number of Assistant Professors:', df.loc[df["title"] == 'Assistant Professor']['firstname'].count())
    print('Number of Professors:', df.loc[df["title"] == 'Professor']['firstname'].count())
    print('Number of Senior Instructors:', df.loc[df["title"] == 'Senior Instructor']['firstname'].count())
    print('Number of Instructors:', df.loc[df["title"] == 'Instructor']['firstname'].count())
    print('Number of Associate Professors:', df.loc[df["title"] == 'Associate Professor']['firstname'].count())


if __name__ == "__main__":
    main()
