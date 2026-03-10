import json
import requests
from django.conf import settings
from datetime import datetime
from app_solar_radiate.interfaces import ISolarActivityRepo


class SolarActivityRepo(ISolarActivityRepo):  # Добавил наследование от интерфейса
    def date_to_string(self, date_obj):
        return date_obj.strftime('%Y-%m-%d')

    def get_solar_activity_data(self, date_obj):
        date_str = self.date_to_string(date_obj)

        # Запрос к первому сервису
        flares_info = self.api_service_1(date_obj)
        if flares_info and len(flares_info) > 0:
            return {
                'has_data': True,
                'date': date_str,
                'flares_count_second': len(flares_info),
                'flares_second': flares_info,
                'message': f'Найдено {len(flares_info)} солнечных вспышек',
                'source': 'service_1'
            }

        # Запрос ко второму сервису
        flares_info_second = self.api_service_2(date_obj)
        if flares_info_second and len(flares_info_second) > 0:
            # Преобразуем словарь в список для единообразия
            flares_list = []
            for key, value in flares_info_second.items():
                flare_item = {'key': key, **value}
                flares_list.append(flare_item)

            return {
                'has_data': True,
                'date': date_str,
                'flares_count_second': len(flares_info_second),
                'flares_second': flares_list,
                'message': f'Найдено {len(flares_info_second)} солнечных вспышек (из альтернативного источника)',
                'source': 'service_2'
            }

        # Если оба сервиса не сработали
        return {
            'has_data': False,
            'date': date_str,
            'flares_count_second': 0,
            'flares_second': [],
            'message': 'Нет данных о солнечных вспышках за указанную дату'
        }

    def api_service_1(self, date_obj):
        date_str = self.date_to_string(date_obj)
        url = settings.API_SERVICE_URL
        flares_info = []

        try:
            # Добавляем дату в запрос, если API поддерживает параметры
            if '{date}' in url:
                url = url.format(date=date_str)

            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()

            if data:
                if isinstance(data, list):
                    for item in data:
                        item_data = {
                            'begin_time': item.get("start_number", ""),
                            'end_time': item.get("end_number", ""),
                        }
                        flares_info.append(item_data)

                elif isinstance(data, dict):
                    # Если это словарь с данными за дату
                    if date_str in data:
                        date_data = data[date_str]
                        if isinstance(date_data, list):
                            for item in date_data:
                                flares_info.append({
                                    'begin_time': item.get("start_number", ""),
                                    'end_time': item.get("end_number", ""),
                                })
                        else:
                            flares_info.append({
                                'begin_time': date_data.get("start_number", ""),
                                'end_time': date_data.get("end_number", ""),
                            })
                    else:
                        flares_info.append({
                            'begin_time': data.get("start_number", ""),
                            'end_time': data.get("end_number", ""),
                        })

            return flares_info

        except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
            print(f"Ошибка при запросе к API сервиса 1: {e}")
            return flares_info

    def api_service_2(self, date_obj):
        date_str = self.date_to_string(date_obj)
        url = settings.API_SERVICE_URL_2
        flares_info = {}

        try:
            # Добавляем дату в запрос, если API поддерживает параметры
            if '{date}' in url:
                url = url.format(date=date_str)

            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()

            if data and isinstance(data, dict):
                # Если данные приходят с ключом по дате
                if date_str in data:
                    date_data = data[date_str]
                    if isinstance(date_data, dict):
                        for key, value in date_data.items():
                            if isinstance(value, dict) and "R" in value:
                                r_data = value["R"]
                                flares_info[key] = {
                                    "MinorProb": r_data.get("MinorProb"),
                                    "MajorProb": r_data.get("MajorProb")
                                }
                else:
                    # Общая обработка всех данных
                    for key, value in data.items():
                        if isinstance(value, dict) and "R" in value:
                            r_data = value["R"]
                            flares_info[key] = {
                                "MinorProb": r_data.get("MinorProb"),
                                "MajorProb": r_data.get("MajorProb")
                            }

            return flares_info

        except (requests.exceptions.RequestException, json.JSONDecodeError, KeyError) as e:
            print(f"Ошибка при запросе к API сервиса 2: {e}")
            return flares_info



