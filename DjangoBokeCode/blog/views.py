from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count, Q
from django.shortcuts import render, get_object_or_404, redirect
import markdown
# Create your views here.
from django.shortcuts import render
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension

from .models import Post, Category, Tag


def index(request):
    # post_list = Post.objects.all().order_by('-created_time')
    # context = {
    #     'post_list': post_list
    # }
    # return render(request, 'blog/index.html',context=context)

    # 请求用户的文章列表
    post_list = Post.objects.filter(author=request.user)
    # 依据查询到的文章对象articles_list创建分页实例对象，并且规定每页最多5篇文章
    paginator = Paginator(post_list, 5)
    # 获得当前浏览器GET请求的参数page的值，也就是当前浏览器所请求的页面数值
    page = request.GET.get('page')
    try:
        # 用于得到指定页面的内容
        current_page = paginator.page(page)
        # 得到当前页的所有对象列表
        articles = current_page.object_list
    # 请求页码数值不是整数
    except PageNotAnInteger:
        current_page = paginator.page(1)
        articles = current_page.object_list
    # 请求页码数值为空或者在URL参数中没有page
    except EmptyPage:
        # paginator.num_pages返回的是页数
        current_page = paginator.page(paginator.num_pages)
        articles = current_page.object_list
    # 给前端渲染的数据是文章列表和当前页
    return render(request, 'blog/index.html', {"articles": articles, "page": current_page})

def detail(request, pk):
    # post = get_object_or_404(Post, pk=pk)
    # post.body = markdown.markdown(post.body,
    #                               extensions=[
    #                                   'markdown.extensions.extra',
    #                                   'markdown.extensions.codehilite',
    #                                   'markdown.extensions.toc',
    #                               ])
    # context={
    # 	'post': post
    # }
    # return render(request, 'blog/detail.html', context=context)

    post = get_object_or_404(Post, pk=pk)
    # 阅读量 +1
    post.increase_views()
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        TocExtension(slugify=slugify),
    ])
    post.body = md.convert(post.body)
    return render(request, 'blog/detail.html', {'post': post, 'toc': md.toc})

def archive(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    # context = {
    #     'post_list': post_list
    # }
    # return render(request, 'blog/index.html', context=context)

    # 依据查询到的文章对象articles_list创建分页实例对象，并且规定每页最多5篇文章
    paginator = Paginator(post_list, 5)
    # 获得当前浏览器GET请求的参数page的值，也就是当前浏览器所请求的页面数值
    page = request.GET.get('page')
    try:
        # 用于得到指定页面的内容
        current_page = paginator.page(page)
        # 得到当前页的所有对象列表
        articles = current_page.object_list
    # 请求页码数值不是整数
    except PageNotAnInteger:
        current_page = paginator.page(1)
        articles = current_page.object_list
    # 请求页码数值为空或者在URL参数中没有page
    except EmptyPage:
        # paginator.num_pages返回的是页数
        current_page = paginator.page(paginator.num_pages)
        articles = current_page.object_list
    # 给前端渲染的数据是文章列表和当前页
    return render(request, 'blog/index.html', {"articles": articles, "page": current_page})

def category(request, pk):
    # 记得在开始部分导入 Category 类
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    # return render(request, 'blog/index.html', context={'post_list': post_list})

    # 依据查询到的文章对象articles_list创建分页实例对象，并且规定每页最多5篇文章
    paginator = Paginator(post_list, 5)
    # 获得当前浏览器GET请求的参数page的值，也就是当前浏览器所请求的页面数值
    page = request.GET.get('page')
    try:
        # 用于得到指定页面的内容
        current_page = paginator.page(page)
        # 得到当前页的所有对象列表
        articles = current_page.object_list
    # 请求页码数值不是整数
    except PageNotAnInteger:
        current_page = paginator.page(1)
        articles = current_page.object_list
    # 请求页码数值为空或者在URL参数中没有page
    except EmptyPage:
        # paginator.num_pages返回的是页数
        current_page = paginator.page(paginator.num_pages)
        articles = current_page.object_list
    # 给前端渲染的数据是文章列表和当前页

    return render(request, 'blog/index.html', {"articles": articles, "page": current_page})

def tag(request, pk):
    # 记得在开始部分导入 Tag 类
    t = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=t).order_by('-created_time')
    # return render(request, 'blog/index.html', context={'post_list': post_list})

    # 依据查询到的文章对象articles_list创建分页实例对象，并且规定每页最多5篇文章
    paginator = Paginator(post_list, 5)
    # 获得当前浏览器GET请求的参数page的值，也就是当前浏览器所请求的页面数值
    page = request.GET.get('page')
    try:
        # 用于得到指定页面的内容
        current_page = paginator.page(page)
        # 得到当前页的所有对象列表
        articles = current_page.object_list
    # 请求页码数值不是整数
    except PageNotAnInteger:
        current_page = paginator.page(1)
        articles = current_page.object_list
    # 请求页码数值为空或者在URL参数中没有page
    except EmptyPage:
        # paginator.num_pages返回的是页数
        current_page = paginator.page(paginator.num_pages)
        articles = current_page.object_list
    # 给前端渲染的数据是文章列表和当前页
    return render(request, 'blog/index.html', {"articles": articles, "page": current_page})

def search(request):
    q = request.GET.get('q')
    if not q:
        error_msg = "请输入搜索关键词"
        messages.add_message(request, messages.ERROR, error_msg, extra_tags='danger')
        return redirect('blog:index')

    articles = Post.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))

    # 依据查询到的文章对象articles_list创建分页实例对象，并且规定每页最多5篇文章
    paginator = Paginator(articles, 5)
    # 获得当前浏览器GET请求的参数page的值，也就是当前浏览器所请求的页面数值
    page = request.GET.get('page')
    try:
        # 用于得到指定页面的内容
        current_page = paginator.page(page)
        # 得到当前页的所有对象列表
        articles = current_page.object_list
    # 请求页码数值不是整数
    except PageNotAnInteger:
        current_page = paginator.page(1)
        articles = current_page.object_list
    # 请求页码数值为空或者在URL参数中没有page
    except EmptyPage:
        # paginator.num_pages返回的是页数
        current_page = paginator.page(paginator.num_pages)
        articles = current_page.object_list

    return render(request, 'blog/index.html', {'articles': articles, "page": current_page})

def about(request):
    return render(request, 'blog/about.html')

def bkpage(request):
    return render(request, 'blog/bkpage.html')

def contact(request):
    return render(request, 'blog/contact.html')