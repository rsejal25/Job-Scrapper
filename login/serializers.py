from rest_framework import serializers
from .models import Login_USER
class LoginSerializer(serializers.ModelSerializer):
  class Meta:
    model=Login_USER
    fields='__all__'

