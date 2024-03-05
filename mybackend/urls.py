from django.urls import path
from . import views

urlpatterns = [
    path('UserRegisterApi/', views.UserRegisterApi),
    path('UserRegisterApi/<int:id>', views.OperationByOne),
    path('hello/', views.hello_world, name='hello-world'),
    path('BlogApi/', views.BlogApi),
]