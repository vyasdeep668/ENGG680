import requests
from bs4 import BeautifulSoup
import time
from ENGG680_Midterm.src.backend.webscrap import *

# MAX_RETRIES = 3
# WAIT_SECONDS = 5
#
# prof_url = 'https://profiles.ucalgary.ca/jessica-bekker'
# response = requests.get(prof_url, timeout=20)
# soup = BeautifulSoup(response.text, "html.parser")  # "lxml")
# phone_number = 'N/A'
# location = 'N/A'
# df = get_faculty_data()
# df = df.drop(df.index[50]).reset_index(drop="True")
# # df = df.set_index('firstname').drop('Jessica')
# print(df)
# for prof_additional_info in soup.find("div", class_='row contact-container').find_all('h4'):
#     print(prof_additional_info.text)
#     if prof_additional_info.text == 'Phone number':
#         phone_number = prof_additional_info.parent.a.text.strip()
#     elif prof_additional_info.text == 'Location':
#         location = prof_additional_info.parent.a.text.strip()
#
# print(phone_number, location)






from matplotlib import pyplot as plt
import pandas as pd
import numpy as np


def plotlinechart(x_list, y_list1, y_list2, y_list3):
    plt.style.use('fivethirtyeight')
    plt.plot(x_list, y_list1, label='Mean', linestyle='--', color="#444444")
    plt.plot(x_list, y_list2, label='Max', color="#008fd5")
    plt.plot(x_list, y_list3, label='Min', color="#e5ae38")
    plt.xlabel('Age')
    plt.ylabel('Cholesterol Level')
    plt.title('Cholesterol Level by Age')
    plt.fill_between(x_list, y_list1, interpolate=True, alpha=0.20)
    plt.legend()
    plt.tight_layout()
    plt.show()


def plotbarchart(x_list, y_list1, y_list2, y_list3):
    plt.style.use('fivethirtyeight')
    x_indexes = np.arange(len(x_list))
    width = 0.25
    plt.bar(x_indexes-width, y_list1, label='Mean', linestyle='--', width=width, color="#444444")
    plt.bar(x_indexes, y_list2, label='Max', width=width, color="#008fd5")
    plt.bar(x_indexes+width, y_list3, label='Min', width=width, color="#e5ae38")
    plt.xlabel('Age', color="#008fd5")
    plt.ylabel('Cholesterol Level')
    plt.title('Cholesterol Level by Age')
    plt.xticks(ticks=x_indexes, labels=x_list)
    plt.legend()
    plt.tight_layout()
    plt.show()


def plothistogramchart(x_list, bins):
    plt.style.use('fivethirtyeight')
    plt.hist(x_list, bins=bins, edgecolor='black')
    plt.xlabel('Age', color="#008fd5")
    plt.ylabel('Number of People')
    plt.title('Age Histogram')
    # plt.legend()
    plt.tight_layout()
    plt.show()


df = pd.read_csv('Assignments/Assignment_3/data.csv', na_values="?")
res = []
age_list = df['age'].to_list()
[res.append(x) for x in age_list if x not in res]
chol_list = df.groupby(by=['age']).mean()['chol'].to_list()
chol_list_1 = df.groupby(by=['age']).max()['chol'].to_list()
chol_list_2 = df.groupby(by=['age']).min()['chol'].to_list()
#print(df)
#plotbarchart(res, chol_list, chol_list_1, chol_list_2)
plotlinechart(res, chol_list, chol_list_1, chol_list_2)
# age_bins = [10, 20, 30, 40, 50, 60, 70]
# plothistogramchart(age_list, age_bins)






