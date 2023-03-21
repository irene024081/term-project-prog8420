from django.contrib.auth.models import User
from rest_framework import serializers
from dj_rest_auth.serializers import UserDetailsSerializer


class ResistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style = {'input_type':'password'}, 
                                      write_only=True)
    

    class Meta:
        model = User
        fields = ['username','email','password','password2','first_name','last_name']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({'error': 'p1 and p2 should be the same'})
    
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'email already exists'})
        
        account = User(email = self.validated_data['email']
                       , username = self.validated_data['username']
                       , first_name = self.validated_data['first_name']
                       , last_name = self.validated_data['last_name'])
        account.set_password(password)
        account.save()
        return account
    