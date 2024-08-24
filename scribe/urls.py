from django.urls import path
from . import views

app_name = 'scribe'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('profile/', views.profile, name='profile'),
    path('blog/', views.blog, name='blog'),
    path('blog-post/', views.blogPosts, name='post'),
    path('price/', views.price, name='price'),
    path('signup/', views.signup, name='signup'),
    path('team/', views.team, name='team'),
]