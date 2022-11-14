from django.db import models

from studentapp.validators import gmail_validation

CHOICES_CLASS = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
    ("11", "11"),
    ("12", "12"),
)

class Student(models.Model):
    name = models.CharField(
        max_length=50,
        blank=False,
        null=True,
    )
    email = models.EmailField(
        max_length=100,
        blank=False,
        null=True,
        validators=[gmail_validation],
    )
    age = models.IntegerField(
        blank=False,
        null=True,
    )
    claass = models.CharField(
        max_length=200,
        blank=False,
        null=True,
        choices = CHOICES_CLASS,
        default = ''
    )

    content = models.TextField()

    def __str__(self):
        return self.name