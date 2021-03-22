from django.shortcuts import render,redirect
import datetime as dt
from django.http  import HttpResponse,Http404

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def blogs_of_day(request):
    date = dt.date.today()
    return render(request, 'today-blogs.html', {"date": date,})

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
        return redirect(blogs_of_day)

    return render(request, 'past-blogs.html', {"date": date})