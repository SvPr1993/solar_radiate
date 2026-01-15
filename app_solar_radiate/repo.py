import json
import requests
from contextlib import contextmanager
from app_solar_radiate.usecase import get_solar_activity

def app_solar_data_save():
    result = get_solar_activity
    with open('result.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
        print("Результаты сохранены!")