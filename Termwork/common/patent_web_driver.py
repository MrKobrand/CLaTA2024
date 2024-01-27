from abc import ABC, abstractmethod

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class PatentWebDriver(ABC):
    def __init__(self) -> None:
        """
        Создать вебдрайвер для парсинга html-страниц.
        :param path_to_driver: Путь к файлу вебдрайвера.
        :return: Сконфигурированный вебдрайвер.
        """
        options = Options()
        options.add_argument('--headless=new')
        options.add_argument('--no-sandbox')
        self._driver = webdriver.Chrome(options=options)

    @abstractmethod
    def get_patent_html(self, patent_link: str) -> str:
        """
        Получить html-представление патента.
        :param patent_link: Ссылка на патент.
        :return: Строковая html-страница патента.
        """
        pass

    def quit(self):
        self._driver.quit()
