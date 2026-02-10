from app_solar_radiate.repo import SolarActivityRepo
from app_solar_radiate.interfaces import ISolarActivityRepo


class SolarActivityRepoFactory:
    @staticmethod
    def create() -> ISolarActivityRepo:
        """
        Создает и возвращает экземпляр репозитория

        Returns:
            ISolarActivityRepo: Экземпляр репозитория
        """
        return SolarActivityRepo()