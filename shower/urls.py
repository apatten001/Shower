from django.urls import path
from .views import RegisterFormView


app_name = 'shower'
urlpatterns = [
    path('register/', RegisterFormView.as_view(), name='shower')


]

