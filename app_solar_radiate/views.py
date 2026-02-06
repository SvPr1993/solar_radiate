from django.shortcuts import render
from app_solar_radiate.forms import DateForm
from app_solar_radiate.usecase import get_solar_activity_usecase
from app_solar_radiate.repo import SolarActivityRepo


def index(request):
    repo = SolarActivityRepo()
    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            selected_date = form.cleaned_data['selected_date']
            solar_data = get_solar_activity_usecase(selected_date, repo)

            context = {
                'form': form,
                'solar_data': solar_data,
                'selected_date': selected_date,
            }
            return render(request, 'result.html', context)
    else:
        form = DateForm()

    return render(request, 'index.html', {'form': form})


def result(request):
    return render(request, 'result.html')
