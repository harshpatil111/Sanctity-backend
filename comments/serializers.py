from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    can_edit = serializers.ReadOnlyField()
    can_restore = serializers.ReadOnlyField()

    class Meta:
        model = Comment
        fields = ['id', 'user', 'content', 'parent', 'created_at', 'updated_at', 'is_deleted', 'replies', 'can_edit', 'can_restore']
        read_only_fields = [ 'user', 'created_at', 'updated_at', 'replies']

    def get_replies(self, obj):
        if obj.replies.exists():
            return CommentSerializer(obj.replies.all(), many=True).data
        return []
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
    
