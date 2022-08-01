from django.shortcuts import render, redirect
from .models import Url
from uuid import uuid4
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')


def create(request):
    if request.method == 'POST':
        url = request.POST['link']
        uid = str(uuid4())[:5]
        new_url = Url(link=url, uuid=uid)
        new_url.save()
        return HttpResponse(uid)


def go(request, pk):
    url = Url.objects.get(uuid=pk)
    link = url.link
    return redirect('https://'+link)
