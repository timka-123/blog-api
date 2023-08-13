from django.urls import path

from .views import all_posts

urlpatterns = [
    path("posts", all_posts)
]
