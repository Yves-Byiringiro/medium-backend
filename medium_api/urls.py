from django.urls import path, include
from medium_api import views

from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('profile',views.ProfileViewSet)
router.register('articles',views.ArticleViewSet)




urlpatterns = [
    
    path('login/', views.LoginViewSet.as_view()),
    path('', include(router.urls))

]
