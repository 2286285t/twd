from django.shortcuts import render
from django.http import HttpResponse
# Import the Category model
from rango.models import Category
from rango.models import Page

def index(request):
    # Query the database for a lsit of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary
    # that will be passed to the template engine.

    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list, 'pages': page_list}

    # Render the response and send it back!
    return render(request, 'rango/index.html', context_dict)
  #  return HttpResponse("Rango says hey there partner! <br/> <a href='/rango/about/'>About</a>" )


def about(request):
    #context_dict = {'boldmessage': "This tutorial has been put together by Stephen Taylor"}
    return render(request, 'rango/about.html')
   # return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a> ")

def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)

        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context_dict)
