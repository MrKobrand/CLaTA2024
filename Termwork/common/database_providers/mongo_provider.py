from typing import List, Dict

from pymongo import MongoClient

from common.database_provider import DatabaseProvider
from models.patent_model import PatentModel


class MongoProvider(DatabaseProvider):
    def __init__(self, connection_string: str) -> None:
        """
        Иницилизирует провайдер БД MongoDB.
        :param connection_string: Строка подключения к БД.
        """
        super().__init__(connection_string)
        self._client = MongoClient(self._connection_string)

    def ensure_db_and_table_created(self) -> None:
        """
        Удостоверяет, что БД и таблица созданы.
        """
        pass

    def check_if_patent_exists(self, patent_id: str) -> bool:
        """
        Проверяет, содержится ли патент в БД.
        :param patent_id: Уникальный идентификатор патента.
        :return: True, если содержится патент в БД, иначе - False.
        """
        return self._client[self._db_name][self._table_name].count_documents({'patent_id': patent_id}, limit=1) == 1

    def insert_patent(self, patent: PatentModel):
        """
        Добавляет патент в БД.
        :param patent: Патент.
        """
        self._client[self._db_name][self._table_name].insert_one({
            'patent_id': patent.patent_id,
            'title': patent.title,
            'url': patent.url,
            'abstract': patent.abstract,
            'description': patent.description,
            'cliams': patent.claims,
            'problems': patent.problems
        })

    def get_patents(self) -> List[PatentModel]:
        """
        Получает патенты из БД.
        :param patent: Список патентов.
        """
        patent_models = []

        for patent in self._client[self._db_name][self._table_name].find():
            patent_model = PatentModel()
            patent_model.patent_id = patent['patent_id']
            patent_model.title = patent['title']
            patent_model.url = patent['url']
            patent_model.abstract = patent['abstract']
            patent_model.description = patent['description']
            patent_model.claims = patent['claims']
            patent_model.problems = patent['problems']
            patent_models.append(patent_model)

        return patent_models

    def insert_problems(self, patent_id: str, problems: List[Dict[str, str]]) -> None:
        """
        Добавляет список решаемых проблем.
        :param patent_id: Уникальный идентификатор патента.
        :param problems: Список решаемых проблем.
        """
        self._client[self._db_name][self._table_name].update_one(
            {'patent_id': patent_id},
            {'$set': {'problems': problems}}
        )

    def get_problems(self) -> List[Dict[str, str]]:
        """
        Возвращает список решаемых проблем.
        :param problems: Список решаемых проблем.
        """
        problems = []
        patent_problems = self._client[self._db_name][self._table_name].find().project({
            'problems': 1
        })

        for patent_problem in patent_problems:
            problems.append(patent_problem['problems'])

        return problems

    def __del__(self) -> None:
        """
        Освобождает выделенные ресурсы.
        """
        self._client.close()
