from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

app_name = 'core'

urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),
  path('register/', views.register, name='register'),
  path('login/', auth_views.LoginView.as_view(), name='login'),
  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
  path('account/', views.dashboard, name='dashboard'),
  path('recipes', views.RecipeView.as_view(), name='recipes'),
  path('categories/', views.GroupView.as_view(), name='categories'),
  path('recipe_set/', views.SearchResultView.as_view(), name='recipe_set'),
  path('posts/', views.PostsView.as_view(), name='posts'),
  path('add/', views.AddView.as_view(), name='add'),
  path('<slug:slug>/', views.SingleView.as_view(), name='single'),
  path('edit/<int:pk>/', views.EditView.as_view(), name='edit'),
  path('delete/<int:pk>/', views.Delete.as_view(), name='delete'),
]