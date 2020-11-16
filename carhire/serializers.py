from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from .models import User, Profile
from django.contrib.auth import get_user_model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','role']
class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    user_details = UserSerializer(source='user', read_only=True)
    class Meta:
        model = Profile
        fields = ['id','user','name','location','profile_picture','user_details']

    def save(self, **kwargs):
        """Include default for read_only `user` field"""
        kwargs["user"] = self.fields["user"].get_default()
        return super().save(**kwargs)