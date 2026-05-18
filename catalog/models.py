from django.db import models

# Create your models here.

class Show(models.Model):
    SHOW_TYPES = (
        ('MOVIE' , 'Movie'),
        ('ANIME', 'Anime')
    )

    title = models.CharField(max_length=255)
    # Api
    tmdb_id = models.IntegerField(unique=True) 
    show_type = models.CharField(max_length=10,choices=SHOW_TYPES)
    description = models.TextField(blank=True, null=True)
    # Image Link
    poster_url = models.URLField(max_length=500)
    release_date = models.DateField(blank=True, null=True)
    rating = models.FloatField(default=0.0)

    affiliate_link = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.title} {self.show_type}"

# 2 Platform Table : Netflex , crunchyroll
class StreamingPlatform(models.Model):
    name = models.CharField(max_length=100)
    logo_url = models.URLField(max_length=500 , blank=True , null=True)

    def __str__(self):
        return self.name
    
# Affilliate Links 
class AffilliateLink(models.Model):
    show = models.ForeignKey(Show , on_delete=models.CASCADE, related_name='affiliate')
    platform = models.ForeignKey(StreamingPlatform, on_delete=models.CASCADE)
    # Affilliate
    url = models.URLField(max_length=1000)

    def __str__(self):
        return f"{self.show.title} - {self.platform.name}"