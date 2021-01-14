from django.shortcuts import render, reverse, redirect
from main.models import ListModel
from main.form import ListForm
from todo_item.models import ItemModel
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from todo.settings import DIV_COUNT


@login_required(login_url='registration:login')
def main_view(request):
    lists = ListModel.objects.filter(user=request.user).order_by('created')
    paginator = Paginator(lists, DIV_COUNT)
    page = request.GET.get('page')
    if not page:
        page = 1
    is_paginated = len(lists) > DIV_COUNT
    contex = {
        'lists': paginator.page(page),
        'user_name': request.user.username,
        'paginator': paginator,
        'is_paginated': is_paginated,
        'page_obj': {
            'number': int(page)
        }
    }
    return render(request, 'index.html', contex)


@login_required(login_url='registration:login')
def create_view(request):
    form = ListForm()
    if request.method == 'POST':
        name = request.POST.get('name')
        form = ListForm({
            'name': name,
            'user': request.user
        })
        if form.is_valid():
            form.save()
            success_url = reverse('main:main')
            return redirect(success_url)
    contex = {
        'form': form
    }
    return render(request, "new_list.html", contex)


@login_required(login_url='registration:login')
def edit_view(request, pk):
    list_ = ListModel.objects.get(id=pk)
    form = ListForm(instance=list_)
    if request.method == 'POST':
        name = request.POST.get('name')
        form = ListForm({
            'name': name,
            'user': request.user
        }, instance=list_)
        if form.is_valid():
            form.save()
            success_url = reverse('main:main')
            return redirect(success_url)
    contex = {
        'form': form,
        'pk': pk
    }
    return render(request, 'edit_list.html', contex)


def delete_list(request, pk):
    list_ = ListModel.objects.get(id=pk)
    list_.delete()
    success_url = reverse('main:main')
    return redirect(success_url)
