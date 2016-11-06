from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    template_view = 'index.html'

    return render(request, template_view)
