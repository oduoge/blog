from django.shortcuts import render

from django.http import HttpRequest
from django.http import HttpResponseRedirect


# Create your views here.
#
# def index(request):
#     return HttpResponse("Hello, blog")
from blog.db_query import DbHandle
from blog.models import user

from .forms import LoginForm, LoginModel


def index(request):
    db_handle = DbHandle(model='blog_user', database='db_blog')
    latest_meta_list = db_handle.all(order='last_login_date')
    print(latest_meta_list)
    results = [user.tran(ele) for ele in latest_meta_list]

    context = {
        'latest_meta_list': results,
    }
    return render(request, 'blog/index.html', context)


def query(request):
    user_email = request.GET.get('email')
    user_pwd = request.GET.get('password')

    return render(request, 'home.html', None)


def home(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/')
    else:
        form = LoginForm()

    return render(request, 'blog/name.html', {'form': form})


def login(request):
    if request.method == 'POST':
        print("hhe")
        print(request.POST)
        form = LoginModel(request)
        if form.is_valid():
            print(request)
            user_email = form.email
            user_pwd = form.password
            context = {
                'user_email': user_email,
                'user_pwd': user_pwd,
            }
            print(user_email)
            return render(request, 'blog/login/home.html', context)
    else:
        form = LoginForm()
        print("no!!")

    return render(request, 'login.html')