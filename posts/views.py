from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models


class PostListView(ListView):
    model = models.Post
    template_name = 'post_list.html'
    paginate_by = 4


class PostDetailView(DetailView):
    model = models.Post
    template_name = 'post_detail.html'


class PostUpdateView(UpdateView):
    model = models.Post
    fields = ['news','content']
    template_name = 'post_edit.html'


class PostDeleteView(DeleteView):
    model = models.Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


class PostCreateView(CreateView):
    model = models.Post
    template_name = 'post_new.html'
    fields = ['news', 'author','content']


class LearnListView(ListView):
    model = models.Learn
    template_name = 'learn_list.html'
    paginate_by = 3


class LearnDetailView(DetailView):
    model = models.Learn
    template_name = 'learn_detail.html'


class LearnUpdateView(UpdateView):
    model = models.Learn
    fields = ['title', 'content',]
    template_name = 'learn_edit.html'


class LearnDeleteView(DeleteView):
    model = models.Learn
    template_name = 'learn_delete.html'
    success_url = reverse_lazy('learn_list')


class LearnCreateView(CreateView):
    model = models.Learn
    template_name = 'learn_new.html'
    fields = ['title', 'author', 'content']
