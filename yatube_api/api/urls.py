from django.urls import path, include
from rest_framework import routers

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet
from django.views.generic import TemplateView


router = routers.DefaultRouter()
router.register('follow', FollowViewSet, basename='follow')
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register(r'^posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]
