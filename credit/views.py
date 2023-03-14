from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Client


class ClientListView(ListView):
    model = Client
    template_name = 'client_list.html'


class ClientDetailView(DetailView):
    model = Client
    template_name = 'client_detail.html'

