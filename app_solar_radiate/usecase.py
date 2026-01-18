import requests, json
from datetime import datetime, date
from django.conf import settings


def get_solar_activity(date_obj):
    date_str = date_obj.strftime('%Y-%m-%d')
    url = settings.URL

        #f'https://kauai.ccmc.gsfc.nasa.gov/DONKI/WS/get/CME?startDate={date_str}&endDate={date_str}'
#https://services.swpc.noaa.gov/products/noaa-scales.json

    try:
        response = requests.get(url, timeout=10)
        print(url)
        print(date_str)
        response.raise_for_status()
        data = response.json()

        if data:
            print(type(data))
            flares_info = []
            for index in data:
                print("CОЛНЕЧНАЯ АКТИВНОСТЬ ЧИСЛО", data[index])
                index_data = {
                    'begin_time': data.get("start_number"),
                    'end_time': data.get("end_number"),
                }
                flares_info.append(index_data)
                #+Нужно сделать так чтобы отображалось одно значание сегодняшнее, и найти рабочий рабочий API, если совсем нет, то написать самому имитацию API
            for key, value in data.items():
                print(key, value)

            return {
                'has_data': True,
                'date': date_str,
                'flares_count': len(data),
                'flares': flares_info,
                'message': f'Найдено {len(data)} солнечных вспышек'
            }
        else:
            return {
                'has_data': False,
                'date': date_str,
                'flares_count': 0,
                'message': 'В указанную дату солнечных вспышек не обнаружено'
            }

    except requests.exceptions.RequestException as e:
        return {
            'has_data': False,
            'date': date_str,
            'error': f'Ошибка при получении данных: {str(e)}',
            'message': 'Не удалось получить данные о солнечной активности'
        }