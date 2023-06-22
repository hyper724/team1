from django.urls import path
from pybo import views

urlpatterns = [
    path('', views.recommend_food),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_page, name='login'),
    path('index/', views.index, name='index'),
]