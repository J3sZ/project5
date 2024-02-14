from django.views.generic import ListView
from .models import post

# Create your views here.

class BlogListview(ListView):
    model = post
    template_name = "home.html"
