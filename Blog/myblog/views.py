from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from .models import Post
from .forms import PostForm,UpdateForm


class HomeView(ListView):
	model=Post
	template_name='home.html'

class ArticaleDetailView(DetailView):
	model=Post
	template_name='articale_details.html'

class AddPostView(CreateView):
	model=Post
	form_class=PostForm
	template_name='add_post.html'
	# fields='__all__'
	# fields=('title','body')

class UpdatePostView(UpdateView):
	model=Post
	form_class=UpdateForm
	template_name='update_post.html'
	# fields=('title','body')

