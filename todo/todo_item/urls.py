from django.urls import path
from todo_item.views import item_view, item_create

app_name = 'items'

urlpatterns = [
    path('<int:pk>', item_view, name='items'),
    path('create/<int:pk>', item_create, name='create_item'),
    path('delete/', item_view),
    path('edit/<int:pk>', item_view)
]