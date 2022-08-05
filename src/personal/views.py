from django.shortcuts import render

def index_view(request,*args,**kwargs):
    context = {}
    return render(request,'index.html',context)

def home_view(request,*args,**kwargs):
    return render(request,'home.html')




