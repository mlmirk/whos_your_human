from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name="home"),
  path('accounts/signup/', views.signup, name='signup'),
  path('about/', views.about, name="about"),
  path('pets/', views.pets_index, name="pets_index"),
  path("pets/<int:pet_id>/", views.pets_detail, name='pets_detail'),
  path('pets/create/', views.PetCreate.as_view(), name="pet_create")
]