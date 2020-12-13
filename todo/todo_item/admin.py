from django.contrib import admin
from todo_item.models import ItemModel


class ListAdmin(admin.ModelAdmin):
    list_display = ['id', 'created', 'name', 'is_done', 'listmodules_id', 'expr_date']
    list_filter = ['created', 'name', 'is_done', 'listmodules_id']
    search_fields = ['name', 'listmodules_id']


admin.site.register(ItemModel, ListAdmin)
