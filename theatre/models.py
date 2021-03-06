import uuid
from django.db import models
# Create your models here.
class Audience(models.Model):
    name = models.CharField(max_length=200, null=True)
    ticketId = models.UUIDField(
            primary_key = True,
            default = uuid.uuid4(),
            editable = False
        )
    seatNo = models.IntegerField(default=0)

