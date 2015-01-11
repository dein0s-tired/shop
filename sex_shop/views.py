from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext, loader

from sex_shop.models import News, Category, Product


def index(request):
    news_list = News.objects.order_by('publish_date')
    categories_list = Category.objects.all()
    paginator = Paginator(news_list, 5)
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    # context = {'news_list': news_list}
    return render_to_response('sex_shop/index.html', {'news': news, 'categories_list': categories_list})
    # return render(request, 'sex_shop/index.html', context)


def categories(request):
    categories_list = Category.objects.filter()
    return HttpResponse("You're at the categories page.")


def category(request, category_id):
    category_item = get_object_or_404(Category, pk=category_id)
    empty = False if Product.objects.exclude(available_count=0).filter(category=category_id) else True
    if not empty:
        return render(request, 'sex_shop/category.html', {'category': category_item})
    else:
        return HttpResponse('EMPTY')