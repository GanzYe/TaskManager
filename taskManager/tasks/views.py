from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.views.generic import TemplateView, UpdateView, DeleteView, CreateView

from tasks.models import Tasks

from tasks.forms import TasksForm


@login_required(login_url='/login')
def allTasks(request):
    context = {
        'fulfilled_tasks': Tasks.objects.filter(status="fulfilled", author=request.user.id),
        'unfulfilled_tasks': Tasks.objects.filter(status="unfulfilled", author=request.user.id),
    }
    return render(request, 'tasks/index.html', context)


class TasksCreate(LoginRequiredMixin, CreateView):
    login_url = '/login'
    template_name = 'tasks/task_create.html'
    model = Tasks
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["forms"] = TasksForm()
        context["forms"].fields['author'].initial = self.request.user.id
        return context


@login_required(login_url='/login')
def edit(request, id):
    if request.method == 'GET':
        return redirect('/')
    else:
        task = Tasks.objects.get(id=id)
        task.status = "fulfilled"
        task.save()
        return redirect('/')


class TaskDelete(LoginRequiredMixin, DeleteView):
    login_url = '/login'
    model = Tasks
    pk_url_kwarg = 'id'
    success_url = '/'

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)
