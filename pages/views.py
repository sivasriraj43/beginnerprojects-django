from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    return HttpResponse("Hello,World")

def about_page_view(request):
    context = {
        "name":"Sivasriraj",
        "age":22,
    }
    return render(request,'pages/about.html',context)