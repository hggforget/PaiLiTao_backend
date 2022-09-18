from django.http import *
from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    context          = {}
    context['test'] = '主页'
    return JsonResponse(context)
