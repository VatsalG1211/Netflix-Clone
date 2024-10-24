from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse,Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.utils import timezone
from django.contrib import messages
from django.conf import settings
import string
from django.core.cache import cache
import uuid
from .models import *
import razorpay
from .email import send_password_reset_link
from django.views.decorators.csrf import csrf_exempt

THROTTLE_RATE = 3  # Number of allowed requests
THROTTLE_PERIOD = 30  # Time window in seconds (1 hour)


# Index Page

def index_page(request):

    if request.user.is_authenticated:
        baseuser = request.user.baseuser
        if Subscription.objects.filter(baseuser=baseuser,is_plan_active=True).exists():
            subscription = Subscription.objects.filter(baseuser=baseuser,is_plan_active=True).first()
            if subscription.check_validity():
                return redirect("profile-page")
           

    if request.method == 'POST':
        email = request.POST.get('email')

        if User.objects.filter(username = email).exists():
            messages.warning(request,"Email is Already taken!")
            print("Email is Already taken!")
            return HttpResponseRedirect(request.path)
        
        else:
            return redirect("register",email)
        

    return render(request,"account/index.html")

# Signup Page

def register_page(request,email):

    if request.method == 'POST':

        email = email
        password = request.POST.get('password')
        
        
        if len(password)<8:
            messages.warning(request,"Password must be atleast 8 characters")
            print("Password must be atleast 8 characters")
            return HttpResponseRedirect(request.path)
    
        user = User.objects.create_user(username=email,email=email,password=password)
      
        # messages.success(request,"Account Successfully Created")
        return redirect(f"/account/email-verification-message/{user.email}")
    

    return render(request,"account/signup.html",{'email':email})


#  Email Verification Message Sent Page

def email_verification_message(request,email):
    if User.objects.filter(email = email).exists():
        user = User.objects.get(email=email)
        baseuser = user.baseuser
        if not baseuser.is_email_verified:
            email = baseuser.user.email
            return render(request,"account/email-verification-message.html",{'email':email})
        else:
            if baseuser.is_email_verified:
                messages.warning(request,"You are already verified !")
                return redirect("login")
    else:    
        return HttpResponse("Lost Your Way")


# Activation of Email

def activate_email(request,email_token):

    if BaseUser.objects.filter(email_token=email_token).exists():

        baseuser = BaseUser.objects.get(email_token=email_token)
        baseuser.activateEmail()
        messages.success(request,"Your email has been Verified !Login Now")
        return redirect("login")
    else:
         raise Http404()


#Forgot Page

def forgot_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        # Get user's IP address
        ip_address = request.META.get('REMOTE_ADDR')

        # Create a unique cache key for the IP address
        cache_key = f"forgot_email_{ip_address}"
        
        # Check how many requests have been made in the last hour

        request_count = cache.get(cache_key, 0)

        if request_count >= THROTTLE_RATE:
            messages.warning(request, 'Too many requests. Please try again later.')
            return HttpResponseRedirect(request.path)


        if not User.objects.filter(email=email).exists():
            messages.warning(request,"User Doesn't Exists !")
            return HttpResponseRedirect(request.path)
        else:
            email_token = uuid.uuid4()
            user = User.objects.get(email=email)
            baseuser = BaseUser.objects.get(user=user)
            baseuser.email_token = email_token
            baseuser.token_expiry_at = timezone.now() + timezone.timedelta(minutes=1)
            baseuser.save()

            send_password_reset_link(request.scheme,request.get_host(),email,email_token) #via email

            # Increment request count
            cache.set(cache_key, request_count + 1, timeout=THROTTLE_PERIOD)

            return render(request,"account/password-reset-message.html",{'email':email})
        
    return render(request,"account/forgot-password.html")

# Reset Password
def reset_password(request,email_token):
    if BaseUser.objects.filter(email_token = email_token).exists():
        baseuser = BaseUser.objects.get(email_token = email_token)
        # Getting TOken Expiry Time
        if timezone.now() > baseuser.token_expiry_at:
            messages.warning(request,"Link is Expired !")
            return redirect("index")
        if request.method == 'POST':
            password = request.POST.get('password')
            conf_password = request.POST.get('conf-password')
            
            if password != conf_password:
                messages.warning(request,"Password Does'nt Match")
                return HttpResponseRedirect(request.path)
            else:
                user = baseuser.user
                user.set_password(password)
                user.save()
                baseuser.save()
                messages.success(request,"Password has been changed")
                return redirect('login')
        return render(request,"account/reset-password.html")
    else:
         raise Http404()

# Login page

def login_page(request):

    if request.user.is_authenticated:
        return redirect("profile-page")  

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember_user = request.POST.get('remember')
        if User.objects.filter(email=email).exists():

            user = authenticate(username = email,password=password)

            
            if user is not None:
                if user.baseuser.is_email_verified:
                    login(request,user)

                    if remember_user:
                        request.session.set_expiry(60 * 60 * 24 * 30)  # 30 days
                    else:
                        request.session.set_expiry(0)

                    user = User.objects.get(email = email)
                    baseuser = BaseUser.objects.get(user = user)

                    if Subscription.objects.filter(baseuser = baseuser).exists():
                        subscription = Subscription.objects.filter(baseuser = baseuser).order_by('-start_date').first()
                        if subscription.check_validity():
                            return redirect("profile-page")
                        else:
                            messages.warning(request,"You don't have any subscription plan.") 
                            return redirect("subscription-page")
                    else:    
                        return redirect("subscription-page")
                else:
                    messages.warning(request,"Please Activate You Email Id")
                    return HttpResponseRedirect(request.path)    
            else:
                messages.warning(request,"Please Enter Correct Password")
                return HttpResponseRedirect(request.path)
            
        
        else:
            messages.warning(request,"User doesn't exists")
            return HttpResponseRedirect(request.path)

    return render(request,"account/login.html")

# Logout 

def logout_page(request):   
    logout(request)
    return redirect("login")


# Subscription Page
@login_required
def subscription_page(request):
    baseuser = request.user.baseuser
    if Subscription.objects.filter(baseuser=baseuser,is_plan_active=True).exists():
        return redirect("profile-page")
    
    return render(request,"account/plan-select.html")

# Payment Page
@login_required
def payment_page(request):
    

    if request.method == 'POST':

        plan_name = request.POST.get('plan')
        print("plan Name",plan_name)
        if plan_name is None:
            messages.warning(request,"there is a problem occured here .try again!")
            return redirect("subscription-page")
        plan = Plan.objects.get(name = plan_name)
        amount = int(plan.amount)
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_SECRET_KEY))

        details = {'amount': amount * 100  , 'currency':'INR'}
        order = client.order.create(data = details)
        print(order['id'])
        
        baseuser = BaseUser.objects.get(user = request.user)

        check_active_plan = False

        if Subscription.objects.filter(baseuser = baseuser).exists():
            subscription = Subscription.objects.filter(baseuser = baseuser)
            for i in subscription:
                if i.is_plan_active:
                    check_active_plan = True
                    break

        if not check_active_plan:        
            subscription = Subscription.objects.create(baseuser = baseuser,plan = plan,order_id = order['id'])
            print(subscription)
            payment = Payment.objects.create(subscription = subscription, amount = amount)
        else:
            return redirect("profile-page")

        data = {'apikey':settings.RAZORPAY_KEY_ID,'email':request.user.email,'order_id':order['id'],'amount':amount}
    return render(request,"account/payment.html",data)

# Fetching Payment info after paying amount 
@csrf_exempt
@login_required
def payment_info(request):
   
    if request.method == 'POST':
        print("Also come")
        response = request.POST

        order_id = response.get('razorpay_order_id')
        payment_id = response.get('razorpay_payment_id')
        payment_signature = response.get('razorpay_signature')

        baseuser = BaseUser.objects.get(user = request.user)
        subscriptions = Subscription.objects.filter(baseuser = baseuser) 

        if Subscription.objects.filter(order_id = order_id).exists():

            subscription = Subscription.objects.get(order_id = order_id)
            payment = Payment.objects.get(subscription = subscription)
            payment.status = 'completed'
            payment.order_id = order_id
            payment.payment_id = payment_id
            payment.payment_signature = payment_signature
            payment.save()

            # cancelling pending payments
            print("verfication done")
          
            return redirect("profile-page")

# Profile Page        
@login_required
def profile_page(request):
    print("come")
    baseuser = request.user.baseuser

    if Subscription.objects.filter(baseuser=baseuser,is_plan_active=True).exists():

        subscription = Subscription.objects.filter(baseuser=baseuser,is_plan_active=True)[0]

        if subscription.check_validity():
            
            if request.method == 'POST':
                profile_img = request.POST.get('profile')
                profile_name = request.POST.get('name')
                is_kid = request.POST.get('is_kid')
                if is_kid is None:
                    is_kid = False
                else:
                    is_kid = True
                
                img = profileAvtar.objects.get(avatar=profile_img) 
                if baseuser.no_of_profile < 5:
                    profile = Profile.objects.create(baseuser=baseuser,
                                                     name=profile_name,
                                                     is_kid=is_kid,
                                                     profile_pic = img)
                    return HttpResponseRedirect(request.path)
                else:
                    return HttpResponseRedirect(request.path)
            profiles = Profile.objects.filter(baseuser = baseuser)
            avatars = profileAvtar.objects.all()
            # Profile.objects.first().delete()
            return render(request,"account/profile.html",{'avatar':avatars,'profiles':profiles,'no_of_profile':baseuser.no_of_profile})
        
        else:
            messages.warning(request,"No plan")
            return redirect("subscription-page")
    else:
        messages.warning(request,"No plan")
        return redirect("subscription-page")



# profile to home redirection according to baseuser's profile
@login_required
def profileRedirector(request,profile_id):

    if Profile.objects.filter(profile_id = profile_id).exists():
        print("yes")
        request.session['profile_id'] = profile_id
        return redirect("home")
    else:
        print("no")
        return redirect("profile-page")




def profile_account(request):
    profile_id = request.session['profile_id']
    profile = Profile.objects.get(profile_id=profile_id)
    baseuser = profile.baseuser
    subscription = Subscription.objects.filter(baseuser=baseuser,is_plan_active=True).first()
    plan = subscription.plan.name
    subscription_id = subscription.order_id
    avatars = profileAvtar.objects.all()
    context = {
        'avatar':avatars,
         'profile':profile,
         'plan':plan,
         'sub_id':subscription_id
    }

    Old_profile_name = profile.name
    Old_profile_avatar = profile.profile_pic.avatar
    Old_is_kid = profile.is_kid
    Old_profile_pic = profile.profile_pic

    if request.method == 'POST':
        profile_img = request.POST.get('profile')
        profile_name = request.POST.get('name')
        is_kid = request.POST.get('is_kid')
        if is_kid is None:
            is_kid = False
        else:
            is_kid = True
        
        if Old_profile_name != profile_name:
            profile.name = profile_name
        if Old_is_kid != is_kid:
            profile.is_kid = is_kid
        if Old_profile_avatar != profile.profile_pic:
            profile_img = profileAvtar.objects.get(avatar=profile_img)
            profile.profile_pic = profile_img
        profile.save() 

        return HttpResponseRedirect(request.path)

    return render(request,'account/profile-account.html',context)    

def profile_account_delete(request):
    
    profile_id = request.session['profile_id']
    profile = Profile.objects.get(profile_id=profile_id)
    profile.delete()
    return redirect("profile-page")


    