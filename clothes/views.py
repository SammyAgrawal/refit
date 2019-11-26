from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return (render(request, 'clothes/base.html', {}))


def item(request, cloth_id):
    return HttpResponse("Page for item %s." % cloth_id)