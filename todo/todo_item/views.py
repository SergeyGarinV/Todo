from django.shortcuts import render
from todo_item.models import ItemModel
from main.models import ListModel


def item_view(request):
    lists = ItemModel.objects.filter(listmodules_id__user=request.user, listmodules_id=1)
    context = {
        'lists': lists,
        'user_name': request.user,
        'name_list': lists[0].listmodules_id.name
    }
    return render(request, 'list.html', context)
