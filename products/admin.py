from django.contrib import admin
from products.models import Product, ProductClient, Distribution


class ProductAdmin(admin.ModelAdmin):
    list_display = ('ean13', 'name_prep',)


class ProductClientAdmin(admin.ModelAdmin):
    list_display = ('ean13', 'name_prep')


class DistributionAdmin(admin.ModelAdmin):
    list_display = ('product', 'names', 'count_names')
    read_only_fields = ('product', 'names', 'count_names')


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductClient, ProductClientAdmin)
admin.site.register(Distribution, DistributionAdmin)
