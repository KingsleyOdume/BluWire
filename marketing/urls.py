from django.urls import path
from .views import email_list_signup

urlpatterns = [
    path('email-signup/', email_list_signup, name='email-list-signup'),
]
