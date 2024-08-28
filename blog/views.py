from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def main(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Szia")

def myfeed(request: HttpRequest) -> HttpResponse:
    return HttpResponse("My_FEED")

def article(request: HttpRequest) -> HttpResponse:
    return ("Article_ID")

def comment(request: HttpRequest) -> HttpResponse:
    return ("Article Comment")