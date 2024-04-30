from django.db import models


class SpecialistsRegistry(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True, null=True)
    speciality = models.TextField(blank=True, null=True)
    certification_category = models.CharField(max_length=150, blank=True, null=True)
    category_assignment_order = models.CharField(max_length=100, blank=True, null=True)
    contact_details = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'specialists_registry'
