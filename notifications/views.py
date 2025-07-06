from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Notification, Comment
from .serializers import NotificationSerializer, CommentSerializer
from django.utils import timezone

class NotificationListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user).order_by('-created_at')
    
class MarkAsReadView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()

    def patch(self, request, *args,**kwargs):
        notification = self.get_objects()
        if notification.user != request.user:
            return Response({"error":"Unauthorized"}, status=403)
        notification.is_read = True
        notification.save()

        return Response({"message": "Notification marked as read"}, status=200)

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        comment = serializer.save(user=self.request.user)
        # Create a notification for the user
        if comment.parent and comment.parent.user != self.request.user:
            Notification.objects.create(
                user=comment.parent.user,   # receiver
                comment=comment,            # the new reply
                is_read=False
            )

class CommentListView(generics.ListAPIView):
    queryset = Comment.objects.filter(parent=None, is_deleted=False).order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class CommentUpdateView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.user != request.user:
            return Response({"error": "Unauthorized"}, status=403)
        if not hasattr(comment, 'can_edit') or not comment.can_edit():
            return Response({"error": "Edit window expired"}, status=403)
        return super().update(request, *args, **kwargs)
    
class CommentDeleteView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.user != request.user:
            return Response({"error": "Unauthorized"}, status=403)
        comment.is_deleted = True
        comment.save()
        return Response({"message": "Comment deleted (soft)"})
    
class CommentRestoreView(generics.GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.user != request.user:
            return Response({"error": "Unauthorized"}, status=403)
        if comment.can_restore():
            comment.is_deleted = False
            comment.save()
            return Response({"message": "Comment restored"})
        return Response({"error": "cannot restore now"}, status=403)

class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

