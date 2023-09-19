from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'landingPage.html')

def dashboard(request):
    return render(request,"homepage.html")
