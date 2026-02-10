class SolarActivityRepoFake:
    def date_to_string(self, date_obj):
        return date_obj.strftime('%Y-%m-%d')

    def get_solar_activity_data(self, date_obj):
        date_str = self.date_to_string(date_obj)
        flares_info = []

        return {
                'has_data': True,
                'date': date_str,
                'flares_count': len(flares_info),
                'flares': flares_info,
                'message': f'Найдено {len(flares_info)} солнечных вспышек',
                'source': 'service_1'
            }