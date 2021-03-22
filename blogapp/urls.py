from django.urls import include, path,re_path
from . import views
from django.contrib import admin

urlpatterns=[
    path('',views.blogs_today,name = 'blogsToday'),
    re_path('archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_blogs,name = 'pastBlogs')
    
]