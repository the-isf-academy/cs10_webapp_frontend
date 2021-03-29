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
    queryset = Task.objects.order_by("due_date")

class TaskForm(LoginRequiredMixin,FormView):
    template_name = 'starter_app/taskForm.html'
    form_class = TaskForm
    success_url = '/dashboard'


    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        if form.instance.task_assigned_to != "":
            form.instance.task_assigned_by = self.request.user.username
        
        form.instance.task_user = self.request.user
        form.save()
        return super().form_valid(form)

