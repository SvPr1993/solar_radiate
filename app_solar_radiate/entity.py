class SolarDataEntity:
    def activity_str(self, solar_activity_index):
        """
        Определяет уровень солнечной активности на основе индекса/количества вспышек

        Args:
            solar_activity_index: количество вспышек или индекс активности

        Returns:
            str: 'high' если активность высокая, 'low' если низкая
        """
        if solar_activity_index > 5:
            return "high"
        else:
            return "low"