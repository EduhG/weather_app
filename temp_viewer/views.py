from django.http import HttpResponse
from django.shortcuts import redirect, render
from temp_viewer.models import Temperature


def home_page(request):
    template_view = 'temp_viewer/index.html'

    if request.method == 'POST':
        print 'request body =>', request.body
        Temperature.objects.create(
            date_time=request.POST['date_time'],
            temp=request.POST['temp'])
        return redirect('/')

    temps = Temperature.objects.all()
    return render(request, template_view, {'temps': temps})


# def home_page(request):
#     template_view = 'temp_viewer/index.html'

#     return render(request, template_view)


def page_not_found(request):
    template_view = '404.html'

    return render(request, template_view, status=404)


def server_error(request):
    template_view = '500.html'

    return render(request, template_view, status=500)
