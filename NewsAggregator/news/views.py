from django.http import HttpResponse
from .posts import NewsData
from django.shortcuts import render
from .models import Country, Category
import re


def create_context(request):
    if request.method == "POST":
        sel_countries = [re.search('\((\w\w)\)', item)[1] for item in request.POST.getlist('list_country')]
        sel_categories = request.POST.getlist('list_category')
        nd = NewsData(sel_countries, sel_categories)
    else:
        nd = NewsData()

    nd.get_data()
    posts = nd.data

    countries = Country.objects.all()
    categories = Category.objects.all()

    context = {
        'posts': posts,
        'countries': countries,
        'categories': categories,
    }

    return context


def home(request):
    context = create_context(request)
    return render(request, 'news/home.html', context)


def upload(request):
    return render(request, 'news/file.html', )


def uploadfile(request):
    if request.method == "POST":
        fl_name = request.POST.get('file_country').name
        print('test')
        print(fl_name)
        return HttpResponse(fl_name)

    return render(request, 'news/file.html',)


def about(request):
    return render(request, 'news/about.html')


def gonews(request):
    context = create_context(request)
    return render(request, 'news/home.html', context)


