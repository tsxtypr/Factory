# Create your views here.
from django.shortcuts import HttpResponse,render
from .models import *
from django.core.paginator import Paginator

#首页
def index(request):
    products = Product.objects.all()
    return render(request,'index.html',locals())

#公司简介
def aboutus(request):
    products = Product.objects.all()
    return render(request,'aboutus.html',locals())

#产品中心
def product(request,page=1):
    #所有的产品信息
    products = Product.objects.all()

    #设置每页分几条
    paginator=Paginator(products,5)
    #这是具体的页对象
    page_obj=paginator.page(page)
    return render(request,'product.html',locals())

#技术咨询
def jszx(request):
    products = Product.objects.all()

    news=News.objects.all()
    return render(request,'jszx.html',locals())

#联系我们
def contact(request):
    products = Product.objects.all()
    return render(request,'contact.html',locals())

#地图接口
def map(request):
    return render(request,'map.html',locals())


#产品的详情
def product_info(request,id=1):

    info=Product.objects.get(id=id)
    return render(request,'product_info.html',locals())

#技术咨询的详情
def jszx_news(request,news_id=1):
    products = Product.objects.all()

    article=News.objects.get(id=news_id)

    # 文章总数
    articles_len = int(News.objects.all().count())
    end = articles_len + 1

    news_id=int(news_id)
    next_num=news_id+1
    privious_num=news_id-1
    if privious_num!=0:
        privious_article=News.objects.get(id=privious_num)
    if next_num!=end:
        next_article=News.objects.get(id=next_num)

    return render(request,'jszx_news.html',locals())
