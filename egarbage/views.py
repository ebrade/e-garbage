from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views.generic import CreateView

from egarbage.models import Register, District, Sector, Cell, Village
from .forms import RegisterForm, ContactForm

# The below ones are for single use.
# from django.http import HttpResponse
from .regions import RwandaRegions
from .save_regions_to_db import save_prov_dis_to_db, save_sectors, save_cells, save_villages


def about(request):
    # save_prov_dis_to_db()
    # save_sectors()
    # save_cells()
    # save_villages()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            return redirect('about')
    else:
        form = ContactForm()
    return render(request, 'egarbage/about.html', {'form': form})


@login_required
def history(request):
    return render(request, 'egarbage/history.html')


@login_required
def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            reg = form.save(commit=False)
            reg.name = request.user.username
            reg.save()
            return render(request, 'egarbage/about.html')

        else:
            form = RegisterForm()
            return render(request, 'egarbage/register.html', {'form': form})
    return render(request, 'egarbage/register.html', {'form': form})


@login_required
class RegisterItem(CreateView):
    model = Register
    success_url = reverse_lazy('register')


def load_district(request):
    province = request.GET.get('province')
    districts = District.objects.filter(province_id=province).order_by('district')
    return render(request, 'egarbage/load_districts.html', {'districts': districts})


def load_sector(request):
    district = request.GET.get('district')
    sectors = Sector.objects.filter(district_id=district).order_by('sector')
    return render(request, 'egarbage/load_sectors.html', {'sectors': sectors})


def load_cell(request):
    sector = request.GET.get('sector')
    cells = Cell.objects.filter(sector_id=sector).order_by('cell')
    return render(request, 'egarbage/load_cells.html', {'cells': cells})


def load_village(request):
    cell = request.GET.get('cell')
    villages = Village.objects.filter(cell_id=cell).order_by('village')
    return render(request, 'egarbage/load_villages.html', {'villages': villages})
