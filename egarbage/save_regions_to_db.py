from egarbage.regions import RwandaRegions
from .models import Province, District, Sector, Cell, Village

regions = RwandaRegions()

# Save all Province to db
provinces = regions.get_provinces()
for prov in provinces:
    province = Province(province=prov)
    province.save()
