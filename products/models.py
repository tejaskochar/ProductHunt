from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=200, blank=True)
    pub_date = models.DateTimeField()
    tot_votes = models.IntegerField(default=1)
    image = models.ImageField(upload_to = 'product/')
    icon = models.ImageField(upload_to = 'product/')
    body = models.TextField()
    hunter = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:200]

    def pub_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
