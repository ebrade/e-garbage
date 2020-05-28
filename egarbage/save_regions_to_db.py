import json

from egarbage.regions import RwandaRegions
from .models import Province, District, Sector, Cell, Village

regions = RwandaRegions()


json_data = open('rwanda_regions.json').read()

response = json.loads(json_data)


# Save all Province to db
provinces = regions.get_provinces()
for prov in provinces:
    province = Province(province=prov)
    province.save()

"""
json_data = open('core/static/core/data/drug1.json').read()

response = json.loads(json_data)
a = 0
b = 0

for data in response['results']:
    generic_name = data['openfda'].get('generic_name')
    brand_name = data['openfda'].get('brand_name')
    substance_name = data['openfda'].get('substance_name')
    spl_product_data_elements = data.get('spl_product_data_elements')
    drug_interactions = data.get('drug_interactions')
    when_using = data.get('when_using')
    pregnancy_or_breast_feeding = data.get('pregnancy_or_breast_feeding')
    information_for_patients = data.get('information_for_patients')
    warnings_and_cautions = data.get('warnings_and_cautions')
    purpose = data.get('purpose')
    dosage_and_administration = data.get('dosage_and_administration')

    if generic_name is None:
        generic_name = []
    if brand_name is None:
        brand_name = []
    if substance_name is None:
        substance_name = []
    if spl_product_data_elements is None:
        spl_product_data_elements = []
    if drug_interactions is None:
        drug_interactions = []
    if when_using is None:
        when_using = []
    if pregnancy_or_breast_feeding is None:
        pregnancy_or_breast_feeding = []
    if information_for_patients is None:
        information_for_patients = []
    if warnings_and_cautions is None:
        warnings_and_cautions = []
    if purpose is None:
        purpose = []
    if dosage_and_administration is None:
        dosage_and_administration = []

    try:
        medicine = Medicine(generic_name=generic_name,
                            brand_name=brand_name,
                            substance_name=substance_name,
                            spl_product_data_elements=spl_product_data_elements,
                            dosage_and_administration=dosage_and_administration,
                            drug_interactions=drug_interactions,
                            when_using=when_using,
                            pregnancy_or_breast_feeding=pregnancy_or_breast_feeding,
                            information_for_patients=information_for_patients,
                            warnings_and_cautions=warnings_and_cautions,
                            purpose=purpose
                            )
        medicine.save()


    except IntegrityError as e:

        print(e)
        pass
    """