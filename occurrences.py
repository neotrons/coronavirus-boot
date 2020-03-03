class OccurrenceMap:
    def __init__(self, **kwargs):
        self.object_id = kwargs.get('OBJECTID')
        self.province_state = kwargs.get('Province_State')
        self.country_region = kwargs.get('Country_Region')
        self.last_update = kwargs.get('Last_Update')
        self.lat = float(kwargs.get('Lat') or 0)
        self.long = float(kwargs.get('Long_') or 0)
        self.confirmed = int(kwargs.get('Confirmed') or 0)
        self.deaths = int(kwargs.get('Deaths') or 0)
        self.recovered = int(kwargs.get('Recovered') or 0)
