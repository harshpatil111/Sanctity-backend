from django.db import models
from django.contrib.auth import get_user_model
from comments.models import Comment

User = get_user_model()

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return f"TO {self.user.username} on Comment #{self.comment.id}"