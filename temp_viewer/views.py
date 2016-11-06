from django.http import HttpResponse
from django.shortcuts import (
    render, render_to_response
)


def home_page(request):
    template_view = 'temp_viewer/index.html'

    return render(request, template_view)


def page_not_found(request):
    template_view = '404.html'

    return render(request, template_view, status=404)


def server_error(request):
    template_view = '500.html'

    return render(request, template_view, status=500)
