from django.urls import path
from .views import *

urlpatterns=[
    path('index/',index,name="index"),
    path('add/',add,name="add"),
    path('dashboard/',dashboard,name="dashboard"),
    path('contact/', contact, name="contact"),
    path('signup/', signup, name="signup"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('detail/<int:pk>',detail,name='detail'),
    path('edit/<int:pk>', edititem, name='edit'),
    path('delete/<int:pk>',delete,name='delete')

]