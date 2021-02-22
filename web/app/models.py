from django.db import models

# Create your models here.

"""
  - Fields of task:
      - name
          - Type: String
      - status
          - Type: Bool
          - Value
              - 0=Incomplete
              - 1=Complete
"""


class Task(models.Model):
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
