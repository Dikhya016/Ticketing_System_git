from django.db import models

# Create your models here.
from django.db import models

class Ticket(models.Model):
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('Closed', 'Closed')
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    ticket_description = models.TextField()
    category = models.CharField(max_length=20, default='Technical')
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Open')
    creation_date = models.DateField(auto_now_add=True)
    last_modified_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.ticket_description

