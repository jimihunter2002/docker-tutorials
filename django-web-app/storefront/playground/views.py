from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# View is a request handler in django


def say_hello(request):
    return render(request, 'hello.html', {'name': 'Devops Docker Development'})
