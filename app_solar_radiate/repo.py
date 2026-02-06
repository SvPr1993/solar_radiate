import json
import requests
from django.conf import settings
from datetime import datetime

#Сделать так чтобы данные получались
#Сделать интерфейс между слоями usecase и repo с помощью нейросети
#

class SolarActivityRepo:
        def date_to_string(self, date_obj):
            return date_obj.strftime('%Y-%m-%d')

        def get_solar_activity_data(self, date_obj):
            date_str = self.date_to_string(date_obj)
            data = [] #self.api_service_1(date_obj)
            if len(data) > 0:
                print("54 строка", type(data))
                return data, False
            data = self.api_service_2(date_obj)
            if len(data) > 0:
                print("58 строка", type(data))
                return data, False
            else:
                print("61 строка", type(data))
                return data, True

        def api_service_2(self, date_obj):
            date_str = self.date_to_string(date_obj)
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

                json_flares_info = json.dumps(flares_info)
                return json_flares_info
            except requests.exceptions.RequestException as e:
                return flares_info

#def api_service_1(date_obj):
#    date_str = date_to_string(date_obj)
#    url = settings.API_SERVICE_URL
#    flares_info = []
#
#    try:
#        response = requests.get(url, timeout=5)
#        response.raise_for_status()
#        data = response.json()
#
#        if data:
#            for index in data:
#                index_data = {
#                    'begin_time': data.get("start_number"),
#                    'end_time': data.get("end_number"),
#                }
#                flares_info.append(index_data)
#                json_data = json.dumps(flares_info)
#
#                return json_data
#
#    except requests.exceptions.RequestException as e:
#        return flares_info





#def get_solar_activity_repo(date_obj):
#   date_str = date_to_string(date_obj)
#   url = settings.API_SERVICE_URL
#   flares_info = []

#   try:
#       response = requests.get(url, timeout=5)
#       response.raise_for_status()
#       data = response.json()

#       if data:
#           for index in data:
#               index_data = {
#                   'begin_time': data.get("start_number"),
#                   'end_time': data.get("end_number"),
#               }
#               flares_info.append(index_data)

#               return flares_info

#   except requests.exceptions.RequestException as e:
#        return flares_info


#def get_solar_activity_repo_second_api(date_obj):
#    date_str = date_to_string(date_obj)
#    url = settings.API_SERVICE_URL_2
#    flares_info = {}
#
#    try:
#        response = requests.get(url, timeout=5)
#        response.raise_for_status()
#        data = response.json()
#
#        for key, value in data.items():
#            r_data = value["R"]
#            flares_info[key] = {
#                "MinorProb": r_data.get("MinorProb"),
#                "MajorProb": r_data.get("MajorProb")
#            }
#       return flares_info

#   except requests.exceptions.RequestException as e:
#       return flares_info


