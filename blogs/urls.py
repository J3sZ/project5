from django.urls import path
from .views import BlogListview, BlogDetailView, BlogCreateView
urlpatterns = [
    path("", BlogListview.as_view(), name="home"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name= "post_detail" ),
    path("post/new/", BlogCreateView.as_view(), name="create_post" ),
]