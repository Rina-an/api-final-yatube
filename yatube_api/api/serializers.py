from django.contrib.auth.models import User

from rest_framework import serializers

from posts.models import Comment, Follow, Group, Post


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

    def validate_following(self, data):
        """Метод для проверки самоподписки и двойной подписки на юзера."""
        user = self.context['request'].user
        if user == data:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя.'
            )
        if Follow.objects.filter(
            user=user,
            following=data
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
