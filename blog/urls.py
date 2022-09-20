from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.listing, name='listing'),
    path('detail/<int:pk>/', views.blog_detail, name='detail'),
]
