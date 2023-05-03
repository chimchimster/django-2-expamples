from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostSitemap
from .feeds import LatestPostFeed

app_name = 'blog'

sitemaps = {'post': PostSitemap,}

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('feed/', LatestPostFeed(), name='post_feed'),
    path('search/', views.post_search, name='post_search'),
]
