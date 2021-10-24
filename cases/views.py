from django.shortcuts import render, redirect
from .models import Case # Case model

from django.views.generic import ListView, DetailView,TemplateView


# Create your views here.

def list(request): # case list를 요청하기 위한 함수
    case_all = Case.objects.all()
    context = {
        'case_all': case_all
        }
    return render(request, 'list.html', context)

def detail(request, id): # list의 case detail을 요청하기 위한 함수
    case = Case.objects.get(id=id) # Case 모델의 특정값을 조회하여 case 변수에 할당
    context = {'case' : case} #응답을 위한 context 변수 생성
    print('case',case)
    return render(request, "detail.html", context) # 요청에 대한 응답



# def filter(request, keyword1):
#     keyword1 = Case.objects.get(keyword1=keyword1)
#     context = {'keword1' : keyword1}
#     return render(request, 'list.html', context)