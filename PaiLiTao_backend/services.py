import json

from django.http import *
from django.shortcuts import render
from django.views.generic import TemplateView

from PaiLiTao_backend.algorithm.FP import selectPath1


def index(request):
    context          = {}
    context['test'] = '主页'
    return JsonResponse(context)



def picrecive(request):
    if (request.method == 'POST'):
        print("the POST method")
        postBody = request.POST
        print(postBody)
        print(request.FILES)
        picture_obj = request.FILES.get('file')
        path = 'PaiLiTao_backend/img/'+picture_obj.name
        with open(path,'wb') as f:
            for content in picture_obj.chunks():
                f.write(content)
        var1 = path
    return HttpResponse('OK')
