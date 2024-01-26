from django.urls import path
from. import views

urlpatterns = [
    path('UserRegisterApi/', views.UserRegisterApi),
    # path('', views.index , name='index'),
]