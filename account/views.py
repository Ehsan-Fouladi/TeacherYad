from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, UpdateView, ListView, CreateView, DeleteView
from .forms import LoginForm, RegisterForm, ProfileForm
from .models import User
from .mixins import FieldsUserMixin, FormValidMixin, LoginRequirdMixins, LogoutRequirdMixins, TeacherRequirdMixins, UpdateMixin, SuperUserMixin
from teacher.models import Teacher


# Login user
class LoginView(LoginRequirdMixins , FormView):
    template_name = 'account/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('account:panel_user')

    def form_valid(self, form):
        cd = form.cleaned_data
        user = authenticate(self.request, username=cd['email'] , password=cd['password'])
        if user is not None:
            login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(self.request, 'شما با موفقیت وارد سایت شدید')
            return redirect(reverse_lazy('account:panel_user'))
        else:
            form.add_error("email", "اطلاعات شما نادرست است؟")
            return render(self.request, "account/login.html", {"form": form})


# Register user
class RegisterView(LoginRequirdMixins , FormView):
    template_name = 'account/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('account:panel_user')

    def form_valid(self, form):
        if self.request.user.is_authenticated == True:
            return redirect(reverse_lazy('account:panel_user'))
        else:
            cd = form.cleaned_data
            user = User.objects.create_user(email=cd['email'], is_teacher=cd['is_teacher'] , password=cd['password1'])
            login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(self.request, 'شما با موفقیت ثبت نام کرده اید')
            return redirect(reverse_lazy('account:panel_user'))


# panel update list
class ProfileView(LogoutRequirdMixins , UpdateView):
    success_url = reverse_lazy('account:panel_user')
    model = User
    form_class = ProfileForm
    template_name = 'account/profile.html'

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)


# panel view user
class PanelUserView(TeacherRequirdMixins , LogoutRequirdMixins , ListView):
    template_name = 'account/panel_user.html'

    def get_queryset(self):
        if self.request.user.is_admin:
            superusers = Teacher.objects.all()
            return superusers
        else:
            superuser = Teacher.objects.filter(user=self.request.user)
            return superuser


# panel edit article
class PanelEditView(TeacherRequirdMixins , LogoutRequirdMixins , FieldsUserMixin, FormValidMixin, CreateView):
    model = Teacher
    success_url = reverse_lazy('account:panel_user')
    template_name = 'account/panel_edit.html'


# panel update article
class PanelUpdate(TeacherRequirdMixins ,LogoutRequirdMixins , FieldsUserMixin, FormValidMixin, UpdateMixin, UpdateView):
    model = Teacher
    success_url = reverse_lazy('account:panel_user')
    template_name = 'account/panel_edit.html'


class PanelDelete(TeacherRequirdMixins , LogoutRequirdMixins , SuperUserMixin, DeleteView):
    model = Teacher
    success_url = reverse_lazy('account:panel_user')
    template_name = 'account/panel_delete.html'

def logout_view(request):
    logout(request)
    messages.success(request, "شما خارج شدید از سایت")
    return redirect("home:home")
