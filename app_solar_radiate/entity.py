class SolarDataEntity:
    def activity_str(self, solar_activity_index):
        if solar_activity_index > 5:
            return "high"
        else:
            return "low"