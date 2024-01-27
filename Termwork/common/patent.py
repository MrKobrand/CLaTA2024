from common.patent_parser import PatentParser


class Patent:
    def __init__(self, patent_link: str, patent_parser: PatentParser) -> None:
        self.__patent_link = patent_link
        self.__patent_parser = patent_parser

        self.patent_link = self.__patent_link

    @property
    def patent_link(self) -> str:
        return self.__patent_link

    @patent_link.setter
    def patent_link(self, patent_link: str) -> None:
        self.__patent_link = patent_link
        self.__patent_parser.set_patent_link(patent_link)

    @property
    def patent_parser(self) -> PatentParser:
        return self.__patent_parser

    @patent_parser.setter
    def patent_parser(self, patent_parser: PatentParser) -> None:
        self.__patent_parser = patent_parser
        self.__patent_parser.set_patent_link(self.__patent_link)

    def get_id(self) -> str:
        """
        Получить уникальный идентификатор.
        :return: Уникальный идентификатор в строковом представлении.
        """
        return self.__patent_parser.get_id()

    def get_title(self) -> str:
        """
        Получить заголовок.
        :return: Заголовок.
        """
        return self.__patent_parser.get_title()

    def get_abstract(self) -> str:
        """
        Получить аннотацию.
        :return: Текст аннотации.
        """
        return self.__patent_parser.get_abstract()

    def get_description(self) -> str:
        """
        Получить описание.
        :return: Текст описания.
        """
        return self.__patent_parser.get_description()

    def get_claims(self) -> str:
        """
        Получить формулы изобретения.
        :return: Текст формул изобретения.
        """
        return self.__patent_parser.get_claims()
