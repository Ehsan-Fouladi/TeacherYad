from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView
from .forms import LoginForm



# Login user
class LoginView(FormView):
    template_name = 'admin/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('admin:index')

    def form_valid(self, form):
        cd = form.cleaned_data
        user = authenticate(self.request, username=cd['email'] , password=cd['password'])
        if user is not None:
            login(self.request, user)
            messages.success(self.request, 'شما با موفقیت وارد سایت شدید')
            return redirect(reverse_lazy('admin:index'))
        else:
            form.add_error("email", "اطلاعات شما نادرست است؟")
            return render(self.request, "admin/login.html", {"form": form})