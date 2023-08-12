from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import InputValueViewSet, HomePageView

router = DefaultRouter()
router.register(r'api/get_all_input_values', InputValueViewSet, basename='input-values')

urlpatterns = [
    path('',  HomePageView.as_view(), name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('khoj_search/', views.khoj_search, name='khoj_search'),
    *router.urls,
]
