from typing import List, Dict

from bs4 import BeautifulSoup

from common.web_drivers.google_patent_webdriver import GooglePatentWebDriver
from common.patent_parser import PatentParser


class GooglePatentParser(PatentParser):
    def __init__(self, google_patent_web_driver: GooglePatentWebDriver) -> None:
        self.__soup: BeautifulSoup = None
        self.__google_patent_web_driver = google_patent_web_driver

    def set_patent_link(self, patent_link: str) -> None:
        page = self.__google_patent_web_driver.get_patent_html(patent_link)
        self.__soup = BeautifulSoup(page, 'html.parser')

    def get_id(self) -> str:
        return self.__soup.find(id='pubnum').text

    def get_title(self) -> str:
        return self.__soup.find('h1', {'id': 'title'}).text.strip()

    def get_abstract(self) -> str:
        return self.__soup.find('patent-text', {'name': 'abstract'}).text.strip()

    def get_description(self) -> str:
        return self.__soup.find('patent-text', {'name': 'description'}).text.strip()

    def get_claims(self) -> str:
        return self.__soup.find('patent-text', {'name': 'claims'}).text.strip()
