from django.contrib import admin
from .models import *
# Register your models here.


class BaseUserAdmin(admin.ModelAdmin):
    list_display=["user","no_of_profile","email_token","is_email_verified","created_at","updated_at"]

admin.site.register(BaseUser,BaseUserAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display=["subscription","order_id","payment_id","payment_signature","amount","status","created_at","updated_at"]

admin.site.register(Payment,PaymentAdmin)

class SubscriptionAdmin(admin.ModelAdmin):
    list_display=["baseuser","plan","is_plan_active","start_date","expiry_date"]

admin.site.register(Subscription,SubscriptionAdmin)

class PlanAdmin(admin.ModelAdmin):
    list_display=["name","amount"]

admin.site.register(Plan,PlanAdmin)

class profileAvtarAdmin(admin.ModelAdmin):
    list_display=["avatar"]

admin.site.register(profileAvtar,profileAvtarAdmin)

class ActorAdmin(admin.ModelAdmin):
    list_display=["name"]

admin.site.register(Actor,ActorAdmin)

class GenresAdmin(admin.ModelAdmin):
    list_display=["name"]

admin.site.register(Genre,GenresAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display=["baseuser","name","is_kid","profile_pic","choice","content_list","created_at","updated_at"]

admin.site.register(Profile,ProfileAdmin)


class ContentAdmin(admin.ModelAdmin):
     list_display=["c_id"]

admin.site.register(Content,ContentAdmin)
admin.site.register(Profile_Content_List)
admin.site.register(Profile_Liked_List)
admin.site.register(Profile_Choice)