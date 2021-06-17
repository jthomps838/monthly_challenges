from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def challenges(request):
    return HttpResponse('Check out all of our challenges')


def january(request):
    return HttpResponse("january")


def february(request):
    return HttpResponse("february")


def march(request):
    return HttpResponse("march")


def april(request):
    return HttpResponse("april")


def may(request):
    return HttpResponse("may")


def june(request):
    return HttpResponse("june")


def july(request):
    return HttpResponse("july")


def august(request):
    return HttpResponse("august")


def september(request):
    return HttpResponse("september")


def october(request):
    return HttpResponse("october")


def november(request):
    return HttpResponse("november")


def december(request):
    return HttpResponse("december")
