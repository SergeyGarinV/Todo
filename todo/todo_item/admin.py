from django.contrib import admin
from todo_item.models import ItemModel


class ListAdmin(admin.ModelAdmin):
    list_display = ['id', 'created', 'name', 'is_done', 'listmodules', 'expr_date']
    list_filter = ['created', 'name', 'is_done', 'listmodules']
    search_fields = ['name', 'listmodules__name']


admin.site.register(ItemModel, ListAdmin)
