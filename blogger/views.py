from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def html(request):
    return render(request, "index.html")

def index(request):
    return HttpResponse("<h1>HTML HOME blogger</h1> <a href='http://127.0.0.1:8000/admin/'>Link to Admin</a>")
# Create your views here.
