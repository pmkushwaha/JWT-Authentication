from django.db import models
from django.core.validators import MinValueValidator ,MaxValueValidator

# Create your models here.
class StreamPlatform(models.Model):
    name=models.CharField(max_length=20)
    about=models.CharField(max_length=100)
    website=models.URLField(max_length=200)

    def __str__(self) :
        return self.name
    
class WatchList(models.Model):
    title=models.CharField(max_length=50)
    storyLine=models.CharField(max_length=200)
    StramPlatform=models.ForeignKey(StreamPlatform, on_delete=models.CASCADE,related_name="watchlist")
    created=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class Review(models.Model):
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description=models.CharField(max_length=200)
    watchList=models.ForeignKey(WatchList,on_delete=models.CASCADE,related_name='review')
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return str(self.rating )+" | "+self.watchList.title