from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.crypto import get_random_string

class Store(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug=models.SlugField(blank=True, unique= True)

    def __str__(self):
        return self.name

def create_slug(instance, new_slug=None):

    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=get_random_string(size=4)
                )
        return create_slug(instance, new_slug=new_slug)
    return slug


@receiver(pre_save, sender=Store)
def generate_slug(instance, *args, **kwargs):
    instance.slug=create_slug(instance)
