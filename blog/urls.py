from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_listing, name='listing'),
    path('detail/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('see_request/', views.see_request, name='see_request'),
    path('user_info/', views.user_info, name='user_info'),
    path('privet_place/', views.privet_place, name='privet_place'),
    path('staff_place/', views.staff_place, name='staff_place'),
    path('add_messages/', views.add_messages, name='add_messages'),
]
