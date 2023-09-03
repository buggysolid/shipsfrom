from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Shop


def index(request):
    shops = Shop.objects.all()
    template = loader.get_template('web/index.html')
    context = {
        'shops': shops,
    }
    return HttpResponse(template.render(context, request))
