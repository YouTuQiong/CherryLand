import random
from .models import Article, Category as c, Tag as t, LikePhrase,f
from django.shortcuts import render, get_object_or_404
from django.db.models import F
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage


# Create your views here.
def index(request):
    post_list = Article.objects.all().order_by('-created_time')
    phrase = getphrase()
    paginator = Paginator(post_list, 6)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数，则展示第1页
        post_list = paginator.page(1)
    except EmptyPage:
        # 如果page超过范围，则展示最后一页
        post_list = paginator.page(paginator.num_pages)
    query_params = request.GET.copy()
    query_params.pop('page', None)  # delete page param
    return render(request, 'index.html', context={'page': page,
                                                  'paginator': paginator,
                                                  'query_params': query_params,
                                                  'post_list': post_list,
                                                  'phrase': phrase,
                                                  })


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    article.views = F('views') + 1
    article.save()
    article = get_object_or_404(Article, pk=pk)
    s = article.tags.all()
    return render(request, 'detail.html', context={'Article': article,
                                                   'phrase': getphrase()
                                                   })


def archives(request):
    post_list = Article.objects.all().order_by('-created_time')
    datalist = Article.objects.datetimes('created_time', 'year', 'DESC')
    datalist = reversed(datalist)
    count = len(post_list)
    dataContentlist = []
    for i in datalist:
        dataContentlist.append(i.year)
        dataContentlist.append(Article.objects.filter(created_time__year=str(i.year)))
    paginator = Paginator(dataContentlist, 6)
    page = request.GET.get('page')
    try:
        dataContentlist = paginator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数，则展示第1页
        dataContentlist = paginator.page(1)
    except EmptyPage:
        # 如果page超过范围，则展示最后一页
        dataContentlist = paginator.page(paginator.num_pages)
    query_params = request.GET.copy()
    query_params.pop('page', None)  # delete page param
    return render(request, 'Archive.html', context={'post_list': post_list,
                                                    'count': count,
                                                    'dataContentlist': dataContentlist,
                                                    'datalist': datalist,
                                                    'phrase': getphrase(),
                                                    'page': page,
                                                    'paginator': paginator,
                                                    'query_params': query_params,
                                                    })


def Category(request, pk):
    cate = get_object_or_404(c, pk=pk)
    post_list = Article.objects.filter(category=cate).order_by('-created_time')
    paginator = Paginator(post_list, 20)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数，则展示第1页
        post_list = paginator.page(1)
    except EmptyPage:
        # 如果page超过范围，则展示最后一页
        post_list = paginator.page(paginator.num_pages)
    query_params = request.GET.copy()
    query_params.pop('page', None)  # delete page param
    count = len(post_list)
    name = post_list[0].category.name
    return render(request, 'Category.html', context={'post_list': post_list,
                                                     'count': count, 'name': name,
                                                     'phrase': getphrase(),
                                                     'page': page,
                                                     'paginator': paginator,
                                                     'query_params': query_params,
                                                     })


def Tag(request, pk):
    cate = get_object_or_404(t, pk=pk)
    post_list = Article.objects.filter(tags=cate).order_by('-created_time')
    count = len(post_list)
    name = cate
    paginator = Paginator(post_list, 20)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数，则展示第1页
        post_list = paginator.page(1)
    except EmptyPage:
        # 如果page超过范围，则展示最后一页
        post_list = paginator.page(paginator.num_pages)
    query_params = request.GET.copy()
    query_params.pop('page', None)  # delete page param
    return render(request, 'Tag.html', context={'post_list': post_list,
                                                'count': count,
                                                'name': name,
                                                'phrase': getphrase(),
                                                'page': page,
                                                'paginator': paginator,
                                                'query_params': query_params,
                                                })


def reader(request):
    post_list = Article.objects.order_by('views')
    max = len(post_list)
    if (max > 11):
        post_list = post_list[max - 10:max]
    else:
        post_list = post_list[0:max]
    post_list = (reversed(post_list))
    return render(request, 'reader.html', context={'post_list': post_list,
                                                         'phrase': getphrase(),
                                                        })


def getphrase():
    phrase = list(LikePhrase.objects.all());
    phrasenum = len(phrase)
    nownum = int(random.randint(0, phrasenum))
    if(len(phrase)!=0):
        s = phrase[nownum - 1].phrase
    else:
        s=''
    return s


def about(request):
    return render(request, 'about.html', context={})


def mygays(request):
    post_list = f.objects.all()
    return render(request, 'mygays.html', context={"post_list",post_list})
