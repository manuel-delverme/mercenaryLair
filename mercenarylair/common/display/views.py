# -*- coding: utf-8 -*-
from display.models import Service
from django.shortcuts import render_to_response,get_object_or_404
from django.shortcuts import render
from forms import MessageForm

def index(request,type_filter=""):
  services_list = Service.objects.all()
  return render_to_response('display/index.html',{'services_list':services_list,'type_filter':type_filter,}) 

def detail(request, service_id):
  service = get_object_or_404(Service, pk=service_id)
  return render_to_response('display/detail.html', {'service': service})

def post(request):
  return render(request, 'index.html', {'form': MessageForm()})
  #return render_to_response('display/post.html')

def update(request, service_id):
  service = get_object_or_404(Service, pk=service_id)
  return render_to_response('display/update.html', {'service': service})
