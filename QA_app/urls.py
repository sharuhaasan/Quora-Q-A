from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('ask/', ask_question, name='ask_question'),
    path('question/<int:pk>/', question_detail, name='question_detail'),
    path('like/<int:answer_id>/', like_answer, name='like_answer'),
    path('register/', register, name='register'),
]
