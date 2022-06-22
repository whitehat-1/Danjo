from django.contrib import admin

# Register your models here.
class Post(models.Model):

    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published")
    )

