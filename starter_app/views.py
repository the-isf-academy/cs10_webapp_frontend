from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, FormView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

#models
from .models import Task
from .forms import TaskForm, CreateAccountForm

from django.contrib.auth import login, authenticate


# Create your views here.
class IndexView(TemplateView):
    template_name = 'starter_app/indexView.html'

class CreateAccountView(FormView):
    template_name = 'starter_app/createAccount.html'
    form_class = CreateAccountForm

    success_url = '/dashboard'


    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return super().form_valid(form)

class TaskDashboard(ListView):
    template_name = 'starter_app/dashboard.html'
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # filter out archieved tasks
        data = self.model.objects.all().filter(archive=False)

        # filter tasks for user
        tasks = data.filter(task_assigned_to=self.request.user.username)
        context['user_tasks'] = tasks.distinct().order_by('-due_date')

        return context

class TaskForm(LoginRequiredMixin,FormView):
    template_name = 'starter_app/taskForm.html'
    form_class = TaskForm
    success_url = '/dashboard'


    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        if form.instance.task_assigned_to == "":
            form.instance.task_assigned_to = self.request.user.username

        form.instance.task_user = self.request.user
        form.save()
        return super().form_valid(form)

class EditTask(UpdateView):
    model = Task
    template_name = 'starter_app/updateTask.html'
    success_url = '/dashboard'

    fields = [
        "title",
        "label",
        "notes",
        "archive",
        "due_date"
    ]
