import datetime

from django.contrib import admin

from models import Category, Product, Order
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_display_links = ('name', 'category')
    list_filter = ('category',)

class ProductOrderInline(admin.TabularInline):
    model = Order.products.through
    readonly_fields = ('quantity', 'product')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'shipping_address')
    list_display = ('user', 'status')
    list_display_links = ('user', 'status')
    list_filter = ('status', 'delivery_date')
    actions = ['mark_completed']
    inlines = [ProductOrderInline,]

    def get_actions(self, request):
        actions = super(OrderAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def mark_completed(modeladmin, request, queryset):
        queryset.update(status='C')
        queryset.update(delivery_date=datetime.datetime.now())

admin.site.register(Category, CategoryAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
