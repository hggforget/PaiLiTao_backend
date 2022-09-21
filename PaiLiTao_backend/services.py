import json
from tkinter import StringVar

from django.http import *
from django.shortcuts import render
from django.views.generic import TemplateView

from PaiLiTao_backend.utils.FP import *

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
        var2=r'C:/Users/HDC/Desktop'
        var1=r'D:/PaiLiTao_backend/'+path
        var3=int(request.POST.get('rate'))
        img_list=start(var1,var2,var3)
        context={}
        context['imgs']=img_list
    return JsonResponse(context)
