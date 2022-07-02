import uuid

from django.db import models
from django.db import transaction


class BasicModel(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created On')
    modified = models.DateTimeField(auto_now=True, verbose_name='Modified On')

    class Meta:
        abstract = True


class BaseModel(BasicModel):
    is_approved = models.BooleanField(default=False, db_index=True)

    class Meta:
        abstract = True


class DisplayID(models.Model):
    PREFIX = ''
    display_id = models.CharField(max_length=20, unique=True, verbose_name='#')

    def get_next_id(self):
        return self.__class__.objects.count() + 1

    def save(self, *args, **kwargs):
        with transaction.atomic():
            if not self.display_id:
                incremental_number = self.get_next_id()
                print(incremental_number, '==========>>>>')
                self.display_id = "{}-{}".format(self.PREFIX, str(incremental_number).zfill(3))
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
