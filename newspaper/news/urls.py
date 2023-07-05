from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('<int:pk>', views.PostDetail.as_view(), name='post_detail'),
    path('search/', views.PostSearch.as_view(), name='post_search'),
    path('create/', views.PostCreate.as_view(), name='post_create'),
    path('<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
    path('author/', views.PostAuthor.as_view(), name='author_posts'),
    path('categories/<int:pk>', views.CategoryList.as_view(), name='category_list'),
]
