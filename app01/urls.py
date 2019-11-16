from django.contrib import admin
from django.urls import path,re_path,include
from . import views


urlpatterns = [
    path('index/',views.index),
    path('aboutus/',views.aboutus),
    path('contact/',views.contact),
    path('jszx/',views.jszx),
    path('map/',views.map),
    path('product/',views.product),
    re_path('product/(?P<page>\d+)/',views.product),
    re_path(r'^$',views.index),
    path('product_info/',views.product_info),
    re_path('product_info/(?P<id>\d+)/',views.product_info),
    path('jszx_news/', views.jszx_news),
    re_path('jszx_news/(?P<news_id>\d+)/',views.jszx_news),

]