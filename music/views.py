from django.shortcuts import render
from django.http import HttpResponse
from .models import Music
def index(request):
    music = Music.objects.all()
    return render(request, 'music/index.html', {
        'music':music,
        'title':'Список музыки'
    })