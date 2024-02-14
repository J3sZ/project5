from django.urls import path
from .views import BlogListview
urlpatterns = [
    path("", BlogListview.as_view(), name="home"),
]