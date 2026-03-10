from datetime import datetime, date
from typing import Union, Protocol, Dict, Any
from app_solar_radiate.dto import OutDTO
from app_solar_radiate.entity import SolarDataEntity


class SolarActivityI(Protocol):
    def get_solar_activity_data(self, date_obj: datetime) -> Dict[str, Any]:
        """Возвращает словарь с данными о солнечной активности."""
        ...


def get_solar_activity_usecase(
        date_input: Union[date, datetime],
        repo: SolarActivityI
) -> OutDTO:
    # Преобразуем date в datetime, если нужно
    if isinstance(date_input, date):
        date_obj = datetime.combine(date_input, datetime.min.time())
    elif isinstance(date_input, datetime):
        date_obj = date_input
    else:
        raise ValueError("date_input должен быть объектом date или datetime")

    data = repo.get_solar_activity_data(date_obj)  # получаем словарь

    # Определяем активность на основе количества вспышек
    flares_count = data.get('flares_count_second', 0)
    solar_data_entity_obj = SolarDataEntity()
    activity_str = solar_data_entity_obj.activity_str(flares_count)

    # Преобразуем в DTO
    return OutDTO(
        has_data=data.get('has_data', False),
        date=data.get('date', ''),
        flares_count_second=flares_count,
        flares_second=data.get('flares_second', []),
        status=activity_str,
        message=data.get('message', '')
    )
