from user_app.api.serializer import ResistrationSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
#from rest_framework_simplejwt.tokens import RefreshToken



@api_view(['POST', ])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status= status.HTTP_200_OK)

@api_view(['POST', ])
def registration_view(request):
    
    if request.method == 'POST':
        serializer = ResistrationSerializer(data = request.data)
        
        data = {}
        
        if serializer.is_valid(raise_exception=True):
            account = serializer.save()
            
            data['response'] = "Registration Successful"
            data['username'] = account.username
            data['email'] = account.email
        
            
        else:
            data = serializer.errors
        
        return Response(data, status=status.HTTP_201_CREATED)
