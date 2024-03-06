from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet

from apps.api.models import User, Post, Comment, Like
from apps.api.serializers import UserCreateSerializer, UserListSerializer, PostSerializer, \
    CommentCreateSerializer, CommentListSerializer, CommentLikeListSerializer, PostDetailSerializer, LikeSerializer


class UserViewSet(ViewSet):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'detail': 'User registered'}, status=status.HTTP_201_CREATED)
        else:
            return Response(data={'detail': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def retrieve(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostDetailSerializer(post)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_active=True)
        return queryset

class CommentViewSet(ViewSet):
    def post(self, request):
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'detail': 'Comment added'}, status=status.HTTP_201_CREATED)
        else:
            return Response(data={'detail': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        queryset = Comment.objects.all()
        serializer = CommentListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=pk)
        serializer = CommentLikeListSerializer(comment)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class LikeViewSet(ViewSet):
    def post(self, request):
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'detail': 'like'}, status=status.HTTP_201_CREATED)
        else:
            return Response(data={'detail': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        queryset = Like.objects.all()
        serializer = LikeSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)