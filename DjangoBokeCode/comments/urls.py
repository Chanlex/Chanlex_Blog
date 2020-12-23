# 陈同学学习站
# 学习时间：2020/12/19 21:28
from django.urls import path

from . import views

app_name = 'comments'
urlpatterns = [
    path('comment/<int:post_pk>', views.comment, name='comment'),
]
