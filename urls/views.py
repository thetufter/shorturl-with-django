from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import URL
from .serializers import URLSerializer


class RootUrlApiView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(
            f"Welcome to ShortURL app!",
            status=status.HTTP_200_OK
        )

    def post(self, request, *args, **kwargs):
        data = {
            'target_url': request.data.get('target_url'),
        }
        serializer = URLSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ForwardUrlApiView(APIView):
    def get_object(self, key):
        try:
            return URL.objects.get(key=key, is_active=True)
        except URL.DoesNotExist:
            return None

    def get(self, request, key, *args, **kwargs):
        url = self.get_object(key)
        if not url:
            return Response(
                "Short URL does not exists",
                status=status.HTTP_400_BAD_REQUEST
            )

        url.clicks += 1
        url.save()
        return redirect(url.target_url)


class UrlAdminApiView(APIView):
    def get_object(self, secret_key):
        try:
            return URL.objects.get(secret_key=secret_key, is_active=True)
        except URL.DoesNotExist:
            return None

    def get(self, request, secret_key, *args, **kwargs):
        url = self.get_object(secret_key)

        if not url:
            return Response(
                "Short URL does not exists",
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = URLSerializer(url)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, secret_key, *args, **kwargs):
        url = self.get_object(secret_key)

        if not url:
            return Response(
                "Short URL does not exists",
                status=status.HTTP_400_BAD_REQUEST
            )

        url.is_active = False
        url.save()

        return Response(
            f"Short URL with key {url.key} has been deleted",
            status=status.HTTP_200_OK
        )
