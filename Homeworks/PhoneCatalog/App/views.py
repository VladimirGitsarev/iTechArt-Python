from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

# Create your views here.

def index(request):
    users = User.objects.all()
    return render(
        request,
        "index.html",
        {
            "catalog": users
        }   
    )

def catalog(request, user_id):
    user = User.objects.get(id=user_id)
    print(user_id)
    return render(
        request, 
        "user.html",
        {
            "user": user
        }
    )

def main(request):
    return HttpResponseRedirect("/catalog")



