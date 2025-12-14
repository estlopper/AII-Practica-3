from django.db import models

# Create your models here.
class Tag(models.Model):
    id = models.IntegerField(primary_key=True)
    value = models.CharField()

    def __str__(self):
        return self.value

class Artist(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField()
    url = models.URLField()
    picture_url = models.URLField(blank=True)

    def __str__(self):
        return self.name

class UserArtist(models.Model):
    user = models.IntegerField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    listen_time = models.TextField()

    def __str__(self):
        return f'User {self.user} - Artist {self.artist.name}'

class UserTagArtist(models.Model):
    user = models.IntegerField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    day = models.TextField()
    month = models.TextField()
    year = models.TextField()

    def __str__(self):
        return f'User {self.user} - Artist {self.artist.name} - Tag {self.tag.value}'

