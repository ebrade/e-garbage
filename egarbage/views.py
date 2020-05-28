import simplejson as simplejson
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from egarbage.models import Register
from .forms import RegisterForm
from .regions import RwandaRegions


def about(request):
    return render(request, 'egarbage/about.html')


def history(request):
    return render(request, 'egarbage/history.html')


# We have to change this thing below I think it is not necessary at all
def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        if request.POST.get('province') and request.POST.get('district') and \
                request.POST.get('sector') and request.POST.get('cell') and \
                request.POST.get('village') and request.POST.get('street') and \
                request.POST.get('e_waste_type') and request.POST.get('quantity'):
            reg = Register()

            reg.name = request.user.username
            reg.province = request.POST.get('province')
            reg.district = request.POST.get('district')
            reg.sector = request.POST.get('sector')
            reg.cell = request.POST.get('cell')
            reg.village = request.POST.get('village')
            reg.street = request.POST.get('street')
            reg.e_waste_type = request.POST.get('e_waste_type')
            reg.quantity = request.POST.get('quantity')
            reg.save()

            return render(request, 'egarbage/register.html')

        else:
            return render(request, 'egarbage/register.html')
    return render(request, 'egarbage/register.html', {'form': form})


class RegisterItem(CreateView):
    model = Register
    success_url = reverse_lazy('register')


def load_district(request):
    province = request.GET.get('province')
    rda_regions = RwandaRegions()
    district = rda_regions.get_districts_from_province(province)
    result_set = []
    for dis in district:
        result_set.append({'name': dis})

    return HttpResponse(simplejson.dumps(result_set), content_type='application/json')


def load_sector(request):
    province = request.GET.get('province')
    district = request.GET.get('district')
    rda_regions = RwandaRegions()
    sector = rda_regions.get_sectors_from_district(province, district)
    result_set = []
    for s in sector:
        result_set.append({'name': s})

    return HttpResponse(simplejson.dumps(result_set), content_type='application/json')


def load_cell(request):
    province = request.GET.get('province')
    district = request.GET.get('district')
    sector = request.GET.get('sector')
    rda_regions = RwandaRegions()
    cell = rda_regions.get_cells_from_sector(province, district, sector)
    result_set = []
    for c in cell:
        result_set.append({'name': c})

    return HttpResponse(simplejson.dumps(result_set), content_type='application/json')


def load_village(request):
    province = request.GET.get('province')
    district = request.GET.get('district')
    sector = request.GET.get('sector')
    cell = request.GET.get('cell')
    rda_regions = RwandaRegions()
    village = rda_regions.get_villages_from_cell(province, district, sector, cell)
    result_set = []
    for v in village:
        result_set.append({'name': v})

    return HttpResponse(simplejson.dumps(result_set), content_type='application/json')
