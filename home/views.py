from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Support
from teacher.models import Teacher
from aboutus.models import Home
from django.contrib import messages

class HomeView(ListView):

    def get(self, request):
        about = Home.objects.all()
        teacher = Teacher.objects.all()
        return render(request, 'home/index.html', {'about': about, 'teacher': teacher})

    def post(self, request):
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            Support.objects.create(name=name, email=email, message=message)
            messages.success(self.request, "!درخواست شما با موفقیت ثبت شد")
            return redirect("home:home")