import requests
from occurrences import OccurrenceMap


class Boot:
    payload = {
        'f': 'json',
        'where': 'Confirmed > 0',
        'returnGeometry': False,
        'spatialRel': 'esriSpatialRelIntersects',
        'outFields': '*',
        'orderByFields': 'Confirmed desc,Country_Region asc,Province_State asc',
        'outSR': '102100',
        'resultOffset': 0,
        'resultRecordCount': 500,
        'cacheHint': True,
    }

    def get_user_agent(self):
        return "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) " \
               "Chrome/79.0.3945.130 Safari/537.36"

    def get_referer(self):
        return self.settings.referer_url

    def __init__(self, settings_class):
        self.settings = settings_class()
        self.url = '{}{}'.format(self.settings.origin_url,
                                 '0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases/FeatureServer/1/query'
                                 )
        self.headers = {
            'User-Agent': self.get_user_agent(),
            'Referer': self.settings.referer_url
        }

    def get_data(self):
        r = requests.get(self.url, params=self.payload, headers=self.headers)
        if r.status_code == 200:
            data = r.json()
            if isinstance(data, dict):
                return data.get('features', [])
        return []

    def map(self):
        features = self.get_data()
        datos = []
        for feature in features:
            occurrence = OccurrenceMap(**feature.get('attributes'))
            datos.append(occurrence.__dict__)
        return datos

    def run(self):
        return self.map()
