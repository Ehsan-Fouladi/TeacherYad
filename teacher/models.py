from django.db import models
from account.models import User
from django.utils.html import format_html
from jalali_date import datetime2jalali
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCount
class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_teacher', default=False)
    username = models.CharField(unique=True, max_length=100, verbose_name="نام")
    name_field = models.CharField(max_length=100, verbose_name="رشته تدریس")
    Foundation = models.CharField(max_length=15, verbose_name='پایه')
    entrance = models.CharField(max_length=20, verbose_name="رتبه کنکور", blank=True, null=True)
    teaching = models.CharField(max_length=50, verbose_name=" چندسال سابقه تدریس")
    discription = models.TextField(verbose_name="توضیحات کوتاه")
    image = models.ImageField(upload_to='Teacher', verbose_name="عکس")
    university = models.CharField(max_length=50, verbose_name="دانشگاه محل تحصیل")
    evidence = models.CharField(max_length=50, verbose_name="مدرک")
    view_resume = models.FileField(upload_to='CV', verbose_name="ارسال رزومه", blank=True, null=True)
    is_teacher = models.BooleanField(verbose_name='ایا معلم هست؟', blank=True, null=True)
    hit_count = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic')
    data_time = models.DateTimeField(auto_now_add=True)

    def shoe_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" height="50px" width="60px">')
        return format_html('<h3 style="color: red">تصویر موجود نیست</h3>')

    shoe_image.short_description = "عکس بند انگشتی"

    def __str__(self):
        return f"{self.is_teacher}/{self.username}"

    def get_jalali_data(self):
        return datetime2jalali(self.data_time).strftime('%Y/%m/%d _ %H:%M')

    class Meta:
        ordering = ("-name_field",)
        verbose_name = 'مدرس'
        verbose_name_plural = "معلم ها"