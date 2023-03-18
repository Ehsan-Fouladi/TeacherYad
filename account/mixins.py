from teacher.models import Teacher
from django.shortcuts import get_object_or_404, redirect, render


class FieldsUserMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_admin:
            self.fields = "__all__"
        elif request.user:
            self.fields = ["username", "name_field", "Foundation", "discription", "image"]
        else:
            return render(request, '404.html')
        return super(FieldsUserMixin, self).dispatch(request, *args, **kwargs)


class FormValidMixin():
    def form_valid(self, form):
        if self.request.user.is_admin:
            form.save()
        else:
            self.obj = form.save(commit=False)
            self.obj.user = self.request.user
            self.obj.is_teacher = None
        return super().form_valid(form)


class UpdateMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        teacher = get_object_or_404(Teacher, pk=pk)
        if teacher.user == request.user or request.user.is_admin:
            return super(UpdateMixin, self).dispatch(request, *args, **kwargs)
        else:
            return render(request, '404.html')



class SuperUserMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_admin:
            return super(SuperUserMixin, self).dispatch(request, *args, **kwargs)
        else:
            return render(request, '404.html')


class LoginRequirdMixins:
    def dispatch(self , request , *args , **kwargs):
        if request.user.is_authenticated == True:
            return redirect('home:home')
        return super(LoginRequirdMixins,  self ).dispatch(request , *args , **kwargs)
    
class LogoutRequirdMixins:
    def dispatch(self , request , *args , **kwargs):
        if request.user.is_authenticated == False:
            return redirect('home:home')
        return super(LogoutRequirdMixins ,  self ).dispatch(request , *args , **kwargs)
    
class TeacherRequirdMixins:
    def dispatch(self , request , *args , **kwargs):
        if request.user.is_teacher == False:
            return redirect('home:home')
        return super(TeacherRequirdMixins ,  self ).dispatch(request , *args , **kwargs)