from .serializers import UserSerializear, UserUpdateSerializear
from .models import User
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt


def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }


# Create your views here.

class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializear

    def post(self, request, *args, **kwargs):
        serializer = UserSerializear(data=request.data)
        serializer.validate_username(request.data['username'])
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"user": serializer.data, 'msg': 'Registration Successful'})


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    obj = User.objects.filter(username=username)
    if not obj:
        return Response({"message": "Invalid Credentials"})
    else:
        data = list(obj.values('status'))
        data = data[0]
        data = data['status']
        if data == 3:
            return Response({"message": "user is not exists"})
        else:
            if username is None or password is None:
                return Response({'error': 'Please provide both username and password'},
                                status=status.HTTP_400_BAD_REQUEST)
            user = authenticate(username=username, password=password)
            if not user:
                return Response({'error': 'Invalid Credentials'})
            token = get_token_for_user(user)
            return Response({'token': token}, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def MyProfileView(request):
    try:
        if emp := User.objects.get(pk=request.user.id):
            serializer = UserUpdateSerializear(emp)
            return Response(serializer.data)
    except Exception as E:
        return Response({"error: something went wrong"}, status=status.HTTP_400_BAD_REQUEST)


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializear
    filterset_fields = ['username']

