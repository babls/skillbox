import os
from uuid import uuid4

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.deconstruct import deconstructible
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _


@deconstructible
class UploadToPathAndRename(object):

    def __init__(self, path):
        self.sub_path = path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.sub_path, filename)


class BlogPost(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    text = models.TextField(max_length=1000, verbose_name=_('text'))
    dataCreate = models.DateTimeField(default=now, blank=True, verbose_name=_('data create'))
    dateEdit = models.DateTimeField(default=now, blank=True, verbose_name=_('date edit'))
    activity = models.BooleanField(default=False, verbose_name=_('activity'), blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('author'))

    def __str__(self):
        return f'{self.id}'
        # return f'{self.name}, {self.dataCreate}, {self.activity}'

    class Meta:
        verbose_name_plural = _('blogs')
        verbose_name = _('blog')


class FilesPost(models.Model):
    file = models.FileField(
        upload_to=UploadToPathAndRename(os.path.join(settings.MEDIA_ROOT, 'upload', 'here')),
        null=True, blank=True, verbose_name=_('activity'))
    post_id = models.ForeignKey(BlogPost, on_delete=models.CASCADE,
                                verbose_name=_('The post to which the image is attached'))

    def __str__(self):
        return f'{self.post_id}, {self.file}'

    class Meta:
        verbose_name_plural = _('files post')
        verbose_name = _('file post')
