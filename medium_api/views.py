from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from medium_api.permissions import UpdateOwnProfile
from medium_api.serializers import ProfileSerializer
from medium_api.models import UserInfo







class ProfileViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (UpdateOwnProfile,)
    authentication_classes =(TokenAuthentication,)