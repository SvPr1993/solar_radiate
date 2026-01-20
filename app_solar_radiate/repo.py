import json
import requests
from contextlib import contextmanager
from django.conf import settings


def get_solar_activity_repo(date_str):
    url = settings.API_SERVICE_URL
    flares_info = []

    try:
        response = requests.get(url, timeout=5)
        print(url)
        print(date_str)
        response.raise_for_status()
        data = response.json()

        if data:
            for index in data:
                index_data = {
                    'begin_time': data.get("start_number"),
                    'end_time': data.get("end_number"),
                }
                flares_info.append(index_data)

                return flares_info

    except requests.exceptions.RequestException as e:
        return flares_info




#def app_solar_data_save():
#    result = get_solar_activity
#    with open('result.json', 'w', encoding='utf-8') as f:
#        json.dump(result, f, ensure_ascii=False, indent=2)
#        print("Результаты сохранены!")