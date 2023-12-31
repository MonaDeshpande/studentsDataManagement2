from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
  path('', views.home, name="home"),
  path('home', views.home, name="home"),
  path('add_student', views.add_student, name="add_student"),
  path('delete_student/<int:unique_no>', views.delete_student, name="delete_student"),
  path('signup', views.signup, name="signup"),
  path('signin', views.signin, name="signin"),
  path('signout', views.signout, name="signout"),
]
