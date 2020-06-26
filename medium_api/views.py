from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from rest_framework.permissions import IsAuthenticatedOrReadOnly

from medium_api.permissions import UpdateOwnProfile, UpdateOwnArticle
from medium_api.serializers import ProfileSerializer, ArticleSerializer
from medium_api.models import UserInfo, Category, Article




class ProfileViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (UpdateOwnProfile,)
    authentication_classes =(TokenAuthentication,)



class LoginViewSet(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES



class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (UpdateOwnArticle, IsAuthenticatedOrReadOnly)
    authentication_classes = (TokenAuthentication,)



    def perform_create(self, serializer):
        serializer.save(author=self.request.user)