from django.db import models


class Support(models.Model):
    name = models.CharField(max_length=78)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name = 'پشتبانی'
        verbose_name_plural = "پشتبانی"

    def __str__(self):
        return f'{self.name}<::>{self.email}'
