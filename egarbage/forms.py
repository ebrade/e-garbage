from django.conf import settings

from .models import Register, District, Cell, Village, Sector, Contact
from .regions import RwandaRegions
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        exclude = {'timestamp', 'name', 'collected'}

        widgets = {
            'quantity': forms.NumberInput(attrs={'min': 1, 'class': 'form-control form-control-md'}),
            'province': forms.Select(attrs={'class': 'form-control form-control-md'}),
            'district': forms.Select(attrs={'class': 'form-control form-control-md'}),
            'sector': forms.Select(attrs={'class': 'form-control form-control-md'}),
            'cell': forms.Select(attrs={'class': 'form-control form-control-md'}),
            'village': forms.Select(attrs={'class': 'form-control form-control-md'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['district'].queryset = District.objects.none()
        self.fields['sector'].queryset = Sector.objects.none()
        self.fields['cell'].queryset = Cell.objects.none()
        self.fields['village'].queryset = Village.objects.none()

        if 'province' in self.data:
            try:
                id = int(self.data.get('province'))
                self.fields['district'].queryset = District.objects.filter(province_id=id).order_by('district')
            except(ValueError, TypeError):
                pass
        if 'province' and 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['sector'].queryset = Sector.objects.filter(district_id=district_id).order_by('sector')
            except(ValueError, TypeError):
                pass

        if 'province' and 'district' and 'sector' in self.data:
            try:
                sector_id = int(self.data.get('sector'))
                self.fields['cell'].queryset = Cell.objects.filter(sector_id=sector_id).order_by('sector')
            except(ValueError, TypeError):
                pass

        if 'province' and 'district' and 'sector' and 'cell' in self.data:
            try:
                cell_id = int(self.data.get('cell'))
                self.fields['village'].queryset = Village.objects.filter(cell_id=cell_id).order_by('sector')
            except(ValueError, TypeError):
                pass

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

    e_waste_type = forms.ChoiceField(choices=choices, label='E-waste Type',
                                     widget=forms.Select(attrs={'class': 'form-control form-control-md'}))
    street = forms.CharField(label='Street',
                             widget=forms.TextInput(attrs={'class': 'form-control form-control-md'}))


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('names', 'email', 'subject', 'message',)


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    phone = forms.CharField(max_length=16, help_text="Please Enter your Phone Number")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'password1', 'password2',)
