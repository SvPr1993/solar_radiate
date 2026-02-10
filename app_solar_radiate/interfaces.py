from abc import ABC, abstractmethod
from datetime import datetime


class ISolarActivityRepo(ABC):
    @abstractmethod
    def get_solar_activity_data(self, date_obj: datetime) -> dict:
        """
        Возвращает данные о солнечной активности для указанной даты

        Args:
            date_obj: Объект даты

        Returns:
            dict: Словарь с данными о солнечной активности
        """
        pass

    @abstractmethod
    def date_to_string(self, date_obj: datetime) -> str:
        """
        Преобразует объект даты в строку

        Args:
            date_obj: Объект даты

        Returns:
            str: Дата в строковом формате
        """
        pass