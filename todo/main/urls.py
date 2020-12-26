from django.urls import path
from main.views import main_view, create_view

app_name = 'main'

urlpatterns = [
    path('', main_view, name='main'),
    path('create/', create_view, name='create'),
    path('delete/', main_view),
    path('edit/', main_view)
]
