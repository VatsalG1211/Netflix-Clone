from django.urls import path
from .views import *
urlpatterns = [
    path('<c_type>/<int:video_id>',content_page,name="video_page"),
    path('get_episodes/<c_id>',get_episodes,name="get_episodes"),
    path('get_content/<c_id>',get_content,name="get_content"),
    path('add_my_list/',add_my_list,name="add_my_list"),
    path('add_like/',add_liked_list,name="add_liked_list"),
    
    
    
]   