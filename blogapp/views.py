from django.shortcuts import render,redirect
import datetime as dt
from django.http  import HttpResponse,Http404
from .models import Blog

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def blogs_today(request):
    date = dt.date.today()
    blogs = Blog.todays_blogs()
    return render(request, 'today-blogs.html', {"date": date,"blogs":blogs})

"""
added function to present blogs from past days.
"""

def past_days_blogs(request, past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(blogs_today)

    blogs = Blog.days_blogs(date)
    return render(request, 'past-blogs.html',{"date": date,"blogs":blogs})