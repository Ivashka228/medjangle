from django.http import HttpResponse
from django.shortcuts import render

ipp = "127.0.0.1"

def index(request):
    return render(request, 'index.html', {'ip':ipp})
def me(request):
    return render(request, 'me.html', {'ip':ipp})