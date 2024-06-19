from django.shortcuts import render
from rest_framework import generics,permissions
from .serializers import UserLoginSerializer,BlogPostSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import Blog
from .pagination import LargeResultsSetPagination
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from rest_framework import status

from django.http import Http404
from django.shortcuts import get_object_or_404

class UserLoginView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        username = validated_data['username']
        password = validated_data['password']

        user = authenticate(request, username=username, password=password)
        if not user or not user.is_active:
            return Response({'error': 'Incorrect credentials'}, status=400)

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        return Response({'access_token': access_token, 'refresh_token': refresh_token})

class BlogPostListView(generics.ListAPIView):
    queryset=Blog.objects.all().order_by('-created_at')
    serializer_class=BlogPostSerializer
    pagination_class=LargeResultsSetPagination

from rest_framework.generics import RetrieveAPIView
class BlogPostDetailView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
       
    

class BlogPostListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    pagination_class=LargeResultsSetPagination

    def get(self, request):
        blogs = Blog.objects.filter(user=request.user).order_by('-created_at')
        serializer = BlogPostSerializer(blogs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   




class BlogPostRetrieveUpdateDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_object(self, pk):
        blog = get_object_or_404(Blog, pk=pk, user=self.request.user)
        return blog

    def get(self, request, pk):
        blog = self.get_object(pk)
        serializer = BlogPostSerializer(blog)
        return Response(serializer.data)

    def put(self, request, pk):
        blog = self.get_object(pk)
        serializer = BlogPostSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            blog = self.get_object(pk)
            blog.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Blog.DoesNotExist:
            raise Http404


class BlogPostSearchByHashtagView(generics.ListAPIView):
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        hashtag = self.kwargs['hashtag']
        return Blog.objects.filter(hashtags__contains=hashtag)