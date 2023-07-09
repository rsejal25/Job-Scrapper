from django.urls import path
from . import views
urlpatterns=[
path('register1',views.RegisterView.as_view()),
path('show/',views.show),
path('login1',views.LoginView.as_view()),
path('login_form',views.login_page),
path('register_form',views.register_page),
path('users_list',views.users_list),
path('details',views.users_details),
path('update_form',views.update_form),
path('delete_form',views.delete_form),
path('delete',views.delete_user),
path('update_user',views.update_user),
]