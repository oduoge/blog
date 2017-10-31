from django.shortcuts import render

from django.http import HttpRequest
from django.http import HttpResponse


# Create your views here.
#
# def index(request):
#     return HttpResponse("Hello, blog")
from blog.db_query import DbHandle
from blog.models import user


def index(request):
    db_handle = DbHandle(model='blog_user', database='db_mysql')
    latest_meta_list = db_handle.all(order='last_login_time')
    print(latest_meta_list)
    results = [user.tran(ele) for ele in latest_meta_list]

    context = {
        'latest_meta_list': results,
    }
    return render(request, 'blog/index.html', context)
