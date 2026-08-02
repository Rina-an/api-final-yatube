from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CommentsViewSet, GroupViewSet, PostViewSet, FollowViewSet

router_v1 = DefaultRouter()

router_v1.register('posts',
                   PostViewSet,
                   basename='posts'
                   )
router_v1.register('follow',
                   FollowViewSet,
                   basename='follow'
                   )
router_v1.register('groups',
                   GroupViewSet,
                   basename='groups'
                   )
router_v1.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentsViewSet,
                   basename='comments'
                   )

v1_urls = [
    path('', include(router_v1.urls)),
    path('', include('djoser.urls.jwt')),
]

urlpatterns = [
    path('v1/', include(v1_urls)),
]
