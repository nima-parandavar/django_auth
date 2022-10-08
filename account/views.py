from django.shortcuts import render, redirect, reverse
from .forms import RegisterForm, RegisterProfileForm, LoginForm
from django.http import HttpRequest
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required


# Create your views here.


def register_user(request: HttpRequest):
    if request.method == "POST":
        """Register user"""
        form = RegisterForm(request.POST)
        # form = UserCreationForm()
        profile_form = RegisterProfileForm(request.POST, files=request.FILES)
        if form.is_valid() and profile_form.is_valid():
            cd = form.cleaned_data
            pcd = profile_form.cleaned_data

            user: User = form.save(commit=False)
            # user.set_password(cd['password'])
            # user.save()

            profile = Profile.objects.get(user=user)
            profile.photo = pcd['photo']
            profile.birth_date = pcd['birth_date']
            profile.bio = pcd['bio']
            profile.phone_number = pcd['phone_number']
            profile.save()

            return HttpResponse("Created")

    else:
        form = RegisterForm()
        # form = UserCreationForm()
        profile_form = RegisterProfileForm()

    context = {
        'form': form, 'profile_form': profile_form
    }
    return render(request, 'account/register_user.html', context)


@login_required
def user_account(request: HttpRequest):
    return render(request, 'account/user_account.html')

# def login_user(request: HttpRequest):
#     msg = None
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             username = cd['username']
#             password = cd.get('password')
#
#             try:
#                 user: User = User.objects.get(username=username)
#                 if user.check_password(password):
#                     login(request, user=user)
#                     return HttpResponse("user login")
#                 else:
#                     msg = 'password is wrong'
#             except User.DoesNotExist:
#                 msg = "user does not exist"
#
#     form = LoginForm()
#     context = {
#         'form': form,
#         'msg': msg
#     }
#     return render(request, 'account/login.html', context)
#
#
#
# def login_user(request: HttpRequest):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST, request=request)
#         if form.is_valid():
#             user: User = form.get_user()
#             login(request, user=user)
#             return redirect('user_account')
#
#     form = AuthenticationForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'account/login.html', context)
#
#
# def logout_user(request: HttpRequest):
#     logout(request=request)
#     return redirect('core:index')
#
