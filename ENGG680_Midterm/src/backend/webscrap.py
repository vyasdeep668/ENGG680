# Course: ENGG 680 Intro to Digital Engineering
# Midterm Project
# File: webscrap.py
# Group Members: Deep Vyas, Aditya Porwal, Sparsh Mehta, Anand Kulkarni

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


def get_faculty_data():
    url = "https://schulich.ucalgary.ca"
    faculty_url = url + "/electrical-computer/faculty-members"
    response = requests.get(faculty_url)
    soup = BeautifulSoup(response.text, "html.parser")  # "lxml")
    database = []
    count = 1
    data = []
    for prof in soup.find("div", class_='row profiles').find_all('p'):
        if count == 3:
            database.append(data)
            data = []
            count = 1
        child_element = prof.findChild('a')
        if child_element is not None:
            full_name = child_element.text.rsplit(' ', 1)
            prof_url = url + child_element.get('href')
            data.insert(0, full_name[0].strip())
            data.insert(1, full_name[1].strip())
            data.insert(3, prof_url.strip())
        else:
            data.insert(2, prof.text.replace('Department of Electrical and Software Engineering', '').strip())
        count = count + 1

    return pd.DataFrame(database, columns=['firstname', 'lastname', 'title', 'homepage'])


def get_prof_data(prof_url):
    # email_pattern = re.compile("\w+@\w+.ca")
    location_pattern = re.compile("[A-Z][A-Z][A-Z].*[0-9]+")
    phonenumber_pattern = re.compile("[0-9][0-9][0-9].*[0-9][0-9][0-9].*[0-9][0-9][0-9][0-9]")
    phone_number = None
    location = None
    response = requests.get(prof_url)
    soup = BeautifulSoup(response.text, "html.parser")  # "lxml")
    for prof_contact_info in soup.find("div", class_='col-md-8 contact-section').find_all('a'):
        if len(re.findall(phonenumber_pattern, prof_contact_info.text)):
            phone_number = prof_contact_info.text
        elif len(re.findall(location_pattern, prof_contact_info.text)):
            location = prof_contact_info.text

    return phone_number, location
