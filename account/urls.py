from . import views
from django .urls import path

app_name = 'account'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name="login"),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('Profile/user/', views.ProfileView.as_view(), name="profile"),
    path('Panel/user/', views.PanelUserView.as_view(), name="panel_user"),
    path('Panel/edit/', views.PanelEditView.as_view(), name="panel_edit"),
    path('Panel/update/<int:pk>', views.PanelUpdate.as_view(), name="panel_update"),
    path('Panel/Delete/<int:pk>', views.PanelDelete.as_view(), name="panel_Delete"),
    path('logout/', views.logout_view, name="logout"),
]