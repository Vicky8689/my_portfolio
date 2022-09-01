# from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse('this id my home page (/)')
    context={'name':'vcky','status':'student'}
    return render (request,'home.html',context)

def about(request):
    # return HttpResponse('this id my about page')
    return render (request,'about.html')


def contact(request):
    # return HttpResponse('this id my contact page (/)')
    return render (request,'contact.html')


def projects(request):
    # return HttpResponse('this id my projects page (/)')
    return render (request,'projects.html')

