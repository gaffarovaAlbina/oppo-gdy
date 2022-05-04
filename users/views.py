from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from .models import User

# Create your views here.
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response(
            {"error": "Please provide both username and password"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    user = authenticate(username=username, password=password)
    if not user:
        return Response(
            {"error": "Invalid Credentials"}, status=status.HTTP_404_NOT_FOUND
        )
    auth_login(request, user)
    token, _ = Token.objects.get_or_create(user=user)
    return Response(
        {"detail": "Token was sent."},
        headers={"token": token.key},
        status=status.HTTP_200_OK,
    )


@csrf_exempt
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def logout(request):
    if not request.user:
        return Response(
            {"error": "Invalid Credentials"}, status=status.HTTP_404_NOT_FOUND
        )
    try:
        request.user.auth_token.delete()
    except:
        return Response(
            {"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST
        )
    auth_logout(request)
    return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
