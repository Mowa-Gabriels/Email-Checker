from django.shortcuts import redirect, render
from emailapp.models import *
from .forms import FormEmailAdd
from django.utils import timezone
from django.contrib import messages
import requests

# Create your views here.

def index(request):
    
    email_logs = EmailLog.objects.all()[4:]
    now = timezone.now

    context = {
       'email_logs': email_logs,
       'now': now,
    }

    return render(request, 'emailapp/welcome_page.html', context)

def email_add(request):

    form = FormEmailAdd()

    if request.method == 'POST':
        form = FormEmailAdd(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Details successfully Added')
            return redirect('email_list')
        else:
            messages.success(request,'Invalid Entry!')
            print(form.errors)
            form = FormEmailAdd()

    context = {
        'form': form,
    }

    return render(request, 'emailapp/add_email.html', context)


def email_list(request):

    email_logs = EmailLog.objects.all()

    context = {
       'email_logs': email_logs
    }

    return render(request, 'emailapp/email_list.html', context)

