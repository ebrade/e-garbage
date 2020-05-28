from django import forms
from .models import Register, District, Cell, Village, Sector
from .regions import RwandaRegions


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        exclude = {'timestamp', 'name', 'collected'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['province'].queryset = Register.objects.none()

        if 'province' in self.data:
            try:
                id = int(self.data.get('province'))
                self.fields['district'].queryset = District.objects.filter(province_id=id).order_by('district')
            except(ValueError, TypeError):
                pass
        if 'province' and 'district' in self.data:
            try:
                province_id = int(self.data.get('province'))
                district_id = int(self.data.get('district'))
                self.fields['sector'].queryset = Sector.objects.filter(province_id=province_id, district_id=district_id).order_by('sector')
            except(ValueError, TypeError):
                pass

        if 'province' and 'district' and 'sector' in self.data:
            try:
                province_id = int(self.data.get('province'))
                district_id = int(self.data.get('district'))
                sector_id = int(self.data.get('sector'))
                self.fields['cell'].queryset = Cell.objects.filter(province_id=province_id, district_id=district_id,
                                                                   sector_id=sector_id).order_by('sector')
            except(ValueError, TypeError):
                pass

        if 'province' and 'district' and 'sector' and 'cell' in self.data:
            try:
                province_id = int(self.data.get('province'))
                district_id = int(self.data.get('district'))
                sector_id = int(self.data.get('sector'))
                cell_id = int(self.data.get('cell'))
                self.fields['village'].queryset = Village.objects.filter(province_id=province_id,
                                                                         district_id=district_id, sector_id=sector_id,
                                                                         cell_id=cell_id).order_by('sector')
            except(ValueError, TypeError):
                pass

    rda_regions = RwandaRegions()
    # rda_regions.get_all_regions()
    provinces_list = rda_regions.get_provinces()
    provinces = [('', 'Choose...')]
    district = [('', 'Choose...')]
    sector = [('', 'Choose...')]
    cell = [('', 'Choose...')]
    village = [('', 'Choose...')]

    for prov in provinces_list:
        p = (prov, prov)
        provinces.append(p)

    choices = (
        ('', 'Choose...'),
        ('Laptop', 'Laptop'),
        ('Computer', 'Computer'),
        ('Phone', 'Phone'),
        ('Radio', 'Radio'),
        ('Charger', 'Charger'),
        ('Speaker', 'Speaker'),
        ('Printer', 'Printer'),
        ('Headphone', 'Headphone'),
        ('Cables', 'Cables')
    )

    province = forms.ChoiceField(choices=provinces, label='Province',
                                 widget=forms.Select(attrs={'class': 'form-control form-control-md',
                                                            'onchange': "getDistricts()"}))
    e_waste_type = forms.ChoiceField(choices=choices, label='E-waste Type',
                                     widget=forms.Select(attrs={'class': 'form-control form-control-md'}))
    district = forms.ChoiceField(choices=district, label='District',
                                 widget=forms.Select(attrs={'class': 'form-control form-control-md',
                                                            'onchange': "getSectors()"}))
    sector = forms.ChoiceField(choices=sector, label='Sector',
                               widget=forms.Select(attrs={'class': 'form-control form-control-md',
                                                          'onchange': "getCells()"}))
    cell = forms.ChoiceField(choices=cell, label='Cell',
                             widget=forms.Select(attrs={'class': 'form-control form-control-md',
                                                        'onchange': "getVillages()"}))
    village = forms.ChoiceField(choices=village, label='Village',
                                widget=forms.Select(attrs={'class': 'form-control form-control-md'}))
    street = forms.CharField(label='Street',
                             widget=forms.TextInput(attrs={'class': 'form-control form-control-md'}))
    quantity = forms.IntegerField(label='Quantity',
                                  widget=forms.NumberInput(attrs={'class': 'form-control form-control-md'}))

