from django.contrib import admin
from egarbage.models import Register

# Register your models here.


admin.site.site_title = " E-garbage Admin Panel"
admin.site.site_header = "E-garbage Admin Panel"
admin.site.index_title = ""


class RegisterAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'province',
                    'district',
                    'sector',
                    'cell',
                    'village',
                    'street',
                    'e_waste_type',
                    'quantity',
                    'collected',
                    'timestamp']


admin.site.register(Register, RegisterAdmin)
