from typing import Any
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context: dict[str,Any]={
        'title':'aifromuz',
        'content':'Home page of aifromuz'
    }
    return render(request,'main/index.html',context)

def about(request):
    context: dict[str,Any]={
        'title':'About',
        'content':'About us',
        'text':'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    }
    return render(request,'main/about.html',context)