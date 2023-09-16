from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView
from django_tables2 import SingleTableView

from .models import Shop
from .tables import ShopTable


class ShopListView(SingleTableView):
    model = Shop
    table_class = ShopTable
    template_name = 'web/shop.html'
