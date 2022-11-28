from django.contrib import admin
from .models import Main_Category, Product, Sub_Category,Orders,OrderItem

# Register your models here.
admin.site.register (Product)
admin.site.register (Main_Category)
admin.site.register (Sub_Category)

class OrderItemTubleinLine(admin.TabularInline) :
    model=OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines=[OrderItemTubleinLine]

admin.site.register (Orders, OrderAdmin)
admin.site.register (OrderItem)
