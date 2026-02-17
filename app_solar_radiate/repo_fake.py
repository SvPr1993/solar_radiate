from datetime import datetime
from typing import Dict, Any

class SolarActivityRepoFake:
    def date_to_string(self, date_obj: datetime) -> str:
        return date_obj.strftime('%Y-%m-%d')

    def get_solar_activity_data(self, date_obj: datetime) -> Dict[str, Any]:
        date_str = self.date_to_string(date_obj)
        flares_info_second: list = [1, "3974"]  # здесь могут быть реальные данные
        return {
            'has_data': True,
            'date': date_str,
            'flares_count_second': len(flares_info_second),
            'flares_second': flares_info_second,
            'message': f'Найдено {len(flares_info_second)} солнечных вспышек',
            'source': 'service_2'
        }