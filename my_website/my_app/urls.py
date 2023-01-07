from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('user/register', views.register, name='register'),
    path('user/login', views.login, name='login'),
    path('user/logout', views.logout, name='logout'),
    path('user/forms', views.users, name='users'),
    path('user/view', views.view, name='view'),
    path('formdelete/<int:id>', views.delete),
    path('formupdate/<int:id>', views.update),
    path('updateform/<int:id>', views.updateform),
    path('header', views.header, name='header'),

]
