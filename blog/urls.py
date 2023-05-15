from blog import views

from django.urls import include, path

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename="user")
router.register(r'posts', views.PostViewSet, basename="post")
router.register(r'comments', views.CommentViewSet, basename="comment")

urlpatterns = [
    path('', include(router.urls)),
]
