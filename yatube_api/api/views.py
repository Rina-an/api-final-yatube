from django.shortcuts import get_object_or_404

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters, mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (AllowAny,
                                        IsAuthenticated,
                                        IsAuthenticatedOrReadOnly,
                                        )

from api.permissions import IsAuthorOrReadOnly
from api.serializers import (CommentSerializer,
                             FollowSerializer,
                             GroupSerializer,
                             PostSerializer,
                             )
from posts.models import Comment, Group, Post


class PostViewSet(viewsets.ModelViewSet):
    """
    Вьюсет для постов.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """Метод пишет авторство автоматически при создании поста."""
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Вьюсет для групп.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (AllowAny, )


class FollowViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet
                    ):
    """
    Вьюсет для подписок.
    """

    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated, )
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('user', 'following')
    search_fields = ('user__username', 'following__username')

    def get_queryset(self):
        """Метод для получения подписчиков пользователя."""
        return self.request.user.follows.all()

    def perform_create(self, serializer):
        """Метод передает user.id подписанта при подписке на пользователя."""
        serializer.save(user=self.request.user)


class CommentsViewSet(viewsets.ModelViewSet):
    """
    Вьюсет для комментариев.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)

    def get_post(self):
        """Метод для получения конкретного поста."""
        return get_object_or_404(
            Post,
            pk=self.kwargs['post_id']
        )

    def get_queryset(self):
        """Метод для получения комментариев поста."""
        post = self.get_post()
        return post.comments.all()

    def perform_create(self, serializer):
        """Метод для передачи айди поста и авторства при создании коммента."""
        post = self.get_post()
        serializer.save(author=self.request.user, post=post)
