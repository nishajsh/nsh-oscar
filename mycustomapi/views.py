from django.http import Http404

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from oscar.core.loading import get_model
from oscarapi.utils import OscarModelSerializer
from oscar.core.compat import get_user_model

User = get_user_model()


class UserSerializer(OscarModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'id')


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):

    def get_object(self, pk):
        try:
            return User.objects.get(id=pk)
        except User.DoesNotExist:
            raise Http404
    

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
