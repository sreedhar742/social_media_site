from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
import base64
from io import BytesIO

class User(AbstractUser):
    """ Custom User Model 
        In cases where we just want to add a new field to the already existing user, subclass
        the `AbstractUser` and add the required fields
        Ensure to update the `settings.AUTH_USER_MODEL` value
    """
    followers = models.ManyToManyField("self", blank=True)

    def is_following(self, user):
        return user in self.followers.all()

class UserProfile(models.Model):
    """ Profile data of user """

    user = models.OneToOneField(User, on_delete=models.CASCADE, 
                                related_name='profile',
                                verbose_name='other Details')
    picture_data = models.BinaryField(blank=True, null=True)
    picture_name = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=11, blank=True)
    address = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if hasattr(self, '_picture_changed') and self._picture_changed:
            img = Image.open(self._picture_file)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
            
            buffer = BytesIO()
            img.save(buffer, format='PNG')
            self.picture_data = buffer.getvalue()
            self.picture_name = self._picture_file.name
            
        super().save(*args, **kwargs)

    def set_picture(self, picture_file):
        self._picture_file = picture_file
        self._picture_changed = True

    @property
    def picture_url(self):
        if self.picture_data:
            return f"data:image/png;base64,{self.get_picture_base64()}"
        return None

    def get_picture_base64(self):
        if self.picture_data:
            return base64.b64encode(self.picture_data).decode('utf-8')
        return None

@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    """ Create a profile anytime a new user is created """
    if kwargs['created']:
        user_profile = UserProfile.objects.get_or_create(
                                    user=kwargs['instance']
                                    )

