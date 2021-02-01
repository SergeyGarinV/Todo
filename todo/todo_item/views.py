from django.shortcuts import render, reverse, redirect
from todo_item.models import ItemModel
from main.models import ListModel
from todo_item.form import ItemForm
from django.contrib.auth.decorators import login_required
from todo.settings import DIV_COUNT
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponse
import json


class ItemView(LoginRequiredMixin, generic.ListView):
    login_url = reverse_lazy('registration:login')
    model = ItemModel
    template_name = 'list.html'
    paginate_by = DIV_COUNT
    ordering = ['created']
    context_object_name = 'lists'

    def get_queryset(self):
        queryset = super().get_queryset()
        lists = ListModel.objects.select_related('user').get(id=self.kwargs['pk'])
        return queryset.filter(listmodules=lists)

    def get_context_data(self, **kwargs):
        lists = ListModel.objects.select_related('user').get(id=self.kwargs['pk'])
        contex = super().get_context_data(**kwargs)
        contex['user_name'] = self.request.user.username
        contex['name_list'] = lists.name
        contex['pk'] = self.kwargs['pk']
        return contex


class ItemGreate(LoginRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('registration:login')
    model = ItemModel
    template_name = 'new_item.html'
    form_class = ItemForm

    def get_success_url(self):
        return reverse_lazy('items:items', kwargs={'pk': self.kwargs['pk']})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        query_dict = kwargs.get('data')
        if query_dict:
            query_dict = query_dict.copy()
            query_dict['user'] = self.request.user
            query_dict['listmodules'] = self.kwargs['pk']
            kwargs['data'] = query_dict
        return kwargs

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['pk'] = self.kwargs['pk']
        return contex


@login_required(login_url='registration:login')
def edit_item(request, pk):
    item_ = ItemModel.objects.get(id=pk)
    form = ItemForm(instance=item_)
    if request.method == 'POST':
        name = request.POST.get('name')
        expr_date = request.POST.get('expr_date')
        form = ItemForm({
            'name': name,
            'expr_date': expr_date,
            'listmodules': item_.listmodules.id
        }, instance=item_)
        if form.is_valid():
            form.save()
            success_url = reverse('items:items', kwargs={'pk': item_.listmodules.id})
            return redirect(success_url)
    contex = {
        'form': form,
        'pk': pk,
        'listmodules': item_.listmodules.id
    }
    return render(request, 'edit_item.html', contex)


def delete_item(request):
    body = json.loads(request.body.decode())
    id = int(body.get('id', 0))
    if id:
        item = ItemModel.objects.filter(id=id).first()
        if item:
            item.delete()
            return HttpResponse(status=201)
    return HttpResponse(status=404)


def is_done_view(request):
    body = json.loads(request.body.decode())
    id = int(body.get('id', 0))
    if id:
        item = ItemModel.objects.filter(id=id).first()
        if item:
            item.is_done = not item.is_done
            item.save()
            return HttpResponse(status=201)
    return HttpResponse(status=404)
