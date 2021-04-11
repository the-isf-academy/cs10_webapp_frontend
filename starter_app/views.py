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

class CreateAccountView(TemplateView):
    template_name = 'starter_app/createAccountView.html'

class TaskDashboard(TemplateView):
    template_name = 'starter_app/dashboardView.html'

class TaskForm(TemplateView):
    template_name = 'starter_app/taskFormView.html'

class EditTask(TemplateView):
    template_name = 'starter_app/updateTaskView.html'
