from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.
def AllBlogs(request):
    Blogs = Blog.objects
    #We have to pass the Blogs as a key which can be used to access the value in html file.
    return render(request, 'Blog/AllBlogs.html',{'Blogs':Blogs})


#We can use the blog_id too retuen the data w.r.t to that blog id and show it in the browser
# if the blog_id doesn't matches with any of the blog_id in database it's going to throw 404 error
def detail(request,blog_id):
    detailblog = get_object_or_404(Blog,pk=blog_id)
    # detailblog will have the details wrt to the blog_id that we have triggered with the URL
    return render(request, 'Blog/Detail.html',{'Blog':detailblog})
