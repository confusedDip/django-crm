from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    # path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    path('record/<int:pk>', views.view_record, name="record"),
    path('record/delete/<int:pk>', views.delete_record, name="delete"),
    path('record/add', views.add_record, name="add"),
]
