from datetime import datetime, date


def get_solar_activity_usecase(date_input, repo):

    # Преобразуем date в datetime, если нужно
    if isinstance(date_input, date):
        date_obj = datetime.combine(date_input, datetime.min.time())
    elif isinstance(date_input, datetime):
        date_obj = date_input
    else:
        raise ValueError("date_input должен быть объектом date или datetime")

    data = repo.get_solar_activity_data(date_obj)

    return data

#Сделать dto и прокинуть через view, сначала сделать через фейк репозиторий, если получилось, то прокинуть оригинал репозитория
#Прочитать про TypeHinting в питоне
#Нужно через нейросеть подключить репозиторий с помощью интерфейса через протокол, обязательное уточнение, что юзкейс подключается без интерфейса
#Нужно сделать структуру похожу на оригинальный репо, сделать чтобы данные было похожи
