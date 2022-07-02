from django.conf import settings
from django.db import models
from django.utils.text import slugify

from core.models import BaseModel


class ImageCollection(BaseModel):
    title = models.CharField(max_length=300, verbose_name="Image Name")
    slug = models.CharField(max_length=300, editable=False, null=True, blank=True, db_index=True)
    file = models.ImageField(max_length=250)
    size = models.PositiveIntegerField(default=0, blank=True, editable=False)

    def __unicode__(self):
        return '%s' % self.file.name

    def __str__(self):
        return '{}-({})'.format(self.title, self.file.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.slug += "-{}".format(str(self.id)[:8])
        self.size = self.file.size
        self.file.name = "{slug}.{ext}".format(
            slug=self.slug, ext=self.file.name.split('.')[-1]
        )
        super(ImageCollection, self).save(*args, **kwargs)

    @property
    def poster_url(self):
        return settings.MEDIA_URL_IMAGES + self.file.name
