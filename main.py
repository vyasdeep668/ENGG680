import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


def main():
    print("web...")
    url = "https://schulich.ucalgary.ca"
    faculty_url = url + "/electrical-computer/faculty-members"

    response = requests.get(faculty_url)
    soup = BeautifulSoup(response.text,"html.parser") # "lxml")
    database = []
    count = 1
    data = []
    for prof in soup.find("div", class_='row profiles').find_all('p'):
        if count == 3:
            print(data)
            database.append(data)
            data = []
            count = 1
        child_element = prof.findChild('a')
        if child_element is not None:
            full_name = child_element.text.rsplit(' ', 1)
            prof_url = url + child_element.get('href')
            phone_number, location = get_info(prof_url)
            data.insert(0, full_name[0].strip())
            data.insert(1, full_name[1].strip())
            data.insert(3, prof_url.strip())
            data.insert(4, phone_number)
            data.insert(5, location)
        else:
            data.insert(2, prof.text.replace('Department of Electrical and Software Engineering', '').strip())
        count = count + 1
    df = pd.DataFrame(database, columns=['firstname', 'lastname', 'title', 'homepage', 'contact', 'location'])
    print(df)
    df.to_csv(path_or_buf='C:/Users/vyasd/Desktop/ENGG680/ENGG680_Midterm/data/uofc_prof.csv', index=True)


    #Stage4: Generating Report
    df = pd.read_csv(filepath_or_buffer='C:/Users/vyasd/Desktop/ENGG680/ENGG680_Midterm/data/uofc_prof.csv')
    print(df)
    print('Number of Assistant Professors:', df.loc[df["title"] == 'Assistant Professor']['firstname'].count())
    print('Number of Professors:', df.loc[df["title"] == 'Professor']['firstname'].count())
    print('Number of Senior Instructors:', df.loc[df["title"] == 'Senior Instructor']['firstname'].count())
    print('Number of Instructors:', df.loc[df["title"] == 'Instructor']['firstname'].count())
    print('Number of Associate Professors:', df.loc[df["title"] == 'Associate Professor']['firstname'].count())


def get_info(prof_url):
    email_pattern = re.compile("\w+@\w+.ca")
    Location_pattern = re.compile("[A-Z][A-Z][A-Z].*[0-9]+")
    PhoneNumber_Pattern = re.compile("[0-9][0-9][0-9].*[0-9][0-9][0-9].*[0-9][0-9][0-9][0-9]")
    phone_number = None
    location = None
    try:
        response = requests.get(prof_url)
        soup = BeautifulSoup(response.text, "html.parser")  # "lxml")
        for prof_contact_info in soup.find("div", class_='col-md-8 contact-section').find_all('a'):
            if len(re.findall(PhoneNumber_Pattern, prof_contact_info.text)):
                phone_number = prof_contact_info.text
            elif len(re.findall(Location_pattern, prof_contact_info.text)):
                location = prof_contact_info.text
    except:
        phone_number = None
        location = None

    return phone_number, location

if __name__ == "__main__":
    main()

    import concurrent.futures
    import threading
    import time

    start = time.perf_counter()


    def do_something(seconds):
        print(f'Sleeping {seconds} second(s)...')
        time.sleep(seconds)
        first_name = "Deep"
        last_name = "Vyas"
        return first_name, last_name


    with concurrent.futures.ThreadPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(do_something, secs)
        for result in results:
            print(result[0])
        # results = [executor.submit(do_something, sec) for sec in secs]
        # for f in concurrent.futures.as_completed(results):
        #    print(f.result())

    finish = time.perf_counter()
    print(finish - start)