"""============================================================================
INFORMATION ABOUT CODE         Coding: ISO 9001:2015
===============================================================================
For Automating Longitude and Latitude parsing

Author: Prajinkya Pimpalghare

Date: 1-January-2018
Version: 1.0
Input Variable: GeoLocation[#01] URL
Basic Requirement Selenium module, and Web driver for chrome
============================================================================"""
from selenium import webdriver


class GeoLocationAutomation(object):
    """ For Automating Login in Citrix and opening its resources"""

    def __init__(self, url):
        """
        For Taking the basic elements required for accessing Citrix
        :param url:
        """
        self.url = url
        try:
            self.chrome_option = webdriver.ChromeOptions()
        except BaseException as error:
            print(" Chrome driver is not in path or selenium is not installed or both : ", error)
        self.latitude = None
        self.longitude = None

    def run_automation(self):
        """
        It actually runs and automate the whole process
        """
        try:
            browser = webdriver.Chrome(chrome_options=self.chrome_option)
            browser.get(self.url)
            self.latitude = browser.find_element_by_id("latitude").get_attribute("value")
            self.longitude = browser.find_element_by_id("longitude").get_attribute("value")
            while True:
                if self.latitude != browser.find_element_by_id("latitude").get_attribute(
                        "value") and self.longitude != browser.find_element_by_id("longitude").get_attribute("value"):
                    self.latitude = browser.find_element_by_id("latitude").get_attribute("value")
                    self.longitude = browser.find_element_by_id("longitude").get_attribute("value")
                    with open("GeoinformationContainer.txt", "a") as file:
                        file.write("Longitude = " + self.longitude + " Latitude = " + self.longitude + "\n")
        except BaseException as error:
            print("Please Check the Internet Connection :", error)


if __name__ == '__main__':
    URL = "https://www.gps-coordinates.net/"  # Add url
    TEMP = GeoLocationAutomation(url=URL)
    TEMP.run_automation()
