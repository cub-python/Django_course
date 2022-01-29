# Register your models here.
from baskets.models import Basket
from django.contrib import admin


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity')
    readonly_fields = ('create_timestamp', 'update_timestamp')
    extra = 0
