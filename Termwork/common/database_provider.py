from abc import ABC, abstractmethod
from typing import List, Dict

from models.patent_model import PatentModel


class DatabaseProvider(ABC):
    def __init__(self, connection_string: str) -> None:
        """
        Инициализирует провайдер базы данных.
        :param connection_string: Строка подключения к БД.
        """
        self._connection_string = connection_string
        self._db_name = 'patent_problems_analysis'
        self._table_name = 'patent_problems'

    @abstractmethod
    def ensure_db_and_table_created(self) -> None:
        """
        Удостоверяет, что БД и таблица (коллекция и т.п.) созданы.
        """
        raise NotImplementedError

    @abstractmethod
    def check_if_patent_exists(self, patent_id: str) -> bool:
        """
        Проверяет, содержится ли патент в БД.
        :param patent_id: Уникальный идентификатор патента.
        :return: True, если содержится патент в БД, иначе - False.
        """
        raise NotImplementedError

    @abstractmethod
    def insert_patent(self, patent: PatentModel) -> None:
        """
        Добавляет патент в БД.
        :param patent: Патент.
        """
        raise NotImplementedError

    @abstractmethod
    def get_patents(self) -> List[PatentModel]:
        """
        Получает патенты из БД.
        :param patent: Список патентов.
        """
        raise NotImplementedError

    @abstractmethod
    def insert_problems(self, patent_id: str, problems: List[Dict[str, str]]) -> None:
        """
        Добавляет список решаемых проблем.
        :param patent_id: Уникальный идентификатор патента.
        :param problems: Список решаемых проблем.
        """
        raise NotImplementedError

    @abstractmethod
    def get_problems(self) -> List[Dict[str, str]]:
        """
        Возвращает список решаемых проблем.
        :param problems: Список решаемых проблем.
        """
        raise NotImplementedError
