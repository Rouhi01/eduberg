from rest_framework.views import APIView, Response
from rest_framework import generics, status
from .serializers import SignupSerializer, ChangePassSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import (
    OutstandingToken, BlacklistedToken
)



class SignupApiView(generics.GenericAPIView):
    serializer_class = SignupSerializer

    def post(self, request, *args, **kwargs):
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class LogoutApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class LogoutAllApiView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            BlacklistedToken.objects.get_or_created(token=token)
        return Response(status=status.HTTP_205_RESET_CONTENT)
    
class ChangePassApiView(generics.GenericAPIView):
    serializer_class = ChangePassSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        obj = self.request.user
        return obj
    
    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        if not self.object.check_password(serializer.data.get('old_password')):
            return Response({
                'old_password': ['Wrong password']
            })
        self.object.set_password(serializer.data.get('new_password'))
        self.save()
        response = {
            'user': self.object.email,
            'status': 'success', 
            'code': status.HTTP_200_OK,
            'message': 'Password updated successfully',
        }
        return Response(response)
    