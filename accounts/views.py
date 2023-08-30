from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth import logout

def login_view(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('work_submission')  # Redirect to a success page
        else:
            error_message = "Invalid username or password. Please try again."
          
    return render(request, 'login.html', {'error_message': error_message})

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')  # Redirect to the login page
