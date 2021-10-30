from django.shortcuts import render, redirect
from taggit.managers import TaggableManager
from taggit.models import Tag


from .models import Case # Case model

from django.views.generic import ListView, DetailView,TemplateView

# Create your views here.

def list(request): # case list를 요청하기 위한 함수
    case_all = Case.objects.all()
    tag = Tag.objects.all()
    
    # if tag.id == tag.ob
    # tag의 아이디와 Case의 아이디가 일치하는 경우에 그때 해당하는 tag.name 값을 가져온다. 그값을 context에 담아준다.
    # tag_id = Tag.objects.all(id=Case.id)
    context = {
        'case_all': case_all,
        'tag_all' : tag
         }
    return render(request, 'list.html', context)

def detail(request, id): # list의 case detail을 요청하기 위한 함수
    case = Case.objects.get(id=id) # Case 모델의 특정값을 조회하여 case 변수에 할당
    context = {'case' : case} #응답을 위한 context 변수 생성
    print('case',case)
    return render(request, "detail.html", context) # 요청에 대한 응답

class TagCloudTV(TemplateView):
    template_name = 'taggit/taggit_cloud.html'

class TaggedObjectLV(ListView):
    template_name = 'taggit/taggit_post_list.html'
    model = Case

    def get_queryset(self):
        return Case.objects.filter(tags_name=self.kwargs.get('tag'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context


# def filter(request, keyword1):
#     keyword1 = Case.objects.get(keyword1=keyword1)
#     context = {'keword1' : keyword1}
#     return render(request, 'list.html', context)

# post = Post.objects.get(id=id)
# comment_list = Comment.objects.filter(post=post) 
