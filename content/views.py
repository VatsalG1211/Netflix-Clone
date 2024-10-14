from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.models import *
from .models import *
import random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from time import sleep
from django.http import JsonResponse

# Create your views here.


@login_required
def home_page(request):
    user = request.user
    baseuser = BaseUser.objects.get(user = user)
    if Subscription.objects.filter(baseuser = baseuser).exists():
        subscription = Subscription.objects.filter(baseuser = baseuser,is_plan_active= True)
        if not subscription:
            messages.warning(request,"Subscription has been Expired") 
            return redirect("subscription-page")
        else:
            profile_id = request.session.get('profile_id')
            if profile_id:
                profile = Profile.objects.get(profile_id = profile_id)

                seasons = Season.objects.all()
                movies = Movie.objects.all()
                popular_seasons = Season.objects.all()[0:10]
                popular_movies = Movie.objects.all()[0:10]

                

                
                season_banner_ad = random.choice(seasons)
                movie_banner_ad = random.choice(movies)

                c_type = ""

                choosed = random.randrange(0,2)
                banner_ad =None

                if choosed == 0:
                    banner_ad = season_banner_ad
                    c_type = "series"
                else:
                    banner_ad = movie_banner_ad
                    c_type = "movie"

                

                
                mylist =[]
                likedlist =[]

                
                
                if profile.content_list is not None:

                    added_content = profile.content_list.content.all()
                    for i in added_content:
                        mylist.append(i.c_id)

                
                if profile.liked_content is not None:

                    liked_content = profile.liked_content.content.all()

                    for i in liked_content:
                        likedlist.append(i.c_id)
                
                adult = True
                if profile.is_kid:
                    adult = False
                else:
                    adult = True


                context = {
                               'current_page':'home',
                               'adult':adult,
                               'profile':profile,
                               'c_type':c_type,
                               'seasons':seasons,
                               'popular_seasons':popular_seasons,
                               'movies':movies,
                               'popular_movies':popular_movies,
                               'banner_ad':banner_ad,
                               'mylist':mylist,
                               'likedlist':likedlist
                               }
                        
                
                return render(request,"content/home.html",context)
            else:
                return redirect("profile-page")
    else:
        return redirect("subscription-page")

def tvshows_page(request):
    user = request.user
    baseuser = BaseUser.objects.get(user = user)
    if Subscription.objects.filter(baseuser = baseuser).exists():
        subscription = Subscription.objects.filter(baseuser = baseuser,is_plan_active= True)
        if not subscription:
            messages.warning(request,"Subscription has been Expired") 
            return redirect("subscription-page")
        else:
            profile_id = request.session.get('profile_id')
            if profile_id:
                profile = Profile.objects.get(profile_id = profile_id)

                seasons = Season.objects.all()
                movies = Movie.objects.all()
                popular_seasons = Season.objects.all()[0:10]
                popular_movies = Movie.objects.all()[0:10]

                

                
               
                c_type = ""

                

                

                
                mylist =[]
                likedlist =[]

                
                
                if profile.content_list is not None:

                    added_content = profile.content_list.content.all()
                    for i in added_content:
                        mylist.append(i.c_id)

                
                if profile.liked_content is not None:

                    liked_content = profile.liked_content.content.all()

                    for i in liked_content:
                        likedlist.append(i.c_id)

                adult = True
                if profile.is_kid:
                    adult = False
                else:
                    adult = True


                context = {
                               'current_page':'home',
                               'adult':adult,
                               'profile':profile,
                               'c_type':c_type,
                               'seasons':seasons,
                               'popular_seasons':popular_seasons,
                               'movies':movies,
                               'popular_movies':popular_movies,
                               'mylist':mylist,
                               'likedlist':likedlist
                               }
                        
                
                return render(request,"content/tv-shows.html",context)
            else:
                return redirect("profile-page")
    else:
        return redirect("subscription-page")

