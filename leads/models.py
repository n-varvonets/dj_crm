from django.db import models

# Create your models here.

class Lead(models.Model):

    SOUCE_CHOICES = (
        ('YouTube', 'YouTube'),  # "as_stored_in_db","as_display_value"
        ('Google', 'Google'),
        ('Gmail', 'Gmail'),
    )

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)

    phoned = models.BooleanField(default=False)
    source = models.CharField(choices=SOUCE_CHOICES, max_length=100)

    profile_picture = models.ImageField(blank=True, null=True)
    special_files = models.FileField(blank=True, null=True)