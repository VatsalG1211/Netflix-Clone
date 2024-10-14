from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .email import send_email_activation_link
from django.utils import timezone


# Create your models here.


class BaseUser(models.Model):

    userid = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="baseuser")
    email_token = models.CharField(null=True,blank=True,max_length=255)
    is_email_verified = models.BooleanField(default=False)
    no_of_profile = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    token_expiry_at = models.DateTimeField(null=True,blank=True)

    def activateEmail(self):

        self.is_email_verified = True
        self.email_token = ""
        self.save()

    def __str__(self):
        return self.user.username



class Plan(models.Model):
    name = models.CharField(max_length=25)
    amount = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.amount}"

class Subscription(models.Model):
    baseuser = models.ForeignKey(BaseUser,on_delete=models.CASCADE,related_name="subscription")
    order_id = models.CharField(max_length=100,null=True)
    plan = models.ForeignKey(Plan,on_delete=models.CASCADE,null=True,blank=True)
    is_plan_active = models.BooleanField(default=False)
    start_date = models.DateTimeField()
    expiry_date = models.DateTimeField()
    

    def save(self,*args,**kwargs):

        if not self.start_date:
            self.start_date = timezone.now()
            self.expiry_date = self.start_date + timezone.timedelta(minutes=15)

        return super().save(*args,**kwargs)

    def check_validity(self):
        if timezone.now() > self.expiry_date :
            self.is_plan_active = False
            self.save()
            return False
        return True

    def __str__(self):
        return f"{self.baseuser} \n {self.plan}"

class Payment(models.Model):

    subscription = models.ForeignKey(Subscription,on_delete=models.CASCADE,related_name="payment")
    order_id = models.CharField(max_length=100,unique=True,blank=True,null=True)
    payment_id = models.CharField(max_length=100,unique=True,blank=True,null=True)
    payment_signature = models.CharField(max_length=100,unique=True,blank=True,null=True)
    amount = models.DecimalField(decimal_places=2,max_digits=10,null=True,blank=True)

    status_choices = [
        ('pending','Pending'),
        ('completed','Completed'),
        ('failed','Failed')
    ]

    status = models.CharField(max_length=10,null=True,choices=status_choices,default='pending',blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.status} \n {self.amount} \n {self.payment_id}"



class profileAvtar(models.Model):
    avatar = models.ImageField(upload_to="img/profile_img/")

    def __str__(self) :
        return f"{self.avatar}"


class Actor(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True,unique=True)

    class Meta:
        ordering = ["name"]
    
    def __str__(self):
        return f"{self.name}"

class Genre(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"

class Content(models.Model):
    c_id = models.CharField(max_length=255,null=True,blank=True,unique=True)

    def __str__(self):
        return f"{self.c_id}"

class Profile_Content_List(models.Model):
    content = models.ManyToManyField(Content)

class Profile_Liked_List(models.Model):
    content = models.ManyToManyField(Content)
    

class Profile_Choice(models.Model):
    actors = models.ManyToManyField(Actor)
    genres = models.ManyToManyField(Genre)
    

    
    


class Profile(models.Model):

    baseuser = models.ForeignKey(BaseUser,on_delete=models.CASCADE,related_name="profile")
    profile_id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    name = models.CharField(null=True,blank=True,max_length=50)
    is_kid = models.BooleanField(default=False)
    profile_pic = models.ForeignKey(profileAvtar,on_delete=models.SET_NULL,related_name="profile_pic",null=True)
    choice = models.ForeignKey(Profile_Choice,on_delete=models.SET_NULL,null=True,blank=True,related_name="profile")
    liked_content = models.OneToOneField(Profile_Liked_List,on_delete=models.SET_NULL,null=True,blank=True)
    content_list = models.OneToOneField(Profile_Content_List,on_delete=models.SET_NULL,null=True,blank=True,related_name="content_list")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def delete(self,*args,**kwargs):
        baseuser = self.baseuser
        baseuser.no_of_profile = baseuser.no_of_profile - 1
        baseuser.save()

        self.choice.delete()

        return super().delete(*args,**kwargs)


    

    def __str__(self):
        return f"{self.baseuser} - {self.name}"





@receiver(post_save,sender = User)
def EmailActivationLink(sender,instance,created,**kwargs):

    if created:
        email = instance.email
        baseuser = BaseUser.objects.create(user = instance)
        email_token = uuid.uuid4()
        baseuser.email_token = email_token
        baseuser.save()
        send_email_activation_link(email,email_token)


@receiver(post_save,sender = Payment)
def activateSubscription(sender,instance,created,**kwargs):
    if created:
        pass
    else:
        subscription = instance.subscription
        if instance.status == 'completed':
            if not subscription.is_plan_active and subscription.expiry_date > timezone.now():
                subscription.is_plan_active = True
                subscription.save()

        baseuser = subscription.baseuser   

        payments = Payment.objects.filter(subscription__baseuser = baseuser,status = 'pending')
        for i in payments:
            i.status = 'failed'
            i.save()

@receiver(post_save, sender=Profile)
def create_profile(sender, instance, created, **kwargs):

    if created:
        baseuser = instance.baseuser
        baseuser.no_of_profile = baseuser.no_of_profile + 1
        baseuser.save()
        
    if created:
        profile_choice = Profile_Choice.objects.create()
        instance.choice = profile_choice

        profile_add_my_list = Profile_Content_List.objects.create()
        instance.content_list = profile_add_my_list

        profile_liked_list = Profile_Liked_List.objects.create()
        instance.liked_content = profile_liked_list

        instance.save()

