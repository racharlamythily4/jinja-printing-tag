from django.shortcuts import render

# Create your views here.


def data_render(request):

    d={'name':'MYTH','age': 21}

    return render(request,"data_render.html",context=d)

def ifelse(request):
    dic={'a':10,'b':20}
    return render(request,'if-else.html',context=dic)

def ifelif(request):
    dic={'a':10,'b':20,'c':30}
    return render(request,'ifelif.html',context=dic)

def nestedifelse(request):
    dic={'a':200,'b':150,'c':100}
    return render(request,'nested-if-else.html',context=dic)