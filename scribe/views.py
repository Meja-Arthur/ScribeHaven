from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'landing-page.html')


def about(request):
    return render(request, 'about-us.html')

def contact(request):
    return render(request, 'contact-us.html')

def profile(request):
    return render(request, 'profile-page.html')

def blog(request):
    return render(request, 'blog-post.html')

def blogPosts(request):
    return render(request, 'blog-posts.html')

def price(request):
    return render(request, 'pricing.html')

def signup(request):
    return render(request, 'signup-page.html')

def team(request):
    return render(request, 'team.html')