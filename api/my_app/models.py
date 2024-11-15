from django.db import models

def musician_avatar_directory_path(instance: "Musician", filename: str) -> str:
    return 'accounts/user_{pk}/avatar/{filename}'.format(
        pk=instance.pk,
        filename=filename
    )

class Musician(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    musical_instrument = models.CharField(max_length=100, null=False, blank=False)
    experience = models.CharField(max_length=100)
    info = models.TextField(null=False, blank=True)
    avatar = models.CharField(max_length=250, null=False, blank=True)
    sample = models.CharField(max_length=100, null=False, blank=True)
    user_tg = models.IntegerField(null=False, blank=False)



class Band(models.Model):
    name = models.CharField(max_length=100)
    musical_genre = models.CharField(max_length=250)
    who_need = models.CharField(max_length=250)
    info = models.TextField(null=False, blank=True)
    sample = models.CharField(max_length=100, null=False, blank=True)
    user_tg = models.IntegerField(null=False, blank=False)
