import json
import requests
from contextlib import contextmanager
from django.conf import settings


def get_solar_activity_repo(date_str):
    url = settings.API_SERVICE_URL
    flares_info = []

    try:
        response = requests.get(url, timeout=5)
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


def get_solar_activity_repo_second_api(date_str):
    url = settings.API_SERVICE_URL_2
    flares_info = {}

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        for key, value in data.items():
            r_data = value["R"]
            flares_info[key] = {
                "MinorProb": r_data.get("MinorProb"),
                "MajorProb": r_data.get("MajorProb")
            }
        return flares_info

    except requests.exceptions.RequestException as e:
        return flares_info


def get_solar_activity_data(date_str):
    data = api_service_1(date_str)
    if len(data) > 0:
        print("54 строка", type(data))
        return data, False
    data = api_service_2(date_str)
    if len(data) > 0:
        print("58 строка", type(data))
        return data, False
    else:
        print("61 строка", type(data))
        return data, True

#Сделать так, чтобы date_str использовалось в функциях.
#Нужно сделать чтобы в usecase возвращались в одном формате, привести данные к одному формату, определить этот тип данных и сделать
#Почитать про интерфесы
def api_service_1(date_str):
    url = settings.API_SERVICE_URL
    flares_info = []

    try:
        response = requests.get(url, timeout=5)
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


def api_service_2(date_str):
    url = settings.API_SERVICE_URL_2
    flares_info = {}

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        for key, value in data.items():
            r_data = value["R"]
            flares_info[key] = {
                "MinorProb": r_data.get("MinorProb"),
                "MajorProb": r_data.get("MajorProb")
            }
        return flares_info

    except requests.exceptions.RequestException as e:
        return flares_info
