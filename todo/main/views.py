from django.shortcuts import render, reverse, redirect
from main.models import ListModel
from main.form import ListForm


def main_view(request):
    lists = ListModel.objects.filter(user=request.user)
    contex = {
        'lists': lists,
        'user_name': request.user.username
    }
    return render(request, 'index.html', contex)


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
