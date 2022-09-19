from django.shortcuts import render

from .models import *


def home(request):

    return render(request, 'home.html')

def blog(request):
    data={
        "maqolalar":Maqola.objects.all()
    }
    return render(request, 'blog.html',data)

def about(request):
    data = {
        "home": Maqola.objects.all()
    }
    return render(request, 'about.html', data)

def maqola(request, pk):
    data={
        "maqola": Maqola.objects.get(id=pk)
    }



    return render(request, 'maqola.html', data)



def intervyular(request):
    data={
        "intervyular":Intervyu.objects.all()
    }
    return render(request, 'interviyu.html',data)
