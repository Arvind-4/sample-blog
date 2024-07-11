from django.urls import path

from blog.views import (
    blog_create_view,
    blog_list_view,
    blog_detail_view,
    blog_edit_view,
    blog_delete_view,
    blog_published_view,
)

app_name = "blog"

urlpatterns = [
    path("create/", blog_create_view, name="blog_create_view"),
    path(
        "",
        blog_list_view,
        name="blog_list_view",
    ),
    path(
        "detail/<int:id>/",
        blog_detail_view,
        name="blog_detail_view",
    ),
    path(
        "edit/<int:id>/",
        blog_edit_view,
        name="blog_edit_view",
    ),
    path(
        "delete/<int:id>/",
        blog_delete_view,
        name="blog_delete_view",
    ),
    path(
        "published/",
        blog_published_view,
        name="blog_published_view",
    ),
]
