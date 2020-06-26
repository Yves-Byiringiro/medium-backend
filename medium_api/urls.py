from django.urls import path, include
from medium_api import views

from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('profile',views.ProfileViewSet)




urlpatterns = [
    
    path('login/', views.LoginViewSet.as_view()),
    path('', include(router.urls))

]
