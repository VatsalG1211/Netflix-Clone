from django.core.mail import send_mail
from .models import *
from django.urls import reverse
from django.conf import settings

def send_email_activation_link(email,email_token):

    subject = "Activation link of Your Account"
    link = reverse("activate-email",kwargs={'email_token':email_token})
    full_link = f"http://127.0.0.1:8000{link}"
    body = f"You need to click on this link to activate your account :\n{full_link}"
    from_email = settings.EMAIL_HOST_USER

    
    send_mail(subject,body,from_email,[email])

def send_password_reset_link(email,email_token):

    subject = "Password Reset link of Your Account"
    link = reverse("password-reset-page",kwargs={'email_token':email_token})
    full_link = f"http://127.0.0.1:8000{link}"
    body = f'''You need to click on this link to change password of your account :\n\n{full_link} 
    \n Link is Valid for 1 Minute Only 
    '''
    from_email = settings.EMAIL_HOST_USER

    

    send_mail(subject,body,from_email,[email])