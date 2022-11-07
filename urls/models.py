import random
import string
from django.db import models


def generate_random_key(n=5):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))


class URL(models.Model):
    key = models.CharField(max_length=5, default='', blank=True)
    secret_key = models.CharField(max_length=14, default='', blank=True)
    target_url = models.URLField(max_length=2048)
    is_active = models.BooleanField(default=True)
    clicks = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.id:
            is_unique = False
            while not is_unique:
                key = generate_random_key()
                is_unique = not self.__class__.objects.filter(key=key).exists()
            self.key = key
            self.secret_key = f'{key}_{generate_random_key(8)}'
        super(URL, self).save(*args, **kwargs)

    def __str__(self):
        return self.key
