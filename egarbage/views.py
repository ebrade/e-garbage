from django.shortcuts import render

# Create your views here.
from egarbage.models import Register
from .forms import RegisterForm


def about(request):
    return render(request, 'egarbage/about.html')


def history(request):
    return render(request, 'egarbage/history.html')


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        if request.POST.get('province') and request.POST.get('district') and \
                request.POST.get('sector') and request.POST.get('cell') and \
                request.POST.get('village') and request.POST.get('street') and \
                request.POST.get('e_waste_type') and request.POST.get('quantity'):
            reg = Register()

            reg.name = request.POST.get('name')
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
