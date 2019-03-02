from django.shortcuts import render , get_object_or_404 ,redirect
from django.utils import timezone
from .models import Portpolio
# Create your views here.
def page(request):
    portpolios=Portpolio.objects
    return render(request,'portpolio.html',{'portpolios':portpolios})