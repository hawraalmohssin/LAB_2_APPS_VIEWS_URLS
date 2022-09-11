from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
def home(request : HttpRequest):
    top_actor : str = "home"

    return HttpResponse(f"hello world,this is my new {home}")