import requests
from bs4 import BeautifulSoup

# def getPosition():
#     position = input("Enter Position(E.g. Software Developer) : ")
#     return position


def getDescription():
    description = input("Enter Job Descreption(E.g. Python) : ")
    description.replace(" ", "+")
    return description


def getLocation():
    location = input("Enter Job location you are looking for(E.g. Pune) : ")
    location.replace(" ", "+")
    return location


# url = "https://jobs.github.com/positions?utf8=✓&description=full+stack+developer&location=New+York"
url = "https://jobs.github.com/positions?utf8=✓&description=" + getDescription() + "&location="+getLocation()
req = requests.get(url)
scrap = BeautifulSoup(req.text, "html.parser")

for i in scrap.find_all("tr", class_="job"):
    print("\n\nPosition : " + i.td.h4.a.text)
    print("Description Link : " + i.td.h4.a.attrs['href'])
    print("Company Name : " + i.find("a", class_="company").text)
    print("Company URL : " + i.find("a", class_="company").attrs['href'])
    print("Job Type : "+i.find("strong").text)
    print("Location : " + i.find("span", class_="location").text, "\n\n")
