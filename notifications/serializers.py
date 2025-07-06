from rest_framework import serializers
from .models import Notification
from comments.serializers import CommentSerializer

class NotificationSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(read_only=True)

    class Meta:
        model = Notification
        fields = ('id',  'comment', 'is_read', 'created_at')
       