def movies_page(request):
    user = request.user
    baseuser = BaseUser.objects.get(user = user)
    if Subscription.objects.filter(baseuser = baseuser).exists():
        subscription = Subscription.objects.filter(baseuser = baseuser,is_plan_active= True)
        if not subscription:
            messages.warning(request,"Subscription has been Expired") 
            return redirect("subscription-page")
        else:
            profile_id = request.session.get('profile_id')
            if profile_id:
                profile = Profile.objects.get(profile_id = profile_id)

                seasons = Season.objects.all()
                movies = Movie.objects.all()
                popular_seasons = Season.objects.all()[0:10]
                popular_movies = Movie.objects.all()[0:10]

                

                
               
                c_type = ""

                

                

                
                mylist =[]
                likedlist =[]

                
                
                if profile.content_list is not None:

                    added_content = profile.content_list.content.all()
                    for i in added_content:
                        mylist.append(i.c_id)

                
                if profile.liked_content is not None:

                    liked_content = profile.liked_content.content.all()

                    for i in liked_content:
                        likedlist.append(i.c_id)
                
                adult = True
                if profile.is_kid:
                    adult = False
                else:
                    adult = True

                context = {
                               'current_page':'home',
                               'adult':adult,
                               'profile':profile,
                               'c_type':c_type,
                               'seasons':seasons,
                               'popular_seasons':popular_seasons,
                               'movies':movies,
                               'popular_movies':popular_movies,
                               'mylist':mylist,
                               'likedlist':likedlist
                               }
                        
                
                return render(request,"content/movies.html",context)
            else:
                return redirect("profile-page")
    else:
        return redirect("subscription-page")


def content_page(request,c_type,video_id):
    if c_type == "series":
        episode = Episode.objects.filter(id = video_id).first()
        video_link = episode.episode
        episode_no = episode.episode_no
        name = episode.name
        poster = episode.thumbnail
        data = {
            'c_type':"series",
             'url':video_link,
             'poster':poster,
             'episode_no':episode_no,
             'name':name
             }
    else:
        movie = Movie.objects.filter(id = video_id).first()
        video_link = movie.movie
        name = movie.title
        poster = movie.poster
        data = {
            'c_type':"movie",
             'url':video_link,
             'poster':poster,
             'name':name
             }
    return render(request,"content/content.html",data)



def add_my_list(request):
    if request.method == 'POST':
        c_id = request.POST.get('c_id')

        print(c_id)

        profile_id = request.session['profile_id']
        profile = Profile.objects.get(profile_id=profile_id)

        if Content.objects.filter(c_id=c_id).exists():
            content = Content.objects.get(c_id = c_id)
            
        else:
            content = Content.objects.create(c_id = c_id)

        if profile.content_list.content.filter(c_id=c_id).exists():
            profile_content_list = profile.content_list
            profile_content_list.content.remove(content)
            profile.save()
            return HttpResponse("Content Deleted")
        else:
            profile_content_list = profile.content_list
            profile_content_list.content.add(content)
            profile.save()
            return HttpResponse("Content Added")


def add_liked_list(request):
    if request.method == 'POST':
        c_id = request.POST.get('c_id')

        if Season.objects.filter(season_id=c_id).exists():
            cont = Season.objects.filter(season_id=c_id).first()
        else:
            cont = Movie.objects.filter(movie_uid=c_id).first()

        

        print(c_id)

        profile_id = request.session['profile_id']
        profile = Profile.objects.get(profile_id=profile_id)

        if Content.objects.filter(c_id=c_id).exists():
            content = Content.objects.get(c_id = c_id)
            
        else:
            content = Content.objects.create(c_id = c_id)

        
        if profile.liked_content.content.filter(c_id=c_id).exists():
            profile_liked_list = profile.liked_content
            profile_liked_list.content.remove(content)
            profile.save()
            cont.likes -= 1
            cont.save()
            return HttpResponse("Like Removed")
        else:
            profile_liked_list = profile.liked_content
            profile_liked_list.content.add(content)
            profile.save()
            cont.likes += 1
            cont.save()
            return HttpResponse("Like Added")
   

@login_required
def mylist_page(request):

    profile_id = request.session['profile_id']
    profile = Profile.objects.get(profile_id=profile_id)

    if profile.content_list.content.exists():

        content_list = profile.content_list.content.all()
    
        seasons = []
        movies = []
    
        for index,i in enumerate(content_list):
            if Season.objects.filter(season_id = i).exists():
                season = Season.objects.get(season_id = i)   
                seasons.append({'counter':index+1,'season':season})    
            else:
                movie = Movie.objects.get(movie_uid = i)   
                movies.append({'counter':index+1,'movie':movie})


        if request.method == 'POST':

            season_id = request.POST.get('removeReq')
            season = Content.objects.get(c_id = season_id)
            content_list = profile.content_list.content.remove(season)
            print(season_id)
            return HttpResponseRedirect(request.path)


        
        
        return render(request,"content/mylist.html",{'seasons':seasons,'movies':movies,'profile':profile})
        
    
        
    else:
        return render(request,"content/mylist.html",{'message':"There is no content Added.",'profile':profile})
    
