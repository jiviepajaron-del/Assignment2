from django.shortcuts import render
from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def about(request):
    context = {"name": "Jivie Pajaron", "student_id": "2025-12711"}
    return render(request, "about.html", context)

# Create your views here.
