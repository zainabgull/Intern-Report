from django.shortcuts import render, HttpResponse
from django import forms
from django.contrib.auth.decorators import login_required
from .models import Intern
from django.http import HttpResponseRedirect
from .forms import WorkSubmissionForm

def work_submission(request):
    print('in work submission function')
    if not request.user.is_authenticated:  # Check if the user is authenticated
        return render(request, 'login_required_alert.html')  # Render the alert template
    
    if request.method == 'POST':
        form = WorkSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')  # Redirect after successful submission
        
    else:
        form = WorkSubmissionForm()
    interns = Intern.objects.all()
    print('interns list ', interns)

    return render(request, 'home.html', {'form': form, 'interns': interns})

def success_form(request):
    if not request.user.is_authenticated:  # Check if the user is authenticated
        return render(request, 'login_required_alert.html')  # Render the alert template
    return render(request, 'success.html')