import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from polls.form import TransactionForm
from polls.models import Transaction


def index(request):
    user = User.objects.all()
    alert = ''
    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')

        loginUser = authenticate(request, username=username, password=password)
        if loginUser:
            login(request, loginUser)
            return redirect('main')
        else:
            alert = 'password is Incorrect'
    context = {
        'user': user,
        'alertText': alert
    }
    return render(request, 'index.html', context=context)


@login_required
def FormShow(request):
    user = request.user
    current = datetime.date.today()
    if (request.method == 'POST'):
        form = TransactionForm(request.POST)
        if (form.is_valid()):
            Transaction.objects.create(
                create_by=user,
                reason=form.cleaned_data.get('reason'),
                type=form.cleaned_data.get('type'),
                start_date=form.cleaned_data.get('start_date'),
                end_date=form.cleaned_data.get('end_date')

            )
            return redirect('main')
    else:
        form = TransactionForm
    context = {
        'form': form
    }
    print(user.first_name)
    return render(request, 'Form.html', context=context)


@login_required
def MainPage(request):
    user = request.user
    transaction = Transaction.objects.filter(create_by=user)
    context = {
        'transcation': transaction
    }
    return render(request, 'main.html', context=context)


def logouting(request):
    logout(request)
    return redirect('index')