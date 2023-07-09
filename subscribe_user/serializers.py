from rest_framework import serializers
from .models import Subscribed_Users
class Subscribed_User_Serializer(serializers.ModelSerializer):
  class Meta:
    model=Subscribed_Users
    fields='__all__'