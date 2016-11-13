from django.shortcuts import render


def home(request):
    return render(request, "SitePages/home.html", {"content": "Home page content"})


def about(request):
    return render(request, "SitePages/about.html", {"content": "About page content"})


def contact(request):
    return render(request, "SitePages/contact.html", {"content": "Contact page content"})
