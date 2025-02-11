import uuid
from django.db import models
from ats_project.constants import GENDER_CHOICES


class Candidate(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Unique Identifier
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
