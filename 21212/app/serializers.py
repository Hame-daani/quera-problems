from rest_framework import serializers
from app.models import Comment, Post


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ("title", "body", "created", "owner")

    def get_owner(self, obj):
        return obj.owner.username


class PostDetailSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()
    comment_set = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="comment_detail"
    )

    class Meta:
        model = Post
        fields = ("title", "body", "created", "updated", "owner", "comment_set")

    def get_owner(self, obj):
        return obj.owner.username


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()
    post = serializers.HyperlinkedRelatedField(read_only=True, view_name="post_detail")

    class Meta:
        model = Comment
        fields = ("post", "owner", "body", "created", "updated")

    def get_owner(self, obj):
        return obj.owner.username
