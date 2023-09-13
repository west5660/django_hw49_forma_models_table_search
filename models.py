from django.db import models


class Company(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    firma = models.ForeignKey(Company, on_delete=models.CASCADE)
    volume = models.DecimalField(max_digits=10, decimal_places=2)  # Поле "Объем"
    packaging = models.CharField(max_length=100)  # Поле "Упаковка"
    is_recommended = models.BooleanField(default=False)  # Поле "Рекомендован"

    def __str__(self):
        return self.name

class Course(models.Model):
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Student(models.Model):
    name=models.CharField(max_length=20)
    group=models.CharField(max_length=4)
    course = models.ManyToManyField(Course)

    def __str__(self):
        return self.name
