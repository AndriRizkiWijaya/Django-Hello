from django.contrib import admin
from .models import Item, OrderItem, Order

# Register your models here.
class ItemModel(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Item, ItemModel)
admin.site.register(OrderItem)
admin.site.register(Order)
