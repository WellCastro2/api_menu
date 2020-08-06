import uuid
from django.db import models


class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    updated_at = models.DateTimeField(u'Data Atualização', auto_now=True, blank=False, null=False)
    created_at = models.DateTimeField(u'Data criado', auto_now_add=True, blank=False, null=False)
    active = models.BooleanField(u'Ativo', default=True)

    class Meta:
        abstract = True
