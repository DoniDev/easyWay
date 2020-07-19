from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill


class Post(models.Model):
    title = models.CharField(default='', max_length=100)
    body = models.TextField(default='', blank=True, unique=True)
    # body = RichTextField(blank=True, null=True)
    slug = models.SlugField(default='', blank=True, max_length=255)
    created = models.DateTimeField(auto_now_add=True)  # adds date automatically
    updated = models.DateTimeField(auto_now=True)  # updates the date when it is updated
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)  # one-to-many relationship
    tags = TaggableManager()
    image = models.ImageField(upload_to='images', default='', blank=True)
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(700, 700  )],
                                     format='JPEG', options={'quality': 60})




    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:detail',
                       args=[str(self.slug)])

