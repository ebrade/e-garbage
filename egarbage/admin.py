from django.contrib import admin
from egarbage.models import Register, Province, District, Sector, Cell, Village, Contact

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


class ProvinceAdmin(admin.ModelAdmin):
    list_display = ['province']


admin.site.register(Province, ProvinceAdmin)


class DistrictAdmin(admin.ModelAdmin):
    list_display = ['province', 'district']


admin.site.register(District, DistrictAdmin)


class SectorAdmin(admin.ModelAdmin):
    list_display = ['district', 'sector']


admin.site.register(Sector, SectorAdmin)


class CellAdmin(admin.ModelAdmin):
    list_display = ['sector', 'cell']


admin.site.register(Cell, CellAdmin)


class VillageAdmin(admin.ModelAdmin):
    list_display = ['cell', 'village']


admin.site.register(Village, VillageAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['names', 'email', 'subject', 'message']


admin.site.register(Contact, ContactAdmin)
