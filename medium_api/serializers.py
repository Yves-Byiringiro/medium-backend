from rest_framework import serializers

from medium_api.models import UserInfo, Category, Article




class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('id','email','username','password')

        extra_kwargs = {

            'password':{
                'write_only':True,
                'style':{'input_type':'password'}  
            }
        }
    
    def create(self, validated_data):
        user = UserInfo.objects.create_user(
            email = validated_data['email'],
            username = validated_data['username'],
            password = validated_data['password']

        )
        return user



class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id','title','description','claps','timestamp','category','author')


        extra_kwargs = {

            'author':{'read_only':True}
        }


