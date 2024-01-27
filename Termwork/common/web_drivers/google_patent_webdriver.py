from common.patent_web_driver import PatentWebDriver


class GooglePatentWebDriver(PatentWebDriver):
    def __init__(self) -> None:
        super().__init__()

    def get_patent_html(self, patent_link: str) -> str:
        self._driver.get(patent_link)
        return self._driver.page_source
