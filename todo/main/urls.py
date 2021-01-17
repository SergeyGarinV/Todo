from django.urls import path
from main.views import MainView, CreateView, edit_view, delete_list, logout_view

app_name = 'main'

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('create/', CreateView.as_view(), name='create'),
    path('delete/<int:pk>', delete_list, name='delete'),
    path('edit/<int:pk>', edit_view, name='edit'),
    path('logout/', logout_view, name='logout')
]
