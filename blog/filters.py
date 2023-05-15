from blog.models import Comment, Post

from django_filters import rest_framework as filters


class PostFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Post
        fields = ['author']


class CommentFilter(filters.FilterSet):

    class Meta:
        model = Comment
        fields = ['author', 'post']


class UserFilter(filters.FilterSet):
    username = filters.CharFilter(lookup_expr='contains')
