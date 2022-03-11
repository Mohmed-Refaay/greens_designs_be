from django.db import models

# Create your models here.


class Section(models.Model):
    title = models.CharField(max_length=50)
    cover_image = models.ImageField(upload_to="")

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=50)
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, related_name="projects")
    content = models.TextField()
    cover_image = models.ImageField(upload_to="")
    
    def __str__(self):
        return self.title

class Image(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField("")

    def __str__(self):
        return self.image.name


class Contact(models.Model):
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    project_details = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
