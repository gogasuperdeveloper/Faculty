from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=255)
    head = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50)
    description = models.TextField()
    coordinator_name = models.CharField(max_length=255)
    coordinator_contact = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    disciplines = models.TextField()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class HomePage(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    info = models.TextField()
    contacts = models.TextField()

    def __str__(self):
        return self.title


class ExchangeProgram(models.Model):
    university = models.CharField(max_length=255)
    country = models.CharField(max_length=255, default="")
    languages = models.CharField(max_length=255)
    places = models.CharField(max_length=255)
    deadline = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.university
