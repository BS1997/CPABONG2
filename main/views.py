from django.shortcuts import render

# Create your views here.
def cpabong_main(request):
    
    return render(request, 'main/home.html')