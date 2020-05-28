import json

from egarbage.regions import RwandaRegions
from .models import Province, District, Sector, Cell, Village


def save_prov_dis_to_db():
    regions = RwandaRegions()

    # Save all Province to db
    provinces = regions.get_provinces()
    for prov in provinces:
        province = Province(province=prov)
        province.save()

        districts = regions.get_districts_from_province(prov)

        for dis in districts:
            district = District(province=province, district=dis)
            district.save()


def save_sectors():
    regions = RwandaRegions()
    dis_instances = District.objects.all()
    num = 0
    instances = []
    for dis_instance in dis_instances:
        prov = dis_instance.province.province
        dis = dis_instance.district
        all_sectors = regions.get_sectors_from_district(prov, dis)

        for sector in all_sectors:
            num = num + 1
            c = Sector(district=dis_instance, sector=sector)
            instances.append(c)

        if num == 1000:
            Sector.objects.bulk_create(instances)
            num = 0
    Sector.objects.bulk_create(instances)


def save_cells():
    regions = RwandaRegions()
    sector_instances = Sector.objects.all()
    num = 0
    instances = []
    for sect in sector_instances:
        prov = sect.district.province.province
        dis = sect.district.district
        sec = sect.sector
        all_cells = regions.get_cells_from_sector(prov, dis, sec)

        for cell in all_cells:
            num = num + 1
            c = Cell(sector=sect, cell=cell)
            instances.append(c)

        if num == 1000:
            Cell.objects.bulk_create(instances)
            num = 0
    Cell.objects.bulk_create(instances)


def save_villages():
    regions = RwandaRegions()
    cell_instances = Cell.objects.all()
    num = 0
    instances = []
    for cell_instance in cell_instances:
        prov = cell_instance.sector.district.province.province
        dis = cell_instance.sector.district.district
        sec = cell_instance.sector.sector
        cell = cell_instance.cell
        all_villages = regions.get_villages_from_cell(prov, dis, sec, cell)

        for village in all_villages:
            num = num + 1
            c = Village(cell=cell_instance, village=village)
            instances.append(c)

        if num == 1000:
            Village.objects.bulk_create(instances)
            num = 0
    Village.objects.bulk_create(instances)
