from django.db import models
from ckeditor.fields import RichTextField

class Home(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    subject = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='about', blank=True, null=True)
    image2 = models.ImageField(upload_to='about', blank=True, null=True)
    # AboutUs
    description = RichTextField(blank=True, null=True)
    # Support
    text = RichTextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)

    def __str__(self):
        return self.title