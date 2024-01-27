from typing import List, Dict

from common.database_provider import DatabaseProvider
from models.patent_model import PatentModel


class Database:
    def __init__(self, database_provider: DatabaseProvider) -> None:
        self.__database_provider = database_provider

    @property
    def database_provider(self) -> DatabaseProvider:
        return self.__database_provider

    @database_provider.setter
    def database_provider(self, database_provider: DatabaseProvider) -> None:
        self.__database_provider = database_provider

    def ensure_db_and_table_created(self) -> None:
        """
        Удостоверяет, что БД и таблица созданы.
        """
        self.__database_provider.ensure_db_and_table_created()

    def check_if_patent_exists(self, patent_id: str) -> bool:
        """
        Проверяет, содержится ли патент в БД.
        :param patent_id: Уникальный идентификатор патента.
        :return: True, если содержится патент в БД, иначе - False.
        """
        return self.__database_provider.check_if_patent_exists(patent_id)

    def insert_patent(self, patent: PatentModel) -> None:
        """
        Добавляет патент в БД.
        :param patent: Патент.
        """
        self.__database_provider.insert_patent(patent)

    def get_patents(self) -> List[PatentModel]:
        """
        Получает патенты из БД.
        :param patent: Список патентов.
        """
        return self.__database_provider.get_patents()

    def insert_problems(self, patent_id: str, problems: List[Dict[str, str]]) -> None:
        """
        Добавляет список решаемых проблем.
        :param patent_id: Уникальный идентификатор патента.
        :param problems: Список решаемых проблем.
        """
        self.__database_provider.insert_problems(patent_id, problems)

    def get_problems(self) -> List[Dict[str, str]]:
        """
        Возвращает список решаемых проблем.
        :param problems: Список решаемых проблем.
        """
        return self.__database_provider.get_problems()
