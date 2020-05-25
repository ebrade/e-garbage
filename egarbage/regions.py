import json
import os
from django.conf import settings


class RwandaRegions:
    @staticmethod
    def get_all_regions():
        with open(os.path.join(settings.BASE_DIR, "egarbage/rwanda_regions.json"), "r") as f:
            all_regions = json.load(f)
        return all_regions

    def get_provinces(self):
        provinces = (self.get_all_regions()).keys()
        return provinces

    def get_all_districts(self):
        data = self.get_all_regions()
        districts = []
        for d, v in data.items():
            prov_dis = self.get_districts_from_province(d)
            districts.extend(prov_dis)
        districts.sort()
        return districts

    def get_districts_from_province(self, province):
        data = self.get_all_regions()
        districts = data[province]
        return list(districts.keys())

    def get_sectors_from_district(self, province, district):
        data = self.get_all_regions()
        sectors = data[province][district]
        return list(sectors.keys())

    def get_cells_from_sector(self, province, district, sector):
        data = self.get_all_regions()
        cells = data[province][district][sector]
        return list(cells.keys())

    def get_villages_from_cell(self, province, district, sector, cell):
        data = self.get_all_regions()
        villages = data[province][district][sector][cell]
        return villages
