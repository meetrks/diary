import datetime

from django.db import models
from django.utils.text import slugify

from core.models import BaseModel, DisplayID
from iam.models import User
from storage.models import ImageCollection

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Tag(BaseModel, DisplayID):
    PREFIX = "TAG"
    name = models.CharField(max_length=250, unique=True, db_index=True)
    slug = models.SlugField(max_length=250, db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    title = models.CharField(max_length=68, null=True, blank=True, help_text="Only for SEO purpose")
    description = models.CharField(max_length=150, null=True, blank=True, help_text="Only for SEO purpose")
    keywords = models.TextField(null=True, blank=True, help_text="Only for SEO purpose")

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Article(BaseModel, DisplayID):
    PREFIX = "ART"
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, db_index=True, unique=True)
    content = models.TextField(null=True, blank=True)
    short_description = models.TextField(null=True, blank=True)
    related_topics = models.ManyToManyField(Tag, related_name='related_articles', blank=True)

    keywords = models.TextField(null=True, blank=True)
    small_poster = models.ForeignKey(ImageCollection, on_delete=models.SET_NULL, null=True, blank=True,
                                     related_name='articles_small_posters')
    main_poster = models.ForeignKey(ImageCollection, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='articles_main_poster')
    creator = models.ForeignKey(User, related_name='articles_created', on_delete=models.SET_NULL, null=True, blank=True,
                                editable=False)
    publisher = models.ForeignKey(User, related_name='articles_published', on_delete=models.SET_NULL, null=True,
                                  blank=True, editable=False)
    published_on = models.DateField(null=True, blank=True, editable=False)

    class Meta:
        ordering = ('-created',)
        unique_together = (('slug',),)

    def save(self, *args, **kwargs):
        self.slug = f"{slugify(self.title)}-{str(self.id)[:8]}"
        if self.is_approved and not self.published_on:
            self.published_on = datetime.date.today()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
