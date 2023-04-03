from django.db import models
from tinymce.models import HTMLField
import uuid


# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=255)
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(null=False, blank=False)
    content = HTMLField()
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
