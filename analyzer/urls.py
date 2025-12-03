from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_resume, name='upload_resume'),
    path('analyze/', views.analyze_resume, name='analyze_resume'),
]
