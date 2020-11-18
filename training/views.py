from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def trhome(request):
    context = {

    }

    return render(request, 'training/trhome.html', context)