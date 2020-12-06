from django.shortcuts import render

data_list = {
    'lists': [
        {'name': 'Написать в деканат', 'is_done': False},
        {'name': 'Распечать документы', 'is_done': True, 'date': '01.12.2020'},
        {'name': 'Сделать ДЗ', 'is_done': True},
        {'name': 'Создать папку templatetags', 'is_done': False}
    ],
    'user_name': 'Admin',
    'name_list': 'Список дел'
}


def item_view(request):
    context = data_list
    return render(request, 'list.html', context)
