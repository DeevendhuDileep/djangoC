from django.shortcuts import render

# Create your views here.

def load_home_page(request):
    return render(request,'home.html',{'color':'yellow','animal':'dog'})

def load_index_page(request):
    return render(request,'index.html')

def load_add_page(request):
    return render(request,'add.html')

def add_num(request):
    n1=int(request.GET['num1'])
    n2=int(request.GET['num2'])
    sum = n1+n2
    return render(request,'result.html',{'result':sum})