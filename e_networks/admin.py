from django.contrib import admin

from e_networks.models import Contacts, NetworkNode, Product
from users.models import User

# Register your models here.

@admin.register(User)
class UserCustomAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'is_active')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_active',)

@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'supplier', 'debt', 'contacts', 'id')
    list_filter = ('contacts__city',)
    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        queryset.update(debt=0.00)

    clear_debt.short_description = 'Обнулить долг'

admin.site.register(Contacts)
# admin.site.register(NetworkNode)
admin.site.register(Product)
