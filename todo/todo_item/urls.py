from django.urls import path
from todo_item.views import item_view

app_name = 'items'

urlpatterns = [
    path('<int:pk>', item_view, name='items'),
    path('create/', item_view, name='create'),
    path('delete/', item_view),
    path('edit/<int:pk>', item_view)
]