def content_provider(request,c_id):
        # user = authenticate(username = 'radharaman@gmail.com',password='radharani')
        # login(request,user)


        if Season.objects.filter(season_id = c_id).exists():
            content = Season.objects.get(season_id = c_id)

            print("Come to Season")
            
    
            # Fetching all Seasons Id
            seasons_all = content.series.season.all()
            seasons=[]
            for i in seasons_all:
                seasons.append(i.season_id)
    
            # Fetching All episode of Current Season
            episodes = Episode.objects.filter(season = content).values()
            episode_list = list(episodes)


            profile = Profile.objects.get(profile_id=request.session['profile_id'])
            # profile = Profile.objects.get(profile_id='28bd24c4-940b-4b20-a754-c4531b2039be')

            is_in_liked_list=False
            if profile.liked_content.content.filter(c_id=c_id).exists():
                is_in_liked_list = True
    
            is_in_content_list=False
            if profile.content_list.content.filter(c_id=c_id).exists():
                is_in_content_list = True

            title_img = content.series.title_img.url
            title_img = title_img.replace("/media/media/","/static/media/")

            poster = content.poster.url
            poster = poster.replace("/media/media/","/static/media/")

            
            data = {
                'c_type':'series',
                'c_id':c_id,
                'poster': poster ,
                'series':content.series.title,
                'title_img':title_img,
                'total_seasons':content.series.no_of_season,
                'seasons':seasons,
                'season_no': content.season_no,
                'actors': list(content.actors.all().values('name')),
                'genres': list(content.series.genres.all().values('name')),
                'description':content.description,
                'trailer':content.trailer,
                'released_date':content.released_date,
                'episodes':episode_list,
                'is_in_content_list':is_in_content_list,
                'is_in_liked_list':is_in_liked_list,
            }
            return data
        
        else:
            content = Movie.objects.get(movie_uid = c_id)
            print("Come to Movie")

            profile = Profile.objects.get(profile_id=request.session['profile_id'])
            # profile = Profile.objects.get(profile_id='28bd24c4-940b-4b20-a754-c4531b2039be')
            
            is_in_liked_list=False
            if profile.liked_content.content.filter(c_id=c_id).exists():
                is_in_liked_list = True
    
            is_in_content_list=False
            if profile.content_list.content.filter(c_id=c_id).exists():
                is_in_content_list = True

            title_img = content.title_img.url
            title_img = title_img.replace("/media/media/","/static/media/")

            poster = content.poster.url
            poster = poster.replace("/media/media/","/static/media/")
            
            data = {
                'c_type':'movie',
                'm_id':content.id,
                'title':content.title,
                'c_id':c_id,
                'poster': poster ,
                'title_img':title_img,
                'actors': list(content.actors.all().values('name')),
                'genres': list(content.genres.all().values('name')),
                'description':content.description,
                'trailer':content.trailer,
                'released_date':content.released_date,
                'is_in_content_list':is_in_content_list,
                'is_in_liked_list':is_in_liked_list,
            }

            return data
     

def get_content(request,c_id):
    if request.method == 'GET':


        print(c_id)

        data = content_provider(request,c_id)
       
        # print(content)
        # print(content.name)
        # return JsonResponse(content,safe=False)
        return JsonResponse(data,safe=False)


def get_episodes(request,c_id):
    if request.method == 'GET':

        print(c_id)
        content = Season.objects.get(season_id = c_id)

      

        # Fetching All episode of Current Season
        episodes = Episode.objects.filter(season = content).values()
        episode_list = list(episodes)
       
        
        data = {
           
            'episodes':episode_list
           
        }
        # print(content)
        # print(content.name)
        # return JsonResponse(content,safe=False)
        return JsonResponse(data,safe=False)


def search(request,query):
    print(query)

    contents = Series.objects.filter(title__icontains = query)
    contents2 = Movie.objects.filter(title__icontains = query)
    by_actor = Actor.objects.filter(name__icontains = query)
    by_actor_content = []
    for i in by_actor:
        content = Season.objects.filter(actors=i)
        content2 = Movie.objects.filter(actors=i)
        for j in content:
            by_actor_content.append(j.season_id)
        for k in content2:
            by_actor_content.append(k.movie_uid)
    content_Id_list = []
    
    for i in contents:
        season = Season.objects.filter(series = i)
        for j in season:
            content_Id_list.append(j.season_id)

    for i in contents2:
            content_Id_list.append(i.movie_uid)
    print(contents2)
    print(content_Id_list)

    for c_id in by_actor_content:
        if c_id in content_Id_list:
            pass
        else:
            content_Id_list.append(c_id)

    content_list =[]

    for c_id in content_Id_list:
        data = content_provider(request,c_id)
        content_list.append(data)
    
    # print(content_list)


    return JsonResponse(content_list,safe=False)