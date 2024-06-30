from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet


router = routers.DefaultRouter()
router.register('follow', FollowViewSet, basename='follow')
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register(r'^posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]

# Я вставил из теории, и думал что одно токин, а другое для пользователей
# Почитал у JWT тоже есть работа с пользователем и токен Json
# urlpatterns = [
#     ...
#     # Djoser создаст набор необходимых эндпоинтов.
#     # базовые, для управления пользователями в Django:
#     path('auth/', include('djoser.urls')),
#     # JWT-эндпоинты, для управления JWT-токенами:
#     path('auth/', include('djoser.urls.jwt')),
# ]
