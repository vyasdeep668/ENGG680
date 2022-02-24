# Course: ENGG 680 Intro to Digital Engineering
# Midterm Project
# File: webscrap.py
# Group Members: Deep Vyas, Aditya Porwal, Sparsh Mehta, Anand Kulkarni, Dipesh Puri

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import time

MAX_RETRIES = 3
WAIT_SECONDS = 5


def get_faculty_data():
    """Returns panda dataframe of faculty information from website
    :param: None
    :type: None
    :rtype: panda dataframe object
    :return: panda dataframe of faculty information from website
    """
    url = "https://schulich.ucalgary.ca"
    faculty_url = url + "/electrical-computer/faculty-members"
    for count in range(MAX_RETRIES):
        try:
            response = requests.get(faculty_url, timeout=20)
            response.raise_for_status()
        except requests.exceptions.RequestException as error:
            count = count + 1
            if count == MAX_RETRIES:
                print("Check Internet Connection!!")
                raise SystemExit(error)
            else:
                print("Connecting...")
                time.sleep(WAIT_SECONDS)

    soup = BeautifulSoup(response.text, "html.parser")  # "lxml")
    database = []
    for prof_raw in soup.find("div", class_='row profiles').find_all('div', class_='text-chunk'):
        prof_raw = prof_raw.find_all('p')
        prof_url = url + prof_raw[0].a['href'].strip()
        prof_name = prof_raw[0].a.text.rsplit(' ', 1)
        prof_fname = prof_name[0].strip()
        prof_lname = prof_name[1].strip()
        position = prof_raw[1].text.replace('Department of Electrical and Software Engineering', '').strip()
        database.append([prof_fname, prof_lname, position, prof_url])

    return pd.DataFrame(database, columns=['firstname', 'lastname', 'title', 'homepage'])


def get_prof_data(prof_url):
    """Returns phone number and location of faculty from website
    :param: prof_url
    :type: string
    :rtype: tuple (phone_number, location)
    :return: phone number and location of faculty from website
    """
    # email_pattern = re.compile(r"\w+@\w+.ca")
    # location_pattern = re.compile(r'\w+ ?\d+\w?')
    # phonenumber_pattern = re.compile(r'\d{3}[.-]\d{3}[.-]\d{4}')
    phone_number = 'N/A'
    location = 'N/A'
    try:
        response = requests.get(prof_url, timeout=20)
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        raise SystemExit(error)
    soup = BeautifulSoup(response.text, "html.parser")  # "lxml")
    for prof_additional_info in soup.find("div", class_='col-md-8 contact-section').find_all('h4'):
        if prof_additional_info.text == 'Phone':
            phone_number = ''
            phone_number_list = prof_additional_info.parent.find_all('a')
            if len(phone_number_list) > 1:
                # prof have 2 contact numbers
                for prof_phone in phone_number_list:
                    phone_number = phone_number + prof_phone.text.strip() + ', '
                phone_number = phone_number[:-2]
            else:
                # prof have only 1 contact numbers
                phone_number = prof_additional_info.parent.a.text.strip()
        elif prof_additional_info.text == 'Location':
            location = prof_additional_info.parent.a.text.strip()

    # for prof_contact_info in soup.find("div", class_='col-md-8 contact-section').find_all('a'):
    #     if re.match(phonenumber_pattern, prof_contact_info.text):
    #         phone_number = prof_contact_info.text
    #     elif re.match(location_pattern, prof_contact_info.text):
    #         location = prof_contact_info.text

    return phone_number, location
