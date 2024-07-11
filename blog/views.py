from django.shortcuts import render, get_object_or_404, redirect

from blog.models import Blog
from blog.forms import BlogForm

from django.http import HttpRequest

# Create your views here.


def blog_create_view(request: HttpRequest):
    form = BlogForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("blog:blog_list_view")
    return render(request, "blog/blog_create.html", {"form": form})


def blog_list_view(request):
    objs = Blog.objects.all().order_by("-created_at")
    return render(request, "blog/blog_list.html", {"objs": objs})


def blog_detail_view(request: HttpRequest, id: str):
    obj = get_object_or_404(Blog, id=id)
    if request.method == "POST":
        comment = request.POST.get("comment")
        obj.comments.create(comment=comment)
        obj.save()
        return redirect("blog:blog_detail_view", id=id)
    return render(request, "blog/blog_detail.html", {"obj": obj})


def blog_edit_view(request: HttpRequest, id: str):
    form = BlogForm(data=request.POST or None, instance=get_object_or_404(Blog, id=id))
    if form.is_valid():
        form.save()
        return redirect("blog:blog_list_view")
    return render(request, "blog/blog_edit.html", {"form": form})


def blog_delete_view(request: HttpRequest, id: str):
    obj = get_object_or_404(Blog, id=id)
    obj.delete()
    return redirect("blog:blog_list_view")


def blog_published_view(request: HttpRequest):
    objs = Blog.objects.filter(draft=False).order_by("-created_at")
    return render(request, "blog/blog_draft_list.html", {"objs": objs})