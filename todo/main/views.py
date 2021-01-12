from django.shortcuts import render, reverse, redirect
from main.models import ListModel
from main.form import ListForm
from todo_item.models import ItemModel
from django.contrib.auth.decorators import login_required


@login_required(login_url='registration:login')
def main_view(request):
    lists = ListModel.objects.filter(user=request.user)
    contex = {
        'lists': lists,
        'user_name': request.user.username
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
