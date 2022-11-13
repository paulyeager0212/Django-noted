from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


def user_directory_path(instance, filename):
    """Return a path to a user's profile picture."""
    return f'user/avatars/{instance.user.id}/{filename}'


class Profile(models.Model):
    """Additional fields to a :model:`user.User`.
    
    **Fields**
        user: a link to a :model:`user.User`.
        avatar: a profile picture.
        bio: a biography (additional info about user).
        
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE,
        related_name='profile')
    avatar = models.ImageField(upload_to=user_directory_path,
                               default='user/default_avatar.jpg')
    bio = models.TextField(max_length=700, blank=True)

    def __str__(self):
        return f'Profile: {self.user}'


class Contact(models.Model):
    follower = models.ForeignKey(User, related_name='from_set', db_index=True,
        on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name='to_set', db_index=True,
        on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.follower} follows {self.followed}'
