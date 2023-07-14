from django.db import models


class UploadedFile(models.Model):
    file = models.FileField(upload_to='files/')
    word_size = models.IntegerField(blank=False, null=False)
