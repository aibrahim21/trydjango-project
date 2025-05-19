from django.shortcuts import render

# Create your views here.
#create url in pages.url for each function

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')
