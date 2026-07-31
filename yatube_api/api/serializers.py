from rest_framework import serializers
from django.contrib.auth.models import User

from posts.models import Comment, Group, Post, Follow


class GroupSerializer(serializers.ModelSerializer):
    """
    Класс сериалайзера для группы постов.
    """

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class FollowSerializer(serializers.ModelSerializer):
    """
    Класс сериалайзера для подписок.
    """

    user = serializers.SlugRelatedField(read_only=True,
                                        slug_field='username'
                                        )
    following = serializers.SlugRelatedField(slug_field='username',
                                             queryset=User.objects.all()
                                             )

    class Meta:
        model = Follow
        fields = ('following', 'user')
        read_only_fields = ('user', )

    def validate(self, data):
        user = self.context['request'].user
        following = data['following']
        if user == following:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя.'
            )
        if Follow.objects.filter(
            user=user,
            following=following
        ).exists():
            raise serializers.ValidationError(
                'Вы уже подписаны на этого пользователя.'
            )

        return data


class CommentSerializer(serializers.ModelSerializer):
    """
    Класс сериалайзера для комментариев.
    """

    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username'
                                          )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'text', 'created', 'post')
        read_only_fields = ('post', )


class PostSerializer(serializers.ModelSerializer):
    """
    Класс сериалайзера для постов.
    """

    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username'
                                          )

    class Meta:
        model = Post
        fields = ('id',
                  'text',
                  'author',
                  'image',
                  'group',
                  'pub_date')
