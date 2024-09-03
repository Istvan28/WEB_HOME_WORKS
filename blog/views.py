from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def main(request: HttpRequest) -> HttpResponse:
    return render(request, template_name = 'index.html')

def myfeed(request: HttpRequest) -> HttpResponse:
    return render(request, template_name = 'my-feed.html')

def article_id(request: HttpRequest, article_id: int) -> HttpResponse:
    return render(request, template_name = 'article_id.html')

def comment(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse("Comment")

def update(request: HttpRequest, article_id: int) -> HttpResponse:
    return render(request, template_name = 'article_id_update.html')

def delete(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse("ARTICLE DELETE")

def topics(request: HttpRequest) -> HttpResponse:
   return render(request, template_name = 'topics.html')

def create(request: HttpRequest) -> HttpResponse:
   return render(request, template_name = 'create.html')

def topics_id(request: HttpRequest, topic_id: int) -> HttpResponse:
    return render(request, template_name = 'topics_id.html')

def topics_id_subscribe(request: HttpRequest, topic_id: int) -> HttpResponse:
    return render(request, template_name = 'topics_id.html')

def topics_id_unsubscribe(request: HttpRequest, topic_id: int) -> HttpResponse:
    return HttpResponse("TOPICS ID UNSUBSCRIBE")

def profile(request: HttpRequest) -> HttpResponse:
    return render(request, template_name = 'profile.html')

def register(request: HttpRequest) -> HttpResponse:
    return render(request, template_name = 'register.html')

def set_password(request: HttpRequest) -> HttpResponse:
    return render(request, template_name = 'set-password.html')

def login(request: HttpRequest) -> HttpResponse:
   return render(request, template_name = 'login.html')

def logout(request: HttpRequest) -> HttpResponse:
    return HttpResponse("LOGOUT")

def year_month(request: HttpRequest, year: int, month: int) -> HttpResponse:
    if len(str(year)) > 4 or len(str(year)) < 4:
        raise ValueError("Helytelen dátum")
    if not (1 <= month <= 12):
        raise ValueError("Helytelen dátum")
    else:
        return HttpResponse("YEAR MONTH")


    

