from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, FormView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

#models

from django.contrib.auth import login, authenticate


# Create your views here.
class IndexView(TemplateView):
    template_name = 'starter_app/indexView.html'
