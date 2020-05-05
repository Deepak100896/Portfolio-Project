from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllBlogs, name='AllBlogs'),
    path('<int:blog_id>/',views.detail,name='detail'),
]
