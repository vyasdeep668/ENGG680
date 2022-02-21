# Course: ENGG 680 Intro to Digital Engineering
# Midterm Project
# File: webscrap.py
# Group Members: Deep Vyas, Aditya Porwal, Sparsh Mehta, Anand Kulkarni

import concurrent.futures
import pandas as pd
from backend import webscrap
import time

MULTI_THREDING = True   # False


def main():
    print("Working...\nMultithreading: ", MULTI_THREDING)
    df = webscrap.get_faculty_data()
    prof_url_list = df['homepage'].to_list()
    prof_additional_info_list = []

    if MULTI_THREDING:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = executor.map(webscrap.get_prof_data, prof_url_list)
            for result in results:
                prof_additional_info_list.append([result[0], result[1]])
    else:
        for prof_url in prof_url_list:
            phone_number, location = webscrap.get_prof_data(prof_url)
            prof_additional_info_list.append([phone_number, location])

    df[['contact', 'location']] = pd.DataFrame(prof_additional_info_list)
    df.to_csv(path_or_buf='C:/Users/vyasd/Desktop/ENGG680/ENGG680_Midterm/data/uofc_prof.csv', index=True)

    title_list = ['Assistant Professor', 'Professor', 'Senior Instructor', 'Instructor', 'Associate Professor']
    for title in title_list:
        print(f'Number of {title}s:', df.loc[df["title"] == title]['firstname'].count())


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print('Total operation execution time with multithreading: {:.2f}'.format(end-start), 'seconds')
