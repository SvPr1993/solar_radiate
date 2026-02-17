from django.shortcuts import render
from app_solar_radiate.forms import DateForm
from app_solar_radiate.usecase import get_solar_activity_usecase
from datetime import datetime
from app_solar_radiate.repo import SolarActivityRepo
from app_solar_radiate.repo_fake import SolarActivityRepoFake
from app_solar_radiate.dto import OutDTO

class SolarRepoFactory:
    @staticmethod
    def execute():
        # Для теста используем фейковый репозиторий
        return SolarActivityRepoFake()
        # Для продакшена раскомментировать:
        #return SolarActivityRepo()

def index(request):
    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            selected_date = form.cleaned_data['selected_date']
            selected_datetime = datetime.combine(selected_date, datetime.min.time())
            repo_construct = SolarRepoFactory()
            solar_data_dto = get_solar_activity_usecase(
                selected_datetime,
                repo_construct.execute()
            )

            context = {
                'form': form,
                'solar_data': solar_data_dto,
                'selected_date': selected_date,
            }
            print(solar_data_dto)
            return render(request, 'result.html', context)
    else:
        form = DateForm()

    return render(request, 'index.html', {'form': form})

def result(request):
    return render(request, 'result.html')


