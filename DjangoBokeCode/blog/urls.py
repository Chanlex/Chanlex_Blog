from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:pk>/', views.detail, name='detail'),
    path('archives/<int:year>/<int:month>/', views.archive, name='archive'),
    path('categories/<int:pk>/', views.category, name='category'),
    path('tags/<int:pk>/', views.tag, name='tag'),
    path('search/', views.search, name='search'),#搜索
    path('about/',views.about,name='about'),#博客页面
    path('bkpage/',views.bkpage,name='bkpage'),#博客页面
    path('contact/',views.contact,name='contact'),#博客页面
]
