from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.api.views import UserViewSet, PostViewSet, CommentViewSet, LikeViewSet

router = DefaultRouter()

router.register('users', UserViewSet, 'user')
router.register('posts', PostViewSet, 'posts')
router.register('comment', CommentViewSet, 'comment')
router.register('likes', LikeViewSet, 'like')
# router.register('comment', CommentViewSet, 'comment')

urlpatterns = [
    path('', include(router.urls))
]