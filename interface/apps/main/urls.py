from django.urls import re_path

from . import views

app_name = "main"

urlpatterns = [  
    re_path(r"^$", views.user_login, name="user_login"),  
    re_path(r"^registration/$", views.user_registration, name="user_registration"),
    re_path(r"^password-recovery/$", views.user_password_recovery, name="user_password_recovery"),
    re_path(r"^password-recovery/(?P<password_recovery_key>\w+)", views.user_password_recovery__set_new_password, name="user_password_recovery__set_new_password"),
    re_path(r"^logout/$", views.user_logout, name="user_logout"),
    # lesson3 
    re_path(r"^test/(?P<named_group>\w+)/$", views.test, name="test"),
    # lesson5
    re_path(r"^template-render/$", views.template_render, name="template_render"),
]
