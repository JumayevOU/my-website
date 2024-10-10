from django.db import models

class About(models.Model):
    full_name = models.CharField(max_length=202)
    title = models.CharField(max_length=202)
    image1 = models.ImageField(upload_to='about/')
    image2 = models.ImageField(upload_to='about/')
    description = models.TextField()
    facebook = models.CharField(max_length=202)
    instagram = models.CharField(max_length=202)
    telegram = models.CharField(max_length=202)

    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.full_name