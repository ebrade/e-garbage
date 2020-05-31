from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout

from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, ListView, TemplateView

from egarbage.models import Register, District, Sector, Cell, Village
from .forms import RegisterForm, ContactForm, SignUpForm

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
    template_name = 'egarbage/history.html'
    hist = Register.objects.filter(name=request.user)
    args = {'hist': hist}
    return render(request, template_name, args)


@login_required
def register_item(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            reg = form.save(commit=False)
            reg.name = request.user
            reg.save()
            return render(request, 'egarbage/about.html')

        else:
            form = RegisterForm()
            return render(request, 'egarbage/register.html', {'form': form})
    return render(request, 'egarbage/register.html', {'form': form})


@login_required
class RegisterItem(CreateView):
    model = Register
    success_url = reverse_lazy('register_item')


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


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('about')
    else:
        form = SignUpForm()
    return render(request, 'egarbage/signup.html', {'form': form})


def logout(request):
    django_logout(request)
    return HttpResponseRedirect('about')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })
