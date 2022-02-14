from django.contrib import admin
from .models import CustomUser

# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    fields = ['username', 'full_name',
              'gender', 'national_code', 'birthday_date', 'ceremony_datetime', 'country']
    list_display = ['username', 'first_name', 'last_name',
                    'gender', 'national_code', 'birthday_date']
    search_fields = ['username', 'full_name']
    ordering = ['ceremony_datetime']

    @admin.display(description='first_name')
    def first_name(self, obj):
        name = obj.get_first_and_last_name()
        return name['first_name']

    @admin.display(description='last_name')
    def last_name(self, obj):
        name = obj.get_first_and_last_name()
        return name['last_name']
