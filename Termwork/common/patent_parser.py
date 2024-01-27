from abc import ABC, abstractmethod
from typing import List, Dict


class PatentParser(ABC):
    @abstractmethod
    def set_patent_link(self, patent_link: str) -> None:
        """
        Установить ссылку патента.
        :param patent_link: Ссылка на патент.
        """
        raise NotImplementedError

    @abstractmethod
    def get_id(self) -> str:
        """
        Получить уникальный идентификатор.
        :return: Уникальный идентификатор в строковом представлении.
        """
        raise NotImplementedError

    @abstractmethod
    def get_title(self) -> str:
        """
        Получить заголовок.
        :return: Заголовок.
        """
        raise NotImplementedError

    @abstractmethod
    def get_abstract(self) -> str:
        """
        Получить аннотацию.
        :return: Текст аннотации.
        """
        raise NotImplementedError

    @abstractmethod
    def get_description(self) -> str:
        """
        Получить описание.
        :return: Текст описания.
        """
        raise NotImplementedError

    @abstractmethod
    def get_claims(self) -> str:
        """
        Получить формулы изобретения.
        :return: Текст формул изобретения.
        """
        raise NotImplementedError
