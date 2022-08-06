from django.db import models


class Password(models.Model):
    name = models.CharField(max_length=255, verbose_name='name')
    url = models.URLField(verbose_name='url')
    username = models.CharField(max_length=255, verbose_name='username')
    password = models.CharField(max_length=255, verbose_name='password')

    class Meta:
        verbose_name = 'password'
        verbose_name_plural = 'passwords'

    def __str__(self):
        return self.password
