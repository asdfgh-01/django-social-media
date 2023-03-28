from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index' ),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('signout',views.signout,name='signout'),
    path('settings',views.settings,name='settings'),
    path('upload',views.upload,name='upload'),
    path('user/<str:username>',views.profile,name='profile'),
    path('follow/<str:username>',views.follow,name='follow'),
    path('chat/', views.home, name='home'),
    path('chat/<str:room>/', views.room, name='room'),
    path('chat/checkview', views.checkview, name='checkview'),
    path('chat/send', views.send, name='send'),
    path('chat/getMessages/<str:room>/', views.getMessages, name='getMessages'),
]