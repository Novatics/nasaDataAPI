from django.db import models

class Satellite(models.Model):

    id = models.AutoField(
        primary_key=True
    )

    satellite_type = models.CharField(
        ('Satellite Type'),
		max_length=25,
        blank=False,
    )

    name = models.CharField(
		('Name'),
		help_text=("Satellite Name"),
		max_length=50,
        blank=False,
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
