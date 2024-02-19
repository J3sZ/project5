from django.urls import path
from .views import BlogListview, BlogDetailView
urlpatterns = [
    path("", BlogListview.as_view(), name="home"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name= "post_detail" ),
]