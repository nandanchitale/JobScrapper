import requests
from bs4 import BeautifulSoup

# Method to get job description


def getDescription():
    description = input("Enter Job Descreption(E.g. Python) : ")
    description.replace(" ", "+")
    return description

# Method to get job location


def getLocation():
    location = input(
        "Enter Job location you are looking for(E.g. Pune) : ")
    location.replace(" ", "+")
    return location


class LinkedInScrapper:
    def generateUrl(description, location):

        # Create URL
        url = "https://www.linkedin.com/search/results/all/?keywords=" + description + "%20" + location + "&origin=GLOBAL_SEARCH_HEADER"
        req = requests.get(url)
        data = {
            "req": req,
            "url": url,
        }
        return data

    def scraper(self):

        description = getDescription()
        location = getLocation()

        data = self.generateUrl(self, description, location)

        req = data['request']

        scrap = BeautifulSoup(req.text, "html.parser")

        for i in scrap.find_all("tr", class_="job"):
            print("\n\nPosition : " + i.td.h4.a.text)
            print("Description Link : " + i.td.h4.a.attrs['href'])
            print("Company Name : " + i.find("a", class_="company").text)
            print("Company URL : " + i.find("a",
                                            class_="company").attrs['href'])
            print("Job Type : "+i.find("strong").text)
            print("Location : " + i.find("span", class_="location").text, "\n\n")


class GitJobScrapper:

    def generateUrl(description, location):

        # Create URL
        url = "https://jobs.github.com/positions?utf8=✓&description=" + \
            description + "&location="+location
        req = requests.get(url)
        data = {
            "req": req,
            "url": url,
        }
        return data

    def scraper(self):

        description = getDescription()
        location = getLocation()

        data = self.generateUrl(self, description, location)

        req = data['request']

        scrap = BeautifulSoup(req.text, "html.parser")

        for i in scrap.find_all("ul", class_="jobs-search-results__list"):
            print("\n\nPosition : " + i.td.h4.a.text)
            print("Description Link : " + i.td.h4.a.attrs['href'])
            print("Company Name : " + i.find("a", class_="company").text)
            print("Company URL : " + i.find("a",
                                            class_="company").attrs['href'])
            print("Job Type : "+i.find("strong").text)
            print("Location : " + i.find("span", class_="location").text, "\n\n")


def main():
    