from django import forms
from .models import Register
from .regions import RwandaRegions


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        exclude = {'timestamp', 'name'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['province'].queryset = Register.objects.none()

    rda_regions = RwandaRegions()
    all = rda_regions.get_all_regions()
    provinces_list = rda_regions.get_provinces()
    provinces = []

    for prov in provinces_list:
        p = (prov, prov)
        provinces.append(p)

    province = forms.ChoiceField(choices=provinces, label='Province',
                                 widget=forms.Select(attrs={'class': 'form-control form-control-lg'}))

    e_waste_type = forms.ChoiceField(choices=choices, label='E-Waste Type',
                                     widget=forms.Select(attrs={'class': 'form-control form-control-lg'}))
