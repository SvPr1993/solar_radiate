import requests
from django.shortcuts import render
from app_solar_radiate.forms import DateForm
from app_solar_radiate.usecase import get_solar_activity


def index(request):
    result_solar_activity = get_solar_activity
    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            selected_date = form.cleaned_data['selected_date']
            solar_data = get_solar_activity(selected_date)

            context = {
                'form': form,
                'solar_data': solar_data,
                'selected_date': selected_date
            }
            return render(request, 'result.html', context)
    else:
        form = DateForm()

    return render(request, 'index.html', {'form': form})


def result(request):
    return render(request, 'result.html')
