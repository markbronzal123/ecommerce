from django.contrib import admin
from .models import Product, Category, Order, UserAccount, OrderItem

class ProductAdmin(admin.ModelAdmin):
    fieldsets   =   [
        ('Product Information',  {'fields':['sku']}),
        (None   ,   {'fields':['barcode']}),
        (None   ,   {'fields':['name']}),
        (None   ,   {'fields':['base_price']}),
        (None   ,   {'fields':['category']}),
        (None   ,   {'fields':['description']}),
        (None   ,   {'fields':['product_image']}),
        (None   ,   {'fields':['number_of_stocks']}),
    ]

    # display
    list_display = ('sku', 'name', 'base_price', 'date_created')
    list_filter = ['date_created']
    search_fields = ['name']

# class OrderAdmin(admin.ModelAdmin):
#     readonly_fields = ['OR', 'product', 'raw_total_price', 'delivery_fee', 'total_price', 'order_date']
#     actions = None
#
#     #  permissions
#     def has_add_permission(self, request):
#         return False
#
#     def has_change_permission(self, request, obj=None):
#             return False
#     # display
#     list_display = ('OR', 'total_price', 'order_date')
#     list_filter = ['order_date']
#     search_fields = ['OR']
#
# admin.site.register(Order, OrderAdmin)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(UserAccount)
# admin.site.register(Order)
# admin.site.register(OrderItem)
