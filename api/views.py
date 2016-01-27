from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from api.models import New

# Create your views here.

def index(request):
    news = New.objects.all()[:2]
    data = serializers.serialize("json", news)
    return HttpResponse(data)
