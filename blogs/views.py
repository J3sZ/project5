from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView
from .models import post

# Create your views here.

class BlogListview(ListView):
    model = post
    template_name = "home.html"


class BlogDetailView(DetailView):
    model = post
    template_name = "post_detail.html"

class BlogCreateView(CreateView):
    model = post
    template_name = "new_post.html"
    fields = ["title", "author", "body"]

class BlogUptadeview(UpdateView):
    model = post
    template_name = "uptade.html"
    fields = [ "title", "body"]