from django.shortcuts import render, reverse, redirect
from main.models import ListModel
from main.form import ListForm
from django.contrib.auth.decorators import login_required
from todo.settings import DIV_COUNT
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.http import HttpResponse
import json


class MainView(LoginRequiredMixin, generic.ListView):
    login_url = reverse_lazy('registration:login')
    model = ListModel
    template_name = 'index.html'
    paginate_by = DIV_COUNT
    ordering = ['created', 'name']
    context_object_name = 'lists'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['user_name'] = self.request.user.username
        return contex


class CreateView(LoginRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('registration:login')
    model = ListModel
    template_name = 'new_list.html'
    form_class = ListForm
    success_url = reverse_lazy('main:main')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        query_dict = kwargs.get('data')
        if query_dict:
            query_dict = query_dict.copy()
            query_dict['user'] = self.request.user
            kwargs['data'] = query_dict
        return kwargs

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


def delete_list(request):
    body = json.loads(request.body.decode())
    id = int(body.get('id', 0))
    if id:
        item = ListModel.objects.filter(id=id).first()
        if item:
            item.delete()
            return HttpResponse(status=201)
    return HttpResponse(status=404)


def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('registration:login'))
