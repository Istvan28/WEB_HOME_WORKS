from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def main(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Szia")

def myfeed(request: HttpRequest) -> HttpResponse:
    return HttpResponse("My_FEED")
