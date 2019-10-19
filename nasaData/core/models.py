from django.db import models
from django.core.validators import FileExtensionValidator


class Satellite(models.Model):

    id = models.AutoField(
        primary_key=True
    )

    satellite_type = models.CharField(
        ('Satellite Type'),
		max_length=255,
        blank=False,
    )

    name = models.CharField(
		('Name'),
		help_text=("Satellite Name"),
		max_length=255,
        blank=False,
	)

    codename = models.CharField(
		('Codename'),
		help_text=("Satellite Codename"),
		max_length=255,
        blank=False,
        default=name
	)

    description = models.TextField(
		('Description'),
		help_text=("Satellite Description"),
        blank=False,
	)

    launch_date = models.DateField(
        ('Launch Date'),
        blank=False,
    )
