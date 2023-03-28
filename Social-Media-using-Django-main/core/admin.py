from django.contrib import admin
from .models import Profile,Post,Follower
from .models import Room, Message

# Register your models here.
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Follower)