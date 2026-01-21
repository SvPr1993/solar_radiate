from datetime import datetime, date
from django.conf import settings
from app_solar_radiate.repo import get_solar_activity_repo


def get_solar_activity_usecase(date_obj):
    date_str = date_obj.strftime('%Y-%m-%d')
    flares_info = get_solar_activity_repo(date_str)
    url = settings.API_SERVICE_URL_2
    if len(flares_info) > 0:
        return {
            'has_data': True,
            'date': date_str,
            'flares_count': len(flares_info),
            'flares': flares_info,
            'message': f'Найдено {len(flares_info)} солнечных вспышек'
        }
    else:
        return url
#Добавить второй API с солнечными вспушками в блок else
#Если сработал блок else, то нужно добавить сюда другой репизоторой со второй API, можно в одном файле repo, если слишком много, то можно создать другой файл
#Сделать случай если сервис вообще не работает, сделать ошибку, условно не получилось получить данный.

#f'https://kauai.ccmc.gsfc.nasa.gov/DONKI/WS/get/CME?startDate={date_str}&endDate={date_str}'
#https://services.swpc.noaa.gov/products/noaa-scales.json

