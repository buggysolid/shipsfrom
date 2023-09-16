import django_tables2 as tables
from .models import Shop


class ShopTable(tables.Table):
    class Meta:
        model = Shop
        template_name = "django_tables2/bootstrap.html"
        fields = ("category", "shipper", "website")
