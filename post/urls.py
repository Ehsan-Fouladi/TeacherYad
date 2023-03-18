from . import views
from django.urls import path


app_name = 'post'

urlpatterns = [
    path('list/', views.ListDetailView.as_view(), name='Detail'),
    path('<int:pk>/', views.DetailView.as_view(), name='user_Detail'),
    path('like/<int:id>/<int:pk>' , views.like , name='like'),
    path('Search/', views.SearchListView, name='search'),
]