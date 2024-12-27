from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('document_list')  # 로그인 후 리다이렉트할 페이지
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'members/login.html')

def logout_view(request):
    logout(request)
    return redirect('document_list')  # 로그아웃 후 리다이렉트할 페이지