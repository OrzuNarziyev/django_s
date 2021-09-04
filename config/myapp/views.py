from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404


# Create your views here.
from .models import Women


def index(request):
    w = Women.objects.all()
    return render(request,'myapp/index.html',{'women':w})


def categories(request, slug):
    return HttpResponse(f"categoriya {slug}")


def archive(request, year):
    if int(year) > 2021:
        raise Http404
    else:
        return HttpResponse(f'<h1>{year}</h1>')


def pageNotFound(request, exception):
    return HttpResponseNotFound(f'page topilmadi')
