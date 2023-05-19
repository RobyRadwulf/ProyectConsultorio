from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('registerA/', views.assistant_register, name='assistant_register'),
    path('registerN/', views.nutritionist_register, name='nutritionist_register'),
    path('registerC/', views.client_register, name='client_register'),
    path('consult/', views.Consult, name='consult'),
    path('client_info/<int:client_id>/', views.patient_details, name='client_info'),
    path('patient_status/', views.patient_progress, name='patient_status'),
]
