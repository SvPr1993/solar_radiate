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
    solar_activity = data['flares_second'][0]
    solar_data_entity_obj = SolarDataEntity()
    activity_str = solar_data_entity_obj.activity_str(solar_activity)

    # Преобразуем в DTO
    return OutDTO(
        has_data=data['has_data'],
        date=data['date'],
        flares_count_second=data['flares_count_second'],
        flares_second=data['flares_second'],
        status=activity_str,
    )

#Прокинуть данные по status во view и во фронт
#Сделать схему микросервиса, он должен принимать int, а в ответ он будет отдавать разрешается ли курьеру поднимать на этаж выше 3, если нет лифта
#На вход нужно принять описание товара, принимать этаж, куда нужно доставить, значение есть лифт или нет, и вес товара
#Пороговое значение нужно получать из базы данных (любая база данных)
#Сервис должен дать ответ можно ли поднять товар на этаж клиента
#Расписать слои микросервиса, которые здесь будут, расписать dto (input, output)
#Расписать entity и методом написать бизнес логику
