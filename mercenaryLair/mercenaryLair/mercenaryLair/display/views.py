from display.models import Service
from django.shortcuts import render_to_response,get_object_or_404

def index(request):
  services_list = Service.objects.all()
  return render_to_response('display/index.html',{'services_list':services_list,}) 

def detail(request, service_id):
  p = get_object_or_404(Service, pk=service_id)
  return render_to_response('display/detail.html', {'display': p})
