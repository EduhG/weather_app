from django.http import HttpResponse
import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from temp_viewer.models import Temperature


def temps_to_json(total):
    """
    Return a list of dictionary odjects of individual database row
    total determines the number of records to be returned when querying
    """

    temps = Temperature.objects.all().order_by("-date_time")[:total]
    temperatures = []

    for temp in temps:
        temperatures.append(temp.to_json())

    return temperatures


def get_json_temps(request):
    """
    Return jso response to ajax requetst
    """

    response = json.dumps(temps_to_json(10))
    try:
        return HttpResponse(response, content_type="application/json")
    except:
        return HttpResponse(json.dumps(None), content_type="application/json")


def home_page(request):
    template_view = 'temp_viewer/index.html'

    if request.method == 'POST':
        Temperature.objects.create(
            date_time=request.POST['date_time'],
            temp=request.POST['temp'])
        return redirect('/')

    temps = Temperature.objects.all()
    template_data = {
        'temps': temps,
    }
    return render(request, template_view, template_data)


def page_not_found(request):
    template_view = '404.html'

    return render(request, template_view, status=404)


def server_error(request):
    template_view = '500.html'

    return render(request, template_view, status=500)


@login_required(login_url="login/")
def login(request):
    template_view = 'temp_viewer/login.html'

    return render(request, template_view)
