from django.db import models
from django.conf import settings
import base64

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='posts', blank=True, null=True)
    picture_binary = models.BinaryField(blank=True, null=True)
    content_type = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField(max_length=2048, blank=True)
    posted_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if hasattr(self.picture, 'file'):
            self.picture_binary = self.picture.file.read()
            file_ext = self.picture.name.split('.')[-1].lower()
            self.content_type = f'image/{file_ext}'
        super().save(*args, **kwargs)

    def get_image_base64(self):
        if self.picture_binary:
            return base64.b64encode(self.picture_binary).decode('utf-8')
        return None

class Comment(models.Model):
	""" The comments Models """

	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
	post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
	text = models.TextField(max_length=2048, blank=True)
	comment_date = models.DateTimeField(auto_now_add=True)
