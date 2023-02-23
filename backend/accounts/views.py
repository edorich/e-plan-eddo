from rest_framework import permissions, mixins, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import UserAccount
from .serializers import UserAccountSerializer, UserSerializer

User = get_user_model()


class SignupView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        data = self.request.data

        password = data['password']
        password2 = data['password2']

        if password == password2:
            serializer = UserAccountSerializer(data=data)

            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            user = serializer.create(serializer.validated_data)
            user = UserSerializer(user)

            return Response(user.data, status=status.HTTP_201_CREATED)

        return Response({'error': 'Password must be same'})


class UserAccountListAPIView(mixins.ListModelMixin,
                             mixins.RetrieveModelMixin,
                             mixins.DestroyModelMixin,
                             mixins.UpdateModelMixin,
                             generics.GenericAPIView):

    permission_classes = [permissions.IsAuthenticated]
    queryset = UserAccount.objects.all().order_by('id')
    serializer_class = UserSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        return qs
