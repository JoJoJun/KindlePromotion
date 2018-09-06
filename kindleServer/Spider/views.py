from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello Django ! ")
def main(request):
    return render(request,'main.html')