from django.urls import include, path,re_path
from . import views
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns=[
    path('',views.blogs_today,name = 'blogsToday'),
    re_path('archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_blogs,name = 'pastBlogs'),
    re_path('search/', views.search_results, name='search_results')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)