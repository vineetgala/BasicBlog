from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from.models import post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class PostListView(ListView):
	model=post
	template_name= 'blog/home.html'
	context_object_name='posts'
	ordering=['-date_posted']


class PostCreateView(LoginRequiredMixin, CreateView):
	model=post
	fields=['title', 'content']

	def form_valid(self,form):
		form.instance.author=self.request.user
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
	model=post
	fields=['title', 'content']

	def form_valid(self,form):
		form.instance.author=self.request.user
		return super().form_valid(form)

	def test_func(self):
		Post=self.get_object()
		if self.request.user == Post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
	model=post
	success_url='/profile'

	def test_func(self):
		Post=self.get_object()
		if self.request.user == Post.author:
			return True
		return False

def home(request):
	return render(request, 'blog/home.html', {'posts':post.objects.all()})
def about(request):
	return render(request, 'blog/about.html', {'title':'About'})