from django.urls import path
from . import views

urlpatterns = [
    path('',views.IndexView,name='index'),
    path('register/',views.RegisterView,name='register'),
    path('login/',views.LoginView,name='login'),
    path('logout/',views.LogoutView,name='logout'),
    path('update-profile',views.updateProfileView,name='update-profile'),
    path('create-post',views.createPostView,name='create-post'),
    path('follow-check/<int:target>/<int:follower>/',views.follower_check_api_view,name='follow-check'),
    path('follow/<int:target>/<int:follower>/',views.follow_api_view,name='follow'),
    path('unfollow/<int:target>/<int:follower>/',views.unfollow_api_view,name='unfollow'),
]