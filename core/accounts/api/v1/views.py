from rest_framework.views import APIView, Response
from rest_framework import generics, status
from .serializers import SignupSerializer

class SignupApiView(generics.GenericAPIView):
    serializer_class = SignupSerializer

    def post(self, request, *args, **kwargs):
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)