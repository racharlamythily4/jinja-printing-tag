from django.shortcuts import render

# Create your views here.


def data_render(request):

    d={'age':21,'name':'Myth','courses':['PYTHON','JAVA','MERN','DJANGO'] }

    return render(request,"data_render.html",context=d)

def ifelse(request):
    dic={'coursefee':(30000,35000,40000,'additionally added for python students')}
    return render(request,'if-else.html',context=dic)

def ifelif(request):
    dic={'trainers':['Santosh','Ravesh','Kishor','Harshad']}
    return render(request,'ifelif.html',context=dic)

def nestedifelse(request):
    dic={'a':10,'b':20,'c':15,'Junior_Trainers':('Rakesh','Pranay')}
    return render(request,'nested-if-else.html',context=dic)

def forloop(request):
    d={'My_Details':['Mythily',21,'Python_Student','PYD-M1']}
    return render(request,'for.html',d)