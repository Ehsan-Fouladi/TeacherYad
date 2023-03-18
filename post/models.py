from django.db import models
from account.models import User
from teacher.models import Teacher
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f'{self.teacher.username} - {self.user.email}'

    class Meta:
        verbose_name = "لایک"
        verbose_name_plural = "لایک ها"
        ordering = ('-user',)
