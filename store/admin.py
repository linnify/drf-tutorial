from django.contrib import admin
from store.models import Store, Address, Stock

admin.site.register(Store)
admin.site.register(Address)
admin.site.register(Stock)