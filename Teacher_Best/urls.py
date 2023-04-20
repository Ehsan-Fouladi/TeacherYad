from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth.urls import path
from . import settings
from templates.admin import views

urlpatterns = [
    path('admin/login/', views.LoginView.as_view()),
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path('accounts/' , include('django.contrib.auth.urls')),
    path('account/', include("account.urls")),
    path('articles/', include("post.urls")),
    path('hitcount/', include('hitcount.urls', namespace='hitcount')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
