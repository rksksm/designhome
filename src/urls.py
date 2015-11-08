from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from . import views
from src.models import Post

urlpatterns = [
		url(r'^$',views.load, name = 'load'),
		url(r'^index',views.index, name = 'index'),
		url(r'^blog', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:100],template_name="blog.html")),
	
		]