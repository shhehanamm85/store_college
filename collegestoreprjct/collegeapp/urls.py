from django.urls import path
from.import views
urlpatterns = [

    path('',views.home,name='home'),
    path('btn-click/',views.btn_click,name='btn_click'),
    path('login/',views.login,name='login'),
    path('re_reg/', views.re_reg, name='rereg'),
    path('reg/', views.reg, name='reg'),

    path('register/', views.register, name='register'),
    path('form', views.form, name='form'),
    path('logout',views.logout,name='logout'),

]