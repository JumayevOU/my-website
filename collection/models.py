from django.db import models

class Collection(models.Model):
    title = models.CharField(max_length=202)
    image1 = models.ImageField(upload_to='collection/')
    image2= models.ImageField(upload_to='collection/')
    image3= models.ImageField(upload_to='collection/')
    image4= models.ImageField(upload_to='collection/')
    image5= models.ImageField(upload_to='collection/')
    create_date = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.title

# class ProjectImage(models.Model):
#     img = models.ImageField(upload_to="project_images")