from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dishes/', views.dishes, name='dishes'),
    path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/<int:id>/ingredients/', views.recipe_ingredients, name='recipe_ingredients'),
    path('recipe/<int:id>/steps/', views.recipe_steps, name='recipe_steps'),
]
