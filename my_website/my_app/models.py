from django.db import models


# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.top_name


class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class UsersList(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return str(self.first_name)


class UserMessages(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField(max_length=100)

    def __str__(self):
        return str(self.name)