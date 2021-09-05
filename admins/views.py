from django.shortcuts import render, HttpResponseRedirect
from users.models import User
from admins.forms import UserAdminRegistrationForm, UserProfileAdminForm
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test


# Create your views here.
@user_passes_test(lambda u: u.is_staff)
def index(request):
    data = {'title': 'Admin panel'}
    return render(request, 'admins/index.html', context=data)


@user_passes_test(lambda u: u.is_staff)
def admin_users(request):
    data = {'title': 'Users', 'users': User.objects.all()}
    return render(request, 'admins/admin-users.html', context=data)


@user_passes_test(lambda u: u.is_staff)
def admin_users_create(request):
    if request.method == 'POST':
        registration_form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if registration_form.is_valid():
            registration_form.save()
            messages.success(request, 'You have successfully registered')
            return HttpResponseRedirect(reverse('admins:admin_users'))
        else:
            print(registration_form.errors)
    else:
        registration_form = UserAdminRegistrationForm()
    context = {'title': 'Admin Registration page', 'form': registration_form}
    return render(request, 'admins/admin-users-create.html', context=context)


@user_passes_test(lambda u: u.is_staff)
def admin_users_update(request, id):
    selected_user = User.objects.get(id=id)
    if request.method == 'POST':
        profile_form = UserProfileAdminForm(instance=selected_user, data=request.POST, files=request.FILES)
        if profile_form.is_valid():
            profile_form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        profile_form = UserProfileAdminForm(instance=selected_user)
    data = {'title': 'User update', 'selected_user': selected_user, 'form': profile_form}
    return render(request, 'admins/admin-users-update-delete.html', context=data)


@user_passes_test(lambda u: u.is_staff)
def admin_users_delete(request, id):
    user = User.objects.get(id=id)
    user.safe_delete()
    return HttpResponseRedirect(reverse('admins:admin_users'))
