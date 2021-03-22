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



def search_results(request):

    if 'blog' in request.GET and request.GET["blog"]:
        search_term = request.GET.get("blog")
        searched_blogs = Blog.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"blogs": searched_blogs})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})