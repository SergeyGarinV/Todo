from django.urls import path
from todo_item.views import ItemView, ItemGreate, edit_item, delete_item, is_done_view

app_name = 'items'

urlpatterns = [
    path('<int:pk>', ItemView.as_view(), name='items'),
    path('create/<int:pk>', ItemGreate.as_view(), name='create_item'),
    path('delete', delete_item, name='delete'),
    path('edit/<int:pk>', edit_item, name='edit_item'),
    path('is_done', is_done_view, name="is_done"),
]