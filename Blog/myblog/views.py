from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Category
from .forms import PostForm,UpdateForm
from django.urls import reverse_lazy


class HomeView(ListView):
	model=Post
	template_name='home.html'
	ordering=['-post_date']
	# ordering=['-id']

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

class DeletePostView(DeleteView):
	model=Post
	template_name='delete_post.html'
	success_url=reverse_lazy("home")

class AddCategoryView(CreateView):
	model=Category
	template_name='add_category.html'
	fields='__all__'
	# form_class=CategoryForm

