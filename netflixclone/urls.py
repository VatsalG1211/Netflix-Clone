from django.contrib import admin
from django.conf import settings
from django.urls import path,include,re_path
from django.conf.urls.static import static
from django.conf.urls import handler404
from django.shortcuts import render
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from account.views import index_page,profile_account,profile_account_delete
from content.views import home_page,mylist_page,search,tvshows_page,movies_page
from .views import custom_404_view,termsandconditions




# Set handler404 to use the custom function
handler404 = custom_404_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('account.urls')),
    path('',index_page,name="index"),
    path('browse/',home_page,name="home"),
    path('browse/tv-shows/',tvshows_page,name="tv-shows"),
    path('browse/movies/',movies_page,name="movies"),
    path('content/',include('content.urls')),
    path('mylist/',mylist_page,name="mylist-page"),
    path('search/<query>',search,name="search"),
    path('profile/account/',profile_account,name="profile-account"),
    path('profile/account/delete-profile/',profile_account_delete,name="profile-account-delete"),
    path('termsandconditions',termsandconditions,name="tandc"),
]

