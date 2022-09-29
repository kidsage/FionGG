import email
from accounts.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.models import update_last_login
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

User = get_user_model()

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get('email')
        username = data.get('username')
        password = data.get('password', None)
        # 사용자 아이디와 비밀번호로 로그인 구현(<-> 사용자 아이디 대신 이메일로도 가능)
        user = authenticate(email=email, password=password)

        if user is None:
            return {
                'id':'None',
                'email':email,
                'username':username,
            }

        try:
            payload = JWT_PAYLOAD_HANDLER(user) # payload 생성
            jwt_token = JWT_ENCODE_HANDLER(payload) # jwt token 생성
            update_last_login(None, user)

        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given username and password does not exist'
            )

        return {
            'id':user.id,
            'token': jwt_token
        }

# 사용자 정보 추출
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username')

