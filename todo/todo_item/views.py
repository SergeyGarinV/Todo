from django.shortcuts import render, reverse, redirect
from todo_item.models import ItemModel
from main.models import ListModel
from todo_item.form import ItemForm


def item_view(request, pk):
    lists = ListModel.objects.select_related('user').get(id=pk)
    list_item = ItemModel.objects.filter(listmodules=lists)
    context = {
        'lists': list_item,
        'user_name': request.user,
        'name_list': lists.name,
        'pk': pk
    }
    return render(request, 'list.html', context)


def item_create(request, pk):
    form = ItemForm()
    if request.method == 'POST':
        name = request.POST.get('name')
        expr_date = request.POST.get('expr_date')
        form = ItemForm({
            'name': name,
            'expr_date': expr_date,
            'listmodules': pk
        })
        if form.is_valid():
            form.save()
            success_url = reverse('items:items', kwargs={'pk': pk})
            return redirect(success_url)
    contex = {
        'form': form
    }
    return render(request, 'new_item.html', contex)
