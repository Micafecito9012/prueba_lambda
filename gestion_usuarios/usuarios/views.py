from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import LoginForm, RegistrationForm
from .models import User


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('user_list')
    else:
        form = LoginForm()
    return render(request, 'usuarios/login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.rol = 'user'  # Por defecto el rol es "user"
            user.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'usuarios/register.html', {'form': form})


@login_required
@user_passes_test(lambda u: u.rol == 'admin', login_url='/forbidden/')
def user_list(request):
    users = User.objects.all()
    return render(request, 'usuarios/user_list.html', {'users': users})


@login_required
@user_passes_test(lambda u: u.rol == 'admin', login_url='/forbidden/')
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = RegistrationForm(instance=user)
    return render(request, 'usuarios/edit_user.html', {'form': form, 'user': user})
