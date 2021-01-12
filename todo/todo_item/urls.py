from django.urls import path
from todo_item.views import item_view, item_create, edit_item, delete_item

app_name = 'items'

urlpatterns = [
    path('<int:pk>', item_view, name='items'),
    path('create/<int:pk>', item_create, name='create_item'),
    path('delete/<int:pk>', delete_item, name='delete'),
    path('edit/<int:pk>', edit_item, name='edit_item')
]