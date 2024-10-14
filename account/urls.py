from django.urls import path
from .views import *

urlpatterns = [
    path('login/',login_page,name="login"),
    path('logout/',logout_page,name="logout"),
    path('signup/<email>',register_page,name="register"),
    path('forgot-password/',forgot_page,name="forgot-page"),
    path('reset-password/<email_token>',reset_password,name="password-reset-page"),
    path('email-verification-message/<email>',email_verification_message),
    path('activate-email/<email_token>',activate_email,name="activate-email"),
    path('subscription/',subscription_page,name="subscription-page"),
    path('payment/',payment_page,name="payment-page"),
    path('payment/payment-info/',payment_info,name="payment-info"),
    path('profile/',profile_page,name="profile-page"),
    path('profile/<str:profile_id>/',profileRedirector,name="profile-redirector"),
]   