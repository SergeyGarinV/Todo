from django.shortcuts import render
from todo_item.models import ItemModel
from main.models import ListModel


def item_view(request, pk):
    lists = ListModel.objects.select_related('user').get(id=pk)
    list_item = ItemModel.objects.filter(listmodules=lists)
    #lists = ItemModel.objects.filter(listmodules_id__user=request.user, listmodules_id=pk)
    context = {
        'lists': list_item,
        'user_name': request.user,
        'name_list': lists.name
    }
    return render(request, 'list.html', context)
