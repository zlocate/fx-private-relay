import datetime

from django.contrib.auth.models import User
from django.db import models

DEFAULT_TEMP_NUM_DURATION = datetime.timedelta(seconds=5*60)


class Session(models.Model):
    twilio_sid = models.CharField(max_length=34, unique=True, blank=False)
    initiating_proxy_number = models.CharField(max_length=20, blank=False)
    initiating_real_number = models.CharField(max_length=20, blank=False)
    initiating_participant_sid = models.CharField(max_length=34, blank=False)
    status = models.CharField(max_length=20, blank=False)
    expiration = models.DateTimeField(null=True)


class TemporaryNumber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=False)
    duration = models.DurationField(
        blank=False,
        default=DEFAULT_TEMP_NUM_DURATION
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    last_modified_at = models.DateTimeField(auto_now=True, db_index=True)
