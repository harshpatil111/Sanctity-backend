from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from datetime import timedelta

User = get_user_model()

class Comment(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return timezone.now() - self.created_at <= timedelta(minutes=15)
    
    def can_restore(self):
        return not self.is_deleted and (timezone.now() - self.created_at <= timedelta(minutes=15))
    
    def restore(self):
        return f'comment {self.user.username} - {self.content[:30]}'
