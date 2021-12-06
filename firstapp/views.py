# coding=utf-8
from django.shortcuts import render, HttpResponse
from firstapp.models import people, article
from django.template import Context, Template
from django import forms
from django.http import HttpResponseRedirect


class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=50)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    email = forms.EmailField(label='邮箱')
    phone = forms.CharField(label='手机号', max_length=11)


def first_web(request):
    context = {}
    article_list = article.objects.all()
    context['article_list'] = article_list
    index_page = render(request, 'first_web.html', context)
    return index_page


def regist(request):
    errors = []
    confirm_password = None
    username = None
    password = None
    email = None
    phone = None
    judge = False
    if request.method == 'POST':
        if not request.POST.get('username'):
            errors.append('用户名不能为空')
        else:
            username = request.POST.get('username', False)
        if not request.POST.get('password'):
            errors.append('密码不能为空')
        else:
            password = request.POST.get('password', False)
        if not request.POST.get('confirm_password'):
            errors.append('第二次密码不能为空')
        else:
            confirm_password = request.POST.get('confirm_password', False)
        if not request.POST.get('email'):
            errors.append('email不能为空')
        else:
            email = request.POST.get('email', False)
        if not request.POST.get('phone'):
            errors.append('手机号不能为空')
        else:
            phone = request.POST.get('phone', False)
        if password == confirm_password:
            judge = True
        else:
            errors.append('两次密码不一致')
        if username is not None and password is not None and confirm_password is not None and email is not None and phone is not None and judge:
            if people.objects.filter(username=username):
                errors.append('该用户名已被注册')
            elif people.objects.filter(email=email):
                errors.append('该邮箱已被注册')
            else:
                registAdd = people.objects.create(username=username, password=password, email=email, phone=phone)
                errors.append('注册成功！')
    return render(request, 'regist.html', {'errors': errors})


def find(request):
    errors = []
    confirm_password = None
    username = None
    newpassword = None
    email = None
    phone = None
    judge = False
    if request.method == 'POST':
        if not request.POST.get('username'):
            errors.append('用户名不能为空')
        else:
            username = request.POST.get('username', False)
        if not request.POST.get('newpassword'):
            errors.append('密码不能为空')
        else:
            newpassword = request.POST.get('newpassword', False)
        if not request.POST.get('confirm_password'):
            errors.append('第二次密码不能为空')
        else:
            confirm_password = request.POST.get('confirm_password', False)
        if not request.POST.get('email'):
            errors.append('email不能为空')
        else:
            email = request.POST.get('email', False)
        if not request.POST.get('phone'):
            errors.append('手机号不能为空')
        else:
            phone = request.POST.get('phone', False)
        if newpassword == confirm_password:
            judge = True
        else:
            errors.append('两次密码不一致')
        if username is not None and newpassword is not None and confirm_password is not None and email is not None and phone is not None and judge:
            if people.objects.filter(username=username, email=email, phone=phone):
                people.objects.filter(username=username, email=email, phone=phone).update(password=newpassword)
                errors.append('修改成功！')
    return render(request, 'find.html', {'errors': errors})


def index(request):
    errors = []
    if request.method == 'POST':
        context = {}
        article_list = article.objects.all()
        context['article_list'] = article_list
        if not request.POST.get('username'):
            errors.append('用户名不能为空')
        else:
            user = request.POST.get('username')
        if not request.POST.get('password'):
            errors.append('密码不能为空')
        else:
            pwd = request.POST.get('password')
        #import psycopg2
        #conn = psycopg2.connect(database='Sakuzyo', user='postgres', password ='jkl1314',host='localhost', port='5432')
        #curs = conn.cursor()
        #curs.execute("select * from pg_tables")
        #tablename = curs.fetchall()[0][1]
        #curs.execute(f"select * from \"{tablename}\"")
        #data = curs.fetchall()
        # print(data)
        #if user == data[0][0] and pwd == data[0][1]:
        #    return render(request, 'first_web.html', context)
        #else:
        #    errors.append('用户名或密码错误,请重新登录')
        person = people.objects.filter(username__exact=user, password__exact=pwd)
        if person:
            return render(request, 'first_web.html', context)
        else:
            errors.append('用户名或密码错误,请重新登录')
    return render(request, 'index.html', {'errors': errors})

# Create your views here.
