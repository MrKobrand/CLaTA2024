from typing import List, Dict


class PatentModel:
    def __init__(self) -> None:
        self.__patent_id = ''
        self.__title = ''
        self.__url = ''
        self.__abstract = ''
        self.__description = ''
        self.__claims = ''
        self.__problems = []

    @property
    def patent_id(self) -> str:
        """
        Получает уникальный идентификатор.
        :return: Уникальный идентификатор в строковом представлении.
        """
        return self.__patent_id

    @patent_id.setter
    def patent_id(self, patent_id: str) -> None:
        """
        Устанавливает уникальный идентификатор.
        :param patent_id: Уникальный идентификатор патента.
        """
        self.__patent_id = patent_id

    @property
    def title(self) -> str:
        """
        Получить заголовок.
        :return: Заголовок.
        """
        return self.__title

    @title.setter
    def title(self, title: str) -> None:
        """
        Устанавливает заголовок.
        :param title: Заголовок.
        """
        self.__title = title

    @property
    def url(self) -> str:
        """
        Получает URL.
        :return: URL-ссылка.
        """
        return self.__url

    @url.setter
    def url(self, url: str) -> None:
        """
        Устанавливает URL.
        :param url: URL-ссылка.
        """
        self.__url = url

    @property
    def abstract(self) -> str:
        """
        Получает аннотацию.
        :return: Текст аннотации.
        """
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: str) -> None:
        """
        Устанавливает аннотацию.
        :param abstract: Текст аннотации.
        """
        self.__abstract = abstract

    @property
    def description(self) -> str:
        """
        Получает описание.
        :return: Текст описания.
        """
        return self.__description

    @description.setter
    def description(self, description: str) -> None:
        """
        Устнанавливает описание.
        :param description: Текст описания.
        """
        self.__description = description

    @property
    def claims(self) -> str:
        """
        Получает формулы изобретения.
        :return: Текст формул изобретения.
        """
        return self.__claims

    @claims.setter
    def claims(self, claims: str) -> None:
        """
        Устанавливает формулы изобретения.
        :param claims: Текст формул изобретения.
        """
        self.__claims = claims

    @property
    def problems(self) -> List[Dict[str, str]]:
        """
        Получает список решаемых проблем.
        :return: Список решаемых проблем.
        """
        return self.__problems

    @problems.setter
    def problems(self, problems: List[Dict[str, str]]) -> None:
        """
        Устанавливает список решаемых проблем.
        :param problems: Список решаемых проблем.
        """
        self.__problems = problems
