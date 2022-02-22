# Course: ENGG 680 Intro to Digital Engineering
# Midterm Project
# File: main.py
# Group Members: Deep Vyas, Aditya Porwal, Sparsh Mehta, Anand Kulkarni, Dipesh Puri

import concurrent.futures
import pandas as pd
from backend import webscrap
import time
from tqdm import tqdm

MULTI_THREDING = True   # True/False


def main():
    font_color = '\033[92m' if MULTI_THREDING else '\033[91m'
    print('\033[1m' + font_color + "Multithreading: " + str(MULTI_THREDING) + '\033[0m' + '\nFetching Data...')
    df = webscrap.get_faculty_data()
    prof_url_list = df['homepage'].to_list()
    prof_additional_info_list = []

    if MULTI_THREDING:

        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = list(tqdm(executor.map(webscrap.get_prof_data, prof_url_list), total=len(prof_url_list)))
            for result in results:
                prof_additional_info_list.append([result[0], result[1]])
    else:
        for prof_url in tqdm(prof_url_list):
            phone_number, location = webscrap.get_prof_data(prof_url)
            prof_additional_info_list.append([phone_number, location])

    df[['contact', 'location']] = pd.DataFrame(prof_additional_info_list)
    df.to_csv(path_or_buf='../data/uofc_prof.csv', index=True)

    title_list = ['Assistant Professor', 'Professor', 'Senior Instructor', 'Instructor', 'Associate Professor']
    for title in title_list:
        print(f'Number of {title}s:', df.loc[df["title"] == title]['firstname'].count())


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    if MULTI_THREDING:
        print('Total operation execution time with multithreading: {:.2f}'.format(end-start), 'seconds')
    else:
        print('Total operation execution time without multithreading: {:.2f}'.format(end - start), 'seconds')
