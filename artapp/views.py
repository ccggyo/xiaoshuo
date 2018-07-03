from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    print(request.path, request.method)
    print(request.META, request.GET)
    print(request.POST)
    # return HttpResponse('<h1>您好</h1>')
    return render(request, 'art/list.html',context={'name':'dakongyi', 'age': 18})