from django.utils import timezone


common_timezones = {
    'Almaty': 'Asia/Almaty',
    'Vladivostok': 'Asia/Vladivostok',
    'Moscow': 'Europe/Moscow',
}


def current_time(request):
    return {
        'current_time': timezone.localtime(timezone.now())
    }


def timezones(request):
    return {
        'timezones': common_timezones
    }
