from django.urls import path
from . import views
urlpatterns=[
path('home',views.home_page),
path('subscribe_user',views.subscribe_user),
path('search_page',views.search_page),
path('view_profile_page',views.profile_user_page),
path('user_details',views.get_user_details),
path('delete_designation_search',views.delete_designation_search),
]