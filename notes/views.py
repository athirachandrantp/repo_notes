from django.shortcuts import render, redirect
from .models import Mynotes
from .forms import Notesform
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


# Create your views here.

def login_notes(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('notes')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'not a valid user')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('notes')
        else:
            print('not correct')
    context = {'page': page}
    return render(request, 'notes/registration.html', context)

def logout_notes(request):
    logout(request)
    return redirect('login')

def register_notes(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'user created')
            login(request, user)
            return redirect('notes')
        else:
            messages.success(request, 'an error occured')
    context = {'page': page, 'form': form}
    return render(request, 'notes/registration.html', context)


@login_required(login_url='login')
def notes(request):
    notes = Mynotes.objects.all().order_by('-notes_date')
    context = {'notes': notes}
    return render(request, 'notes/notes.html', context)
@login_required(login_url='login')
def view_notes(request, pk):
    projectobj = Mynotes.objects.get(id=pk)
    return render(request, 'notes/view_notes.html', {'notes': projectobj})
@login_required(login_url='login')
def add_notes(request):
    profile = request.user
    form = Notesform()
    if request.method == 'POST':
        form = Notesform(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
                user = form.save(commit=False)
                user.owner = profile
                user.save()
                return redirect('notes')
    context = {'form': form}

    return render(request, 'notes/form.html', context)
@login_required(login_url='login')
def update_notes(request, pk):
    notes = Mynotes.objects.get(id=pk)
    form = Notesform(instance=notes)
    if request.method == 'POST':
        form = Notesform(request.POST, request.FILES, instance=notes)
        if request.user == notes.owner:
            if form.is_valid():
                form.save()

            return redirect('notes')
        else:
            messages.error(request, 'not a valid user')

    context = {'form': form}
    return render(request, 'notes/form.html', context)

@login_required(login_url='login')
def delete_notes(request, pk):
    notes = Mynotes.objects.get(id=pk)
    if request.user == notes.owner:
        # if request.user.is_authenticated:
        # print('success')
        notes.delete()
        return redirect('notes')
    else:
        messages.error(request, 'not a valid user')

    context = {'notes': notes}
    return render(request, 'notes/delete_notes.html', context)

@login_required(login_url='login')
def user_page(request):
    user = request.user
    context = {'user': user, 'details': user}
    return render(request, 'notes/user_page.html', context)
