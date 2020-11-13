from django.db import models
from django.urls import reverse
from django.conf import settings

import misaka
# Create your models here.

from groups.models import Group

from django.contrib.auth import get_user_model
User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.PROTECT)
    # automatic post time
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name='posts', null=True, blank=True, on_delete=models.PROTECT)

    def __self__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:single', kwargs={'username': self.user.username, 'pk': self.pk})
    
    widgets = {
            'title': forms.TextInput(attrs={'class': 'form-post-title', 'placeholder': 'Enter post title'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea form-post-content',
                                          'placeholder': 'Enter post text'})
        }

    class Meta:
        # descending order
        ordering = ['-created_at']
        unique_together = ['user', 'message']
