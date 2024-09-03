from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def main(request: HttpRequest) -> HttpResponse:
    return render(request, template_name = 'index.html')

def myfeed(request: HttpRequest) -> HttpResponse:
    return HttpResponse("My_FEED")

def article_id(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse("Article ID")

def comment(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse("Comment")

def update(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse("ARTICLE UPDATE")

def delete(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse("ARTICLE DELETE")

def topics(request: HttpRequest) -> HttpResponse:
    return HttpResponse("TOPICS")

def create(request: HttpRequest) -> HttpResponse:
    return HttpResponse("CREATE")

def topics_id(request: HttpRequest, topic_id: int) -> HttpResponse:
    return HttpResponse("TOPICS ID")

def topics_id_subscribe(request: HttpRequest, topic_id: int) -> HttpResponse:
    return HttpResponse("TOPICS ID SUBSCRIBE")

def topics_id_unsubscribe(request: HttpRequest, topic_id: int) -> HttpResponse:
    return HttpResponse("TOPICS ID UNSUBSCRIBE")

def profile(request: HttpRequest) -> HttpResponse:
    return render(request, template_name = 'profile.html')

def register(request: HttpRequest) -> HttpResponse:
    return HttpResponse("REGISTER")

def set_password(request: HttpRequest) -> HttpResponse:
    return HttpResponse("SET PASSWORD")

def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse("LOGIN")

def logout(request: HttpRequest) -> HttpResponse:
    return HttpResponse("LOGOUT")

def year_month(request: HttpRequest, year: int, month: int) -> HttpResponse:
    if len(str(year)) > 4 or len(str(year)) < 4:
        raise ValueError("Helytelen dátum")
    if not (1 <= month <= 12):
        raise ValueError("Helytelen dátum")
    else:
        return HttpResponse("YEAR MONTH")


    

