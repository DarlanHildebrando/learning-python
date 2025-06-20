from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Cliente

class UserDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class SerializerClientView(serializers.ModelSerializer):
    user = UserDisplaySerializer

    email = serializers.EmailField(write_only=True, required=True)
    username = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)

    print('AAAAAAAAAAAAAAAA')

    class Meta:
        model = Cliente
        fields = (
          'id',
          'username',
          'email',
          'password'
        )
        read_only_fields = [id]

    def create(self, validated_data):
        
        user_data = {
            'username': validated_data.pop('username'),
            'email': validated_data.pop('email'),
            'password': validated_data.pop('password'),
        }

        user = User.objects.create_user(**user_data)
        
        cliente = Cliente.objects.create(user=user, **validated_data)

        return cliente

class SerializerReadOnly(serializers.ModelSerializer):
    

# class serializerRegisterUser(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta: 
#         model = User
#         fields = ["username", "password", "email"]

#     def create(self, validate_data):

#         user = User.objects.create_user(
#             username=validate_data["username"],
#             email=validate_data["email"],
#             password=validate_data["password"],

#         )

#         return user  

# class serializerListAllClients(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["id", "username", "email"]
