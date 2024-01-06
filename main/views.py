from typing import Any
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context: dict[str,Any]={
        'title':'aifromuz',
        'content':'home page of aifromuz',
        'list':[1,2,3,4,],
        'dict':{'first':1},
        'is_authenticated':False



    }
    return render(request,'main/index.html',context)