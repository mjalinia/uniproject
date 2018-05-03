from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),

    path('new/', views.PostCreateView.as_view(), name='post_new'),


    path('<int:pk>/edit/',
         views.PostUpdateView.as_view(), name='post_edit'), 
    path('<int:pk>/',
         views.PostDetailView.as_view(), name='post_detail'), 
    path('<int:pk>/delete/',
         views.PostDeleteView.as_view(), name='post_delete'),  

    path('learn/', views.LearnListView.as_view(), name='learn_list'),

    path('learn/<int:pk>/edit/',
         views.LearnUpdateView.as_view(), name='learn_edit'),

    path('learn/<int:pk>/', views.LearnDetailView.as_view(), name='learn_detail'),

    path('learn/<int:pk>/delete/',views.LearnDeleteView.as_view(), name='learn_delete'),

    path('new/', views.PostCreateView.as_view(), name='post_new'),

    path('learn/new/', views.LearnCreateView.as_view(), name='learn_new'),
]
