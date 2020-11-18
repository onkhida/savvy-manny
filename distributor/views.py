from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {}
    return render(request, "distributor/hometemplate.html", context)
    # return HttpResponse("<h1>Working</h1>")