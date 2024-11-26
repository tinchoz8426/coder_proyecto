from django.urls import path

from app_coder import views

urlpatterns = [
    path("pagina-inicio/", views.inicio),
    path('cursos/', views.cursos),
    path('profesores/', views.profesores),
    path('estudiantes/', views.estudiantes),
    path('entregables/', views.entregables),
]