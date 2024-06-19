from datetime import date

from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(
        blank=True,
        null=True
    )
    budget = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    duration_in_days = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='Duration in Days'
    )

    estimated_hours = models.FloatField(
        null=True,
        blank=True,
        verbose_name='Estimated Hours'
    )

    start_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Start Date',
        default=date.today()
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )

    last_edited_on = models.DateTimeField(
        auto_now=True,
        editable=False
    )
