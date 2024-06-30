from rest_framework.generics import get_object_or_404
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import viewsets, permissions, mixins
from drf_spectacular.utils import extend_schema, OpenApiResponse

from posts.models import Post, Group
from .serializers import (
    PostSerializer,
    GroupSerializer,
    CommentSerializer,
    FollowSerializer,
)
from .permissions import IsAuthorOrReadOnly


@extend_schema(
    responses={
        200: PostSerializer,
        404: OpenApiResponse(
            description='Empty response, post by id not found'),
    }
)
class FollowViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    """Список подписок."""

    serializer_class = FollowSerializer
    filter_backends = [SearchFilter]
    search_fields = ['following__username']

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@extend_schema(
    responses={
        200: PostSerializer,
        404: OpenApiResponse(
            description='Empty response, post by id not found'),
    }
)
class PostViewSet(viewsets.ModelViewSet):
    """Список постов."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly,
                          permissions.IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@extend_schema(
    responses={
        200: GroupSerializer,
        404: OpenApiResponse(
            description='Empty response, post by id not found'),
    }
)
class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Список групп."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


@extend_schema(
    responses={
        200: CommentSerializer,
        404: OpenApiResponse(
            description='Empty response, post by id not found'),
    }
)
class CommentViewSet(viewsets.ModelViewSet):
    """Список комментариев."""

    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly,
                          permissions.IsAuthenticatedOrReadOnly]

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def get_queryset(self):
        post = self.get_post()
        return post.comments.all()

    def perform_create(self, serializer):
        post = self.get_post()
        serializer.save(author=self.request.user, post=post